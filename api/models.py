from django.db import models

# Create your models here.
class SatelliteInfo(models.Model):
    def __str__(self):
        return self.Name
    id=models.IntegerField(default=0)
    Name = models.CharField(max_length=200, primary_key=True, default='NA')
    OrbitType = models.CharField(max_length=200, blank=True, null=True)
    OrbitDay = models.FloatField(max_length=200, blank=True, null=True)
    OrbitalPeriod = models.FloatField(max_length=200, blank=True, null=True)
    altitude = models.FloatField(default=0)


class Sensor(models.Model):
    def __str__(self):
        return f'{self.SensorName} \t {self.SatelliteName}'

    SensorName = models.CharField(max_length=200, blank=True, null=True)
    SatelliteName = models.CharField(max_length=200, blank=True, null=True)
    SatelliteID=models.IntegerField(default=0)
    Swath = models.FloatField(default=0)
    TiltFore = models.FloatField(default=0)
    TiltAft = models.FloatField(default=0)
    application1= models.CharField(max_length=200, blank=True, null=True)
    application2= models.CharField(max_length=200, blank=True, null=True)
    application3= models.CharField(max_length=200, blank=True, null=True)
