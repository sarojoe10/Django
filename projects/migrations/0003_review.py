# Generated by Django 5.1.3 on 2024-11-14 10:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_alter_project_demo_link_alter_project_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("body", models.TextField(blank=True, null=True)),
                (
                    "value",
                    models.CharField(
                        choices=[("up", "up"), ("down", "down")], max_length=100
                    ),
                ),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]
