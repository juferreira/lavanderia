from django.db import models
from django.utils import timezone
# Create your models here.

class Apartamento(models.Model):
    unidade = models.IntegerField(primary_key=True)
    morador = models.ForeignKey(Morador)

    def __str__(self):
           return str(self.unidade)

class Morador(models.Model):
    apartamento = models.ForeignKey(Apartamento)
    nome = models.CharField(max_length=200)
    auto_increment_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name_plural = "Moradores"

    def __str__(self):
        return self.nome
  

class Maquina(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    def __str__(self):
        return str(self.numero)


class Reserva(models.Model):
    data_uso_maquina = models.DateTimeField(blank=True, null=False, primary_key=True)
    apartamento_responsavel = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    data_criacao_reserva = models.DateTimeField(
            default=timezone.now)
    class meta:
        unique_together = (('data_uso_maquina','apartamento_responsavel','maquina'),) 
