from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=264)

    def __str__(self):
        return str(self.first_name)+' '+str(self.last_name)
