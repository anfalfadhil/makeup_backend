from django.apps import AppConfig


class MakeupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'makeup'

    def ready(self):
        from . import signals

class UsersConfig(AppConfig):
    name='users'

    def ready(self):
        import users.signals