from django.db import models


# Create your models here.
class Players(models.Model):
    first_name = models.CharField(max_length=20,unique=True)
    last_name = models.CharField(max_length=20,unique=True)
    position = models.CharField(max_length=40)
    age = models.SmallIntegerField()
    previous_club = models.CharField(max_length=30,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Player'
        
