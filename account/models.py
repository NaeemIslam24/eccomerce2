from django.db import models

# Create your models here.

class NorulIslam(models.Model):

    son1 = models.CharField(max_length=50)
    son2 = models.CharField(max_length=50)
    son3 = models.CharField(max_length=50)
    son4 = models.CharField(max_length=50)

    def __str__(self):
        return self.son1

    def first_two(self):
        
        two = self.firuzaislam_set.all()
        print('--------------------')
        print(two)
        return two
    

class FiruzaIslam(models.Model):

    daughter1 = models.CharField(max_length=50)
    daughter2 = models.CharField(max_length=50)
    daughter3 = models.CharField(max_length=50)
    daughter4 = models.CharField(max_length=50)
    n = models.ForeignKey(NorulIslam, on_delete=models.CASCADE)
 

    def __str__(self):
        return self.daughter1
