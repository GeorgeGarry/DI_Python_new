from datetime import date

from django.core.validators import MaxValueValidator

# Create your models here.
from django.db import models  # import the models package. This line is already existing as soon as we use 'startapp'


# Must inherit from Django Model class
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return f'''
first_name={self.first_name}
last_name={self.last_name}
birth_date={self.birth_date}
has_pet={self.has_pet}
number_pet={self.number_pet}
'''

    def person_age(self):
        current_date = date.today()
        current_age = current_date.year - self.birth_date.year
        return current_age
