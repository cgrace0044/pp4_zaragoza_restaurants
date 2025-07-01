from django.apps import AppConfig


class LettersFromZaragozaConfig(AppConfig):
    """
    Provides primary key type for restaurant app
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "letters_from_zaragoza"
