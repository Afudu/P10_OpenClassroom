# Generated by Django 4.2.7 on 2024-11-10 17:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_remove_project_contributors_url_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="issue",
            name="comments_url",
        ),
    ]