from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.


class User(auth_models.AbstractBaseUser):
    pass


class Profile(models.Model):
    pass
