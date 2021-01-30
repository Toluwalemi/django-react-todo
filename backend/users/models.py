from django.contrib.auth.models import AbstractUser


# Create your models here.

class NewUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
