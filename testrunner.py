import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
django.setup()

# for running via setup
def run_tests():
    runner_class = get_runner(settings)
    test_runner = runner_class(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['tests'])
    sys.exit(failures)


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))
