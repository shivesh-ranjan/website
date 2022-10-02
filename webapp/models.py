from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=13)
    Email = models.CharField(max_length=100)
    Issue = models.TextField()
    TimeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.Name + " - " + self.Email

class MailList(models.Model):
    Sno = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=100)
    def __str__(self):
        return self.Email