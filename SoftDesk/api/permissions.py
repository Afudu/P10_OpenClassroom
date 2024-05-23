from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import Project


class IsAuthorOrReadOnly(BasePermission):
    """
      Custom Object-level permission to only allow obj authors to edit and delete an object.
    """

    message = "You have to be the author to update or delete."

    def has_object_permission(self, request, view, obj):
        # Checks whether the request is a read or a write operation,
        # against SAFE_METHODS = tuple containing 'GET', 'OPTIONS' and 'HEAD'.
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the object.
        return obj.author == request.user


class IsProjectAuthor(BasePermission):
    """
    view-level permission to only allow access to project's author.
    """
    message = "You have to be the author of this project to access."

    def has_permission(self, request, view):
        """
        view-level permission
        """
        # GET and POST
        project_id = view.kwargs.get("project_pk")
        project = Project.objects.get(pk=project_id)

        # check if the logged-in user is the author.
        if request.user == project.author:
            return True


class IsProjectContributor(BasePermission):
    """
    view-level permission to only allow access to project's contributors.
    """
    message = "You have to be a project contributor to access."

    def has_permission(self, request, view):
        """
        view-level permission
        """
        # GET and POST
        project_id = view.kwargs.get("project_pk")
        project = Project.objects.get(pk=project_id)

        # check if the logged-in user is a contributor.
        if request.user in project.contributors.all():
            return True


class IsProjectAuthorOrContributor(BasePermission):
    """
    view-level permission to only allow access to project's author or its contributors.
    """
    message = "You have to be the author or a contributor of this project to access."

    def has_permission(self, request, view):
        """
        view-level permission
        """
        # GET and POST
        project_id = view.kwargs.get("project_pk")
        project = Project.objects.get(pk=project_id)

        # check if the logged-in user is a contributor.
        if request.user == project.author or request.user in project.contributors.all():
            return True


class IsAccountOwnerOrReadOnly(BasePermission):
    """
      Object-level permission to only allow users to update and delete their own account.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner.
        return obj.id == request.user.id
