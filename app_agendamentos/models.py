from django.db import models

class Registro(models.Model):
    id          = models.AutoField(primary_key=True)
    nome        = models.TextField(max_length=255)
    endereco    = models.TextField(max_length=255)
    email       = models.TextField(max_length=155)
    telefone    = models.TextField(max_length=55)
    data_coleta = models.DateField(null = True)
    hora_coleta = models.TimeField(null = True)