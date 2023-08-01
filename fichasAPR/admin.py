from django.contrib import admin
from .models import InformacionAPR, Bombas, Abastecimiento, CustomUser, InformacionAdministrativa, InformacionDistribucionTarifa, InformacionPozos, InformacionSuministro, InformacionSuministroElectrico,Red


# Register your models here.

admin.site.register(InformacionAPR)
admin.site.register(Bombas)
admin.site.register(Red)
admin.site.register(Abastecimiento)
admin.site.register(CustomUser)
admin.site.register(InformacionAdministrativa)
admin.site.register(InformacionDistribucionTarifa)
admin.site.register(InformacionPozos)
admin.site.register(InformacionSuministro)
admin.site.register(InformacionSuministroElectrico)
