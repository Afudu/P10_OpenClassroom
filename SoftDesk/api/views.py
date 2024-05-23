from django.conf import settings
from api.permissions import IsAuthorOrReadOnly, IsProjectAuthor, IsProjectContributor, IsAccountOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from api.models import User, Project, Issue, Comment
from rest_framework.viewsets import ModelViewSet
from api.serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserDetailSerializer,

    ProjectCreateSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,

    ContributorCreateSerializer,
    ContributorListSerializer,
    ContributorDetailSerializer,

    IssueCreateSerializer,
    IssueListSerializer,
    IssueDetailSerializer,

    CommentCreateSerializer,
    CommentListSerializer,
    CommentDetailSerializer
)


class UserViewSet(ModelViewSet):
    """
    ViewSet for creating, viewing and editing Users.
    """

    permission_classes = [IsAccountOwnerOrReadOnly]

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        """
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'list':
            return UserListSerializer
        elif self.action == 'retrieve':
            return UserDetailSerializer
        return UserDetailSerializer  # default serializer

    def get_queryset(self):
        """
        This view should return a list of users based on the queryset.
        """
        # Users list ordered by date joined.
        return User.objects.all().order_by("date_joined")


class ProjectViewSet(ModelViewSet):
    """
    ViewSet for creating, viewing and editing Projects.
    """
    permission_classes = [IsAuthorOrReadOnly]

    # The _project variable is created to avoid unnecessary database queries.
    _project = None

    @property
    def project(self):
        """
        Then the attribute project is created by adding the built-in @property decorator.
        This attribute is available in the view and can be called in the serializer.
        https://docs.python.org/3/library/functions.html#property
        """
        # The _project variable is created to avoid unnecessary database queries.
        # If the view was never accessed, a database query will be made.
        # Else, _project will have a value and no database query will be performed.
        if self._project is None:
            # self._project = Project.objects.all()
            self._project = Project.objects.filter(contributors=self.request.user)

        return self._project

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateSerializer
        elif self.action == 'list':
            return ProjectListSerializer
        elif self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectCreateSerializer  # default serializer

    def get_queryset(self):
        # use order_by to avoid the warning for the pagination
        return self.project.order_by("created_time")

    def perform_create(self, serializer):
        """
        Creation of a model instance.
        """
        # upon creation, the logged-in user is saved as author and as contributor.
        serializer.save(author=self.request.user, contributors=[self.request.user])


class ContributorViewSet(ModelViewSet):
    """
    A ViewSet for adding, viewing and adding project contributors.
    """

    permission_classes = [IsProjectAuthor]

    # The _project variable is created to avoid unnecessary database queries.
    _project = None

    @property
    def project(self):
        """create an attribute project inside the ContributorViewSet
        this attribute is available in the view and can be called/available in the serializer
        """

        # if the view was never executed before, we will make the database query;
        # otherwise, _project will have a value and no database query will be performed
        if self._project is None:
            self._project = get_object_or_404(
                Project.objects.all().prefetch_related("contributors"),
                pk=self.kwargs["project_pk"],
            )
        return self._project

    def get_queryset(self):
        # Returns contributors ordered by 'date_joined' to avoid the pagination warning.
        return self.project.contributors.all().order_by("date_joined")

    def get_serializer_class(self):
        if self.action == 'create':
            return ContributorCreateSerializer
        elif self.action == 'list':
            return ContributorListSerializer
        elif self.action == 'retrieve':
            return ContributorDetailSerializer
        return ContributorCreateSerializer  # default serializer

    # adds a contributor
    def perform_create(self, serializer):
        self.project.contributors.add(serializer.validated_data["user"])

    # removes a contributor
    def perform_destroy(self, instance):
        self.project.contributors.remove(instance)


class IssueViewSet(ModelViewSet):
    """
    ViewSet for creating, viewing and editing Issues in a Project.
    """
    permission_classes = [IsAuthorOrReadOnly, IsProjectContributor]

    _issue = None

    @property
    def issue(self):
        if self._issue is None:
            self._issue = Issue.objects.filter(project_id=self.kwargs["project_pk"])

        return self._issue

    def get_queryset(self):
        return self.issue.order_by("created_time")
        # return Issue.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return IssueCreateSerializer
        elif self.action == 'list':
            return IssueListSerializer
        elif self.action == 'retrieve':
            return IssueDetailSerializer
        return IssueCreateSerializer  # default serializer

    # upon creation, save the logged-in user as author and assignee
    def perform_create(self, serializer):
        selected_assignee = serializer.validated_data["assignee"]
        project_pk = self.kwargs["project_pk"]
        project = get_object_or_404(Project, id=project_pk)
        serializer.save(author=self.request.user, assignee=selected_assignee, project=project)


class CommentViewSet(ModelViewSet):
    """
    ViewSet for creating, viewing and editing Comments made in an Issue.
    """
    permission_classes = [IsAuthorOrReadOnly, IsProjectContributor]

    _comment = None

    @property
    def comment(self):
        if self._comment is None:
            self._comment = Comment.objects.filter(issue_id=self.kwargs["issue_pk"])

        return self._comment

    def get_queryset(self):
        return self.comment.order_by("created_time")

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        elif self.action == 'list':
            return CommentListSerializer
        elif self.action == 'retrieve':
            return CommentDetailSerializer
        return CommentCreateSerializer  # default serializer

    # upon creation, save the logged-in user as author
    def perform_create(self, serializer):
        project_pk = self.kwargs["project_pk"]
        issue_pk = self.kwargs["issue_pk"]
        issue = get_object_or_404(Issue, id=issue_pk)
        issue_url = f"{settings.BASE_URL}/api/projects/{project_pk}/issues/{issue_pk}/"

        author = self.request.user
        serializer.save(author=author, issue=issue, issue_url=issue_url)
