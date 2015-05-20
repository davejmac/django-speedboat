# Django Test App #
A project to test a reusable django app

## Settings ##


## Usage ##


## Testing ##
To test this app, clone this project, then from the root of the project, run `python testrunner.py`

If any database changes are made to the model, follow these steps before running the testrunner:


  1. `pip install -e .` to install the app.
  2. Set up migrations, run
     ```django-admin makemigrations testapp --settings=testapp.test_settings```
  3. Run migrations ```django-admin migrate testapp --settings=testapp.test_settings```
