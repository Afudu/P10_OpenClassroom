from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Custom User model for creating users"""
    age = models.IntegerField(verbose_name="age")
    contact_consent = models.BooleanField(default=False, verbose_name="contact consent")
    data_share_consent = models.BooleanField(default=False, verbose_name="data share consent")

    def __str__(self):
        return self.username


class Project(models.Model):
    """ Project model for creating projects"""
    # Short project_types
    objects = None
    BACKEND = "B"
    FRONTEND = "F"
    IOS = "I"
    ANDROID = "A"

    # Long project_types
    PROJECT_TYPES = [
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    ]

    name = models.CharField(max_length=100, verbose_name="name of project")
    description = models.TextField(verbose_name="project description")
    type = models.CharField(max_length=1, choices=PROJECT_TYPES, verbose_name="project type")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        related_name="project_author",
        verbose_name="project author",
    )
    contributors = models.ManyToManyField(
        User,
        blank=True,
        related_name="project_contributors",
        verbose_name="project contributors",
    )

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="created on")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="updated on")
    # issues_url = models.URLField(blank=True, verbose_name="issues url")
    # contributors_url = models.URLField(blank=True, verbose_name="contributors url")

    def __str__(self):
        return f"Project: {self.name} ¦ Author: {self.author}"


class Issue(models.Model):
    """
    Issue model for creating issues.
    Issue is related to a project, the default state is ToDo.
    An issue can be assigned to a contributor or to the author itself.
    The default assignee will be its author.
    """

    objects = None

    # Short issue tags
    BUG = "B"
    FEATURE = "F"
    TASK = "T"

    # Long issue tags
    TAGS = [
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task"),
    ]

    # Short issue states
    TODO = "T"
    IN_PROGRESS = "I"
    COMPLETED = "C"

    # Long issue states
    STATES = [
        (TODO, "ToDo"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
    ]

    # Short issue priorities
    LOW = "L"
    MEDIUM = "M"
    HIGH = "H"

    # Long issue priorities
    PRIORITIES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]
    name = models.CharField(max_length=100, verbose_name="name of issue")
    description = models.TextField(verbose_name="issue description")
    tag = models.CharField(max_length=2, choices=TAGS, verbose_name="issue tag")
    state = models.CharField(
        max_length=2, choices=STATES, default=TODO, verbose_name="issue state"
    )
    priority = models.CharField(
        max_length=1, choices=PRIORITIES, verbose_name="issue priority"
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        related_name="related_project",
        verbose_name="related project",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="issue_author",
        blank=True,
        verbose_name="issue author",
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        related_name="issue_assignee",
        verbose_name="issue assignee",
    )
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="created on")
    comments_url = models.URLField(blank=True, verbose_name="comments url")

    def __str__(self):
        return (
            f"{self.name} | {self.tag}, {self.state}, {self.priority} | {self.project} "
        )


class Comment(models.Model):
    """
    Comment model allowing to create comments from issues.
    Comment is related to an Issue
    """

    objects = None
    name = models.CharField(max_length=100, verbose_name="comment name")
    description = models.TextField(verbose_name="comment description")
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        blank=True,
        related_name="comments",
        verbose_name="related issue",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        related_name="comment_author",
        verbose_name="comment author",
    )
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="created on")
    issue_url = models.URLField(blank=True, verbose_name="issue url")

    def __str__(self):
        return f"{self.name} | {self.issue}"
