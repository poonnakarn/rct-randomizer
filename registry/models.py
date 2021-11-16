from django.db import models

class Patient(models.Model):
    hospital_number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital_number

class Sequence(models.Model):
    arm = models.CharField(max_length=10)
    patient = models.OneToOneField(Patient, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.arm
