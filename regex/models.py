from django.db import models

class Regex(models.Model):
    name = models.CharField(max_length=20)
    regex_search = models.CharField(max_length=400)
    regex_change = models.CharField(max_length=400)