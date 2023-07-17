import os


def get_my_postgres_passwd():
    variable_value = os.environ.get('PURPLE_UNICORN')
    return variable_value
