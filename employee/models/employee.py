from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255, null=False)
    department = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.__dict__)

    def __cmp__(self, other):
        return self.__dict__ == other.__dict__
