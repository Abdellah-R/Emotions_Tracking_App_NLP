from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emotiontracking.settings")


if __name__ == "__main__":
    db_settings = settings.DATABASES['default']
    print("Database Engine:", db_settings['ENGINE'])
    print("Database Name:", db_settings['NAME'])
    print("Database User:", db_settings['USER'])
    print("Database Password:", db_settings['PASSWORD'])
    print("Database Host:", db_settings['HOST'])
    print("Database Port:", db_settings['PORT'])
