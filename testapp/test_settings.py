DEBUG=True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}
}

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'testapp',
]

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ROOT_URLCONF = 'testapp.urls'

SECRET_KEY = 'test-key'
