from django.contrib import admin
#from .models import Reserva
from .models import Apartamento
from .models import Maquina
from .models import Morador

# Register your models here.

#admin.site.register(Reserva)

admin.site.register(Apartamento)
admin.site.register(Morador)
admin.site.register(Maquina)
