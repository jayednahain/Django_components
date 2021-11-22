from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals'

    def ready(self):
        from signals.My_signals import authentication_signals
        from signals.My_signals import model_signals
        from signals.My_signals import request_signals
