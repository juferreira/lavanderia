from django.db import models
from django.utils import timezone
# Create your models here.


class Apartamento(models.Model):
    unidade = models.IntegerField(primary_key=True)
 
class Maquina(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    numero = models.IntegerField()

class Reserva(models.Model):
    data_uso_maquina = models.DateTimeField(blank=True, null=False, primary_key=True)
    apartamento_responsavel = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    data_criacao_reserva = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return 'Unidade: ' + str(self.apartamento_responsavel.unidade) + ' - Data da utilização: ' + self.data_uso_maquina.strftime("%Y-%m-%d %H:%M:%S") 



    
    
        

