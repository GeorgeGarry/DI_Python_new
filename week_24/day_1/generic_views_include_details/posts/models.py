from django.db import models

# Create your models here.
# Create your models here.
from datetime import datetime
from users.models import Person


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=50)
    released_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    # If you delete a person, his posts will be also deleted

    def __str__(self):
        return f'{self.title}'
