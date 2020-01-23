from . import settings

DATABASES = {
    "default":{
        "ENGINE":"django.db.backends.sqlite3",
        "NAME":":memory:",
    }
}

EMAIL_BACKEND = 'django.core.email.backends.locmen.EmailBackend'