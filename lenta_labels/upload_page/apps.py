from django.apps import AppConfig


class UploadPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload_page'

    def ready(self):
        import upload_page.signals
