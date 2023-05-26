from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    first_name = models.CharField('First name', max_length=200)
    last_name = models.CharField('Last name', max_length=200)
    email = models.CharField('Email', max_length=200)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Role(models.Model):
    family_choices = [
        ("Data", "Data"),
        ("IT Operations", "IT Operations"),
        ("Product and delivery", "Product and delivery"),
        ("Quality assurance testing (QAT)", "Quality assurance testing (QAT)"),
        ("Technical", "Technical"),
        ("User-centred design", "User-centred design"),
    ]
    title = models.CharField(max_length=200)
    job_family = models.CharField(max_length=200, choices=family_choices)
    level = models.CharField(max_length=200, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

