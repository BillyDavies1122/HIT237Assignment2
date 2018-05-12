from django.db import models

# Create your models here.
class Game(models.Model):
     gameName = models.CharField(max_length=100) #PRIMARY KEY
     description = models.CharField(max_length=1000)
     price = models.DecimalField(max_digits=5,decimal_places=2)
     releaseDate = models.DateField(auto_now=False, auto_now_add=False)
     publisherName = models.CharField(max_length=100) #FOREIGN KEY

     def __str__(self):
         """returns a string representation of the model"""
         return str("""Name:%s \n
                        Description:%s \n
                        Price:$%s \n
                        Release Date:%s \n
                        Published By:%s \n""" %(self.gameName,self.description,self.price,
                                     self.releaseDate,self.publisherName))


class Publisher(models.Model):
    publisherName = models.CharField(max_length=100)#PRIMARY KEY
    Location = models.CharField(max_length=100)
    dateFounded = models.DateField(auto_now=False, auto_now_add=False)
    gameName = models.CharField(max_length=100)#FOREIGN KEY

    def __str__(self):
        """returns a string representation of the model"""
        return str(""" Game Name:%s \n
                       Publisher Name:%s \n
                       Location:%s \n
                       Date Founded: %s""" %(self.gameName,self.publisherName,self.Location,
                                            self.dateFounded))


class systemRequirements(models.Model):
    gameName = models.CharField(max_length=100)#FOREIGN KEY
    memoryNeeded = models.CharField(max_length=100)
    miniumumDiskSpace = models.CharField(max_length=100)
    gpuRequired = models.CharField(max_length=50)

    def __str__(self):
        """returns a string representation of the model"""
        return str(""" Name:%s \n
                       Minimum memory required:%s \n
                       miniumum disk space required:$%s \n
                       Recommended GPU:%s""" %(self.gameName,self.memoryNeeded,
                                                  self.miniumumDiskSpace,self.gpuRequired))
