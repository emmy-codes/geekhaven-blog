from django.apps import AppConfig


class GeekhavenBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geekhaven_blog'
    verbose_name = 'GeekHaven Blog'  # custom title shown on the admin panel
