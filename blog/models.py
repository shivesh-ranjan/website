from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=50)
    Body = RichTextField()
    TimeStamp = models.DateTimeField(blank=True)
    Category = models.CharField(max_length=20)
    Slug = models.CharField(max_length=130)

    def __str__(self):
        return self.Slug+ ". " + self.Title + " by " + self.Author