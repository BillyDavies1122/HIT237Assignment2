from django.db import models
"""
One publisher has many games
one game can have one publisher

one game can have one set of system systemRequirements
one system requirements can have one game


"""
# Create your models here.
class publisher(models.Model):
    publisherName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    dateFounded = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        """returns a string representation of the model"""
        return str(self.publisherName)

class systemRequirements(models.Model):
    memoryNeeded = models.CharField(max_length=100)
    miniumumDiskSpace = models.CharField(max_length=100)
    gpuRequired = models.CharField(max_length=50)
    def __str__(self):
        """returns a string representation of the model"""
        return str(self.memoryNeeded)

class game(models.Model):
     gameName = models.CharField(max_length=100)
     description = models.CharField(max_length=1000)
     price = models.DecimalField(max_digits=5,decimal_places=2)
     releaseDate = models.DateField(auto_now=False, auto_now_add=False)
     publisher = models.ForeignKey(publisher,default='')
     systemRequirements = models.ForeignKey(systemRequirements,default='')

     def __str__(self):
         """returns a string representation of the model"""
         return str(self.gameName)
