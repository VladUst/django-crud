from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=120, unique=True)
    short_name = models.CharField(max_length=20)
    established = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.short_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    university = models.ForeignKey(to='University', on_delete=models.CASCADE)
    admission_year = models.CharField(max_length=10)

    def __str__(self):
        return self.name
