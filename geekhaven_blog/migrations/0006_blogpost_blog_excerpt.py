# Generated by Django 4.2.10 on 2024-03-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geekhaven_blog", "0005_rename_blog_header_blogpost_blog_heading_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="blog_excerpt",
            field=models.TextField(blank=True, default=""),
        ),
    ]
