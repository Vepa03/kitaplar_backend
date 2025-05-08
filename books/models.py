from django.db import models
from writers.models import Writer
from django.core.exceptions import ValidationError


class Book(models.Model):
    title_tm = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    image = models.ImageField(upload_to='books')
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name="books")
    file = models.FileField(upload_to='books', max_length=200)
    
    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        if not self.file.name.endswith('.pdf'):
            raise ValidationError("The file must be pdf")

    def __str__(self):
        return self.title_tm
