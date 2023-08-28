from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    abreviacion = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.nombre

class Fuerza(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre

class Regimiento(models.Model):
    nombre = models.CharField(max_length=100)
    fuerza = models.ForeignKey(Fuerza, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre