from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import (
    CustomUser, InformacionSuministro, Abastecimiento, InformacionPozos,
    InformacionAdministrativa, Bombas, Red, InformacionSuministroElectrico,
    InformacionDistribucionTarifa, InformacionAPR
)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'nombre', 'rut',
                  'correo', 'telefono', 'rol_usuario')


class InformacionSuministroForm(forms.ModelForm):
    class Meta:
        model = InformacionSuministro
        fields = '__all__'


class AbastecimientoForm(forms.ModelForm):
    class Meta:
        model = Abastecimiento
        fields = '__all__'


class InformacionPozosForm(forms.ModelForm):
    class Meta:
        model = InformacionPozos
        fields = '__all__'


class InformacionAdministrativaForm(forms.ModelForm):
    class Meta:
        model = InformacionAdministrativa
        fields = '__all__'


class BombasForm(forms.ModelForm):
    class Meta:
        model = Bombas
        fields = '__all__'


class RedForm(forms.ModelForm):
    class Meta:
        model = Red
        fields = '__all__'


class InformacionSuministroElectricoForm(forms.ModelForm):
    class Meta:
        model = InformacionSuministroElectrico
        fields = '__all__'


class InformacionDistribucionTarifaForm(forms.ModelForm):
    class Meta:
        model = InformacionDistribucionTarifa
        fields = '__all__'


class InformacionAPRForm(forms.ModelForm):
    class Meta:
        model = InformacionAPR
        fields = '__all__'
