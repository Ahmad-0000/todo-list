from django.db import models

class User(models.Model):
    """
    Represent an user
    """
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        """
        Return the user name
        """
        return self.name
