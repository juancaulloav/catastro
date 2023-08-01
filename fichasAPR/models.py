from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    rol_usuario = models.CharField(max_length=50)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username

class InformacionSuministro(models.Model):
    nombre_plantilla = models.CharField(max_length=100, blank=True)
    tipo_suministro = models.CharField(max_length=50, blank=True)
    numero_tramo = models.IntegerField(null=True, blank=True)
    valor_tramos = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return self.nombre_plantilla

class Abastecimiento(models.Model):
    nombre_plantilla = models.CharField(max_length=100, blank=True)
    frecuencia_camion_aljibe = models.CharField(max_length=50, blank=True)
    volumen_camion_aljibe = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    informacion_general = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_plantilla

class InformacionPozos(models.Model):
    plantilla_informacion_pozos = models.CharField(max_length=100, blank=True)
    tipos_pozos = models.CharField(max_length=50, blank=True)
    profundidad_pozos = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    diametro_pozo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    materialidad_pozo = models.CharField(max_length=50, blank=True)
    causalidad_pozo = models.CharField(max_length=50, blank=True)
    estado_pozo = models.CharField(max_length=50, blank=True)
    informacion_abastecimiento = models.ForeignKey('Abastecimiento', on_delete=models.CASCADE)
    informacion_suministro = models.ForeignKey('InformacionSuministro', on_delete=models.CASCADE)

    def __str__(self):
        return self.plantilla_informacion_pozos

class InformacionAdministrativa(models.Model):
    plantilla_informacion_administrativa = models.CharField(max_length=100)
    numero_arranques = models.IntegerField(null=True, blank=True)
    estado_general = models.CharField(max_length=50, blank=True)
    estado_regulacion = models.CharField(max_length=50, blank=True)
    estado_distribucion = models.CharField(max_length=50, blank=True)
    informacion_administrativa = models.TextField()
    usuario = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.plantilla_informacion_administrativa

class Bombas(models.Model):
    nombre_bomba = models.CharField(max_length=100)
    potencia_hp = models.IntegerField(null=True, blank=True)
    marca = models.CharField(max_length=50, blank=True)
    tipo = models.CharField(max_length=50, blank=True)
    q_medida = models.CharField(max_length=50, blank=True)
    sistema = models.CharField(max_length=50, blank=True)
    volumen = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    informacion_general = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_bomba

class Red(models.Model):
    nombre_red = models.CharField(max_length=100)
    longitud_red = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    densidad_red = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    material = models.CharField(max_length=50, blank=True)
    diametro_sistema_distribucion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_red

class InformacionSuministroElectrico(models.Model):
    nombre_informacion_suministro = models.CharField(max_length=100)
    paneles_solares = models.BooleanField()
    generador = models.BooleanField()
    tipo_energia = models.CharField(max_length=50, blank=True)
    material = models.CharField(max_length=50, blank=True)
    informacion_red_distribucion = models.ForeignKey('Red', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_informacion_suministro

class InformacionDistribucionTarifa(models.Model):
    nombre_plantilla = models.CharField(max_length=100)
    planos = models.FileField(upload_to='planos/', blank=True)
    pruebas_bombeo = models.FileField(upload_to='pruebas_bombeo/', blank=True)
    diseño_tratamiento = models.FileField(upload_to='diseño_tratamiento/', blank=True)
    muestra_nch409_1 = models.FileField(upload_to='muestra_nch409_1/', blank=True, null=True)
    muestra_nch409_2 = models.FileField(upload_to='muestra_nch409_2/', blank=True, null=True)
    bombas = models.ForeignKey('Bombas', on_delete=models.CASCADE)
    red = models.ForeignKey('Red', on_delete=models.CASCADE)
    informacion_extra = models.TextField()

    def __str__(self):
        return self.nombre_plantilla

class InformacionAPR(models.Model):
    nombre_comite = models.CharField(max_length=100, blank=True)
    sector_apr = models.CharField(max_length=50, blank=True)
    comuna_apr = models.CharField(max_length=50, blank=True)
    informacion_administrativa = models.ForeignKey('InformacionAdministrativa', on_delete=models.CASCADE)
    informacion_abastecimiento = models.ForeignKey('Abastecimiento', on_delete=models.CASCADE)
    informacion_distribucion_tarifa = models.ForeignKey('InformacionDistribucionTarifa', on_delete=models.CASCADE)
    nombre_presidente = models.CharField(max_length=100)
    telefono_presidente = models.CharField(max_length=20, blank=True)
    correo_presidente = models.EmailField(blank=True)
    nombre_tesorero = models.CharField(max_length=100, blank=True)
    telefono_tesorero = models.CharField(max_length=20, blank=True)
    correo_tesorero = models.EmailField(blank=True)
    nombre_secretario = models.CharField(max_length=100, blank=True)
    telefono_secretario = models.CharField(max_length=20, blank=True)
    correo_secretario = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre_comite

class MiAPR(models.Model):
    informacion_apr = models.ForeignKey('InformacionAPR', on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"APR: {self.informacion_apr} - Usuario: {self.usuario}"