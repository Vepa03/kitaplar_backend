from django.db import models


class Writer(models.Model):
    username_tm = models.CharField(max_length=150)
    username_en = models.CharField(max_length=150)
    image = models.ImageField(upload_to='writers')

    def __str__(self):
        return self.username_tm
    