from django.apps import AppConfig


class GeekhavenBlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "geekhaven_blog"
    # custom title shown on the admin panel
    verbose_name = "GeekHaven Blog"
