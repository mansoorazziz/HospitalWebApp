from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)
    evening = models.BooleanField(default=False)
    night = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class LabTest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
