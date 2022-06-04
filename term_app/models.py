from django.db import models


class Test(models.Model):
    question = models.CharField(max_length=5000)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)

    def __str__(self):
        return self.question