from django.db import models


class Regex(models.Model):
    """ 正規表現 """
    name = models.CharField(max_length=20)
    regex_search = models.CharField(max_length=400)
    regex_change = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.name