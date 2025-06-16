from django.db import models

class User(models.Model):
    """
    Represent an user
    """
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100) # Too long because of encryption

    def __str__(self):
        """
        Return the user name
        """
        return self.name

class Task(models.Model):
    """
    Represent a task
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    add_date = models.DateTimeField('addition_date')
    deadline = models.DateTimeField()
    done_date = models.DateTimeField(null=True)

    def __str__(self):
        """
        Return the task's title
        """
        return self.title
