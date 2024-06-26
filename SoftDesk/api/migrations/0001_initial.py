# Generated by Django 4.2.7 on 2024-05-14 16:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(verbose_name='age')),
                ('contact_consent', models.BooleanField(default=False, verbose_name='contact consent')),
                ('data_share_consent', models.BooleanField(default=False, verbose_name='data share consent')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name of project')),
                ('description', models.TextField(verbose_name='project description')),
                ('type', models.CharField(choices=[('B', 'Back-end'), ('F', 'Front-end'), ('I', 'iOS'), ('A', 'Android')], max_length=1, verbose_name='project type')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('issues_url', models.URLField(blank=True, verbose_name='issues url')),
                ('contributors_url', models.URLField(blank=True, verbose_name='contributors url')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL, verbose_name='project author')),
                ('contributors', models.ManyToManyField(blank=True, related_name='project_contributors', to=settings.AUTH_USER_MODEL, verbose_name='project contributors')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name of issue')),
                ('description', models.TextField(verbose_name='issue description')),
                ('tag', models.CharField(choices=[('B', 'Bug'), ('F', 'Feature'), ('T', 'Task')], max_length=2, verbose_name='issue tag')),
                ('state', models.CharField(choices=[('T', 'ToDo'), ('I', 'In Progress'), ('C', 'Completed')], default='T', max_length=2, verbose_name='issue state')),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1, verbose_name='issue priority')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('comments_url', models.URLField(blank=True, verbose_name='comments url')),
                ('assignee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL, verbose_name='issue assignee')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL, verbose_name='issue author')),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_project', to='api.project', verbose_name='related project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='comment name')),
                ('description', models.TextField(verbose_name='comment description')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('issue_url', models.URLField(blank=True, verbose_name='issue url')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='comment author')),
                ('issue', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.issue', verbose_name='related issue')),
            ],
        ),
    ]
