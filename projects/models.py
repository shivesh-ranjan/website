from sys import maxsize
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Project(models.Model):
    Sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=70)
    Tag = models.CharField(max_length=30)
    Body = RichTextField()
    TimeStamp = models.DateTimeField(blank=True)
    Source = models.CharField(max_length=300)
    Deploy = models.CharField(max_length=300)
    Slug = models.CharField(max_length=20)
    def __str__(self):
        return self.Slug+ ". " + self.Title