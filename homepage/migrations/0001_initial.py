# Generated by Django 5.1.5 on 2025-02-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banners",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("image_alt", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SEO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="The title of the page for SEO.", max_length=255
                    ),
                ),
                ("logo", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "description",
                    models.TextField(help_text="The meta description of the page."),
                ),
                (
                    "keywords",
                    models.CharField(
                        help_text="Comma-separated keywords for SEO.", max_length=255
                    ),
                ),
                (
                    "canonical_url",
                    models.URLField(
                        help_text="Canonical URL to avoid duplicate content issues."
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("youtube_link", models.URLField(blank=True, null=True)),
                ("facebook_link", models.URLField(blank=True, null=True)),
                ("instagram_link", models.URLField(blank=True, null=True)),
                (
                    "scripts",
                    models.TextField(
                        blank=True,
                        help_text="Custom scripts (e.g., tracking, analytics) to embed in the page.",
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
