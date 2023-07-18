import os


def get_my_postgres_user():
    variable_value = os.environ.get('GRAY_GOOSE')
    return variable_value


def get_my_postgres_passwd():
    variable_value = os.environ.get('PURPLE_UNICORN')
    return variable_value


def get_my_postgres_hostname():
    variable_value = os.environ.get('PINK_FLAMINGO')
    return variable_value


def get_my_postgres_port():
    variable_value = os.environ.get('GREEN_FROG')
    return variable_value


def get_my_secret_key():
    variable_value = os.environ.get('BROWN_DONKEY')
    return variable_value


