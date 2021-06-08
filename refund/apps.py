from django.apps import AppConfig


class RefundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'refund'

    def ready(self):
        from refund import signals
