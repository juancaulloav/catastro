from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    CustomUser, InformacionSuministro, Abastecimiento, InformacionPozos,
    InformacionAdministrativa, Bombas, Red, InformacionSuministroElectrico,
    InformacionDistribucionTarifa, InformacionAPR,MiAPR,
)
from .forms import (
    CustomUserCreationForm, InformacionSuministroForm, AbastecimientoForm, InformacionPozosForm,
    InformacionAdministrativaForm, BombasForm, RedForm, InformacionSuministroElectricoForm,
    InformacionDistribucionTarifaForm, InformacionAPRForm
)
from django.urls import reverse_lazy
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de inicio de sesión después de crear el usuario
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', {'form': form})
### Ingreso de usuarios ###

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

### desconectarse ####

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Define la página de redirección después del logout


@login_required
def home(request):
    informaciones_apr = InformacionAPR.objects.select_related(
        'informacion_administrativa',
        'informacion_abastecimiento',
        'informacion_distribucion_tarifa'
    ).all()

    return render(request, 'home.html', {'informaciones_apr': informaciones_apr})

###customuser ###
@login_required
def customuser_list(request):
    customusers = CustomUser.objects.all()
    return render(request, 'customuser/customuser_list.html', {'customusers': customusers})


def customuser_create(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customuser_list')
    return render(request, 'customuser/customuser_form.html', {'form': form})


@login_required
def customuser_update(request, pk):
    customuser = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserCreationForm(request.POST or None, instance=customuser)
    if form.is_valid():
        form.save()
        return redirect('customuser_list')
    return render(request, 'customuser/customuser_form.html', {'form': form})


@login_required
def customuser_delete(request, pk):
    customuser = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        customuser.delete()
        return redirect('customuser_list')
    return render(request, 'customuser/customuser_confirm_delete.html', {'customuser': customuser})

#### informacionsuministro ###
@login_required
def informacionsuministro_list(request):
    informaciones_suministro = InformacionSuministro.objects.all()
    return render(request, 'informacionsuministro/informacionsuministro_list.html', {'informaciones_suministro': informaciones_suministro})



@login_required
def informacionsuministro_create(request):
    form = InformacionSuministroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('informacionsuministro_list')
    return render(request, 'informacionsuministro/informacionsuministro_form.html', {'form': form})


@login_required
def informacionsuministro_update(request, pk):
    informacionsuministro = get_object_or_404(InformacionSuministro, pk=pk)
    form = InformacionSuministroForm(
        request.POST or None, instance=informacionsuministro)
    if form.is_valid():
        form.save()
        return redirect('informacionsuministro_list')
    return render(request, 'informacionsuministro/informacionsuministro_form.html', {'form': form})


@login_required
def informacionsuministro_delete(request, pk):
    informacionsuministro = get_object_or_404(InformacionSuministro, pk=pk)
    if request.method == 'POST':
        informacionsuministro.delete()
        return redirect('informacionsuministro_list')
    return render(request, 'informacionsuministro/informacionsuministro_confirm_delete.html', {'informacionsuministro': informacionsuministro})



    ### VIEWS DE ABASTECIMIENTO ###


@login_required
def abastecimiento_list(request):
    abastecimientos = Abastecimiento.objects.all()
    return render(request, 'abastecimiento/abastecimiento_list.html', {'abastecimientos': abastecimientos})


@login_required
def abastecimiento_create(request):
    form = AbastecimientoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('abastecimiento_list')
    return render(request, 'abastecimiento/abastecimiento_form.html', {'form': form})


@login_required
def abastecimiento_update(request, pk):
    abastecimiento = get_object_or_404(Abastecimiento, pk=pk)
    form = AbastecimientoForm(request.POST or None, instance=abastecimiento)
    if form.is_valid():
        form.save()
        return redirect('abastecimiento_list')
    return render(request, 'abastecimiento/abastecimiento_form.html', {'form': form})


@login_required
def abastecimiento_delete(request, pk):
    abastecimiento = get_object_or_404(Abastecimiento, pk=pk)
    if request.method == 'POST':
        abastecimiento.delete()
        return redirect('abastecimiento_list')
    return render(request, 'abastecimiento/abastecimiento_confirm_delete.html', {'abastecimiento': abastecimiento})


@login_required
def informacionpozos_list(request):
    informacionpozos = InformacionPozos.objects.all()
    return render(request, 'informacionpozos/informacionpozos_list.html', {'informacionpozos': informacionpozos})


@login_required
def informacionpozos_create(request):
    form = InformacionPozosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('informacionpozos_list')
    return render(request, 'informacionpozos/informacionpozos_form.html', {'form': form})


@login_required
def informacionpozos_update(request, pk):
    informacionpozos = get_object_or_404(InformacionPozos, pk=pk)
    form = InformacionPozosForm(
        request.POST or None, instance=informacionpozos)
    if form.is_valid():
        form.save()
        return redirect('informacionpozos_list')
    return render(request, 'informacionpozos/informacionpozos_form.html', {'form': form})


@login_required
def informacionpozos_delete(request, pk):
    informacionpozos = get_object_or_404(InformacionPozos, pk=pk)
    if request.method == 'POST':
        informacionpozos.delete()
        return redirect('informacionpozos_list')
    return render(request, 'informacionpozos/informacionpozos_confirm_delete.html', {'informacionpozos': informacionpozos})

### iNFORMACION ADMINISTRATIVA ###
@login_required
def informacionadministrativa_list(request):
    informacionesadministrativas = InformacionAdministrativa.objects.all()
    return render(request, 'informacionadministrativa/informacionadministrativa_list.html', {'informacionesadministrativas': informacionesadministrativas})


@login_required
def informacionadministrativa_create(request):
    form = InformacionAdministrativaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('informacionadministrativa_list')
    return render(request, 'informacionadministrativa/informacionadministrativa_form.html', {'form': form})


@login_required
def informacionadministrativa_update(request, pk):
    informacionadministrativa = get_object_or_404(
        InformacionAdministrativa, pk=pk)
    form = InformacionAdministrativaForm(
        request.POST or None, instance=informacionadministrativa)
    if form.is_valid():
        form.save()
        return redirect('informacionadministrativa_list')
    return render(request, 'informacionadministrativa/informacionadministrativa_form.html', {'form': form})


@login_required
def informacionadministrativa_delete(request, pk):
    informacionadministrativa = get_object_or_404(
        InformacionAdministrativa, pk=pk)
    if request.method == 'POST':
        informacionadministrativa.delete()
        return redirect('informacionadministrativa_list')
    return render(request, 'informacionadministrativa/informacionadministrativa_confirm_delete.html', {'informacionadministrativa': informacionadministrativa})


@login_required
def bombas_list(request):
    bombas = Bombas.objects.all()
    return render(request, 'bombas/bombas_list.html', {'bombas': bombas})


@login_required
def bombas_create(request):
    form = BombasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bombas_list')
    return render(request, 'bombas/bombas_form.html', {'form': form})


@login_required
def bombas_update(request, pk):
    bomba = get_object_or_404(Bombas, pk=pk)
    form = BombasForm(request.POST or None, instance=bomba)
    if form.is_valid():
        form.save()
        return redirect('bombas_list')
    return render(request, 'bombas/bombas_form.html', {'form': form})


@login_required
def bombas_delete(request, pk):
    bomba = get_object_or_404(Bombas, pk=pk)
    if request.method == 'POST':
        bomba.delete()
        return redirect('bombas_list')
    return render(request, 'bombas/bombas_confirm_delete.html', {'bomba': bomba})


@login_required
def red_list(request):
    redes = Red.objects.all()
    return render(request, 'red/red_list.html', {'redes': redes})


@login_required
def red_create(request):
    form = RedForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('red_list')
    return render(request, 'red/red_form.html', {'form': form})


@login_required
def red_update(request, pk):
    red = get_object_or_404(Red, pk=pk)
    form = RedForm(request.POST or None, instance=red)
    if form.is_valid():
        form.save()
        return redirect('red_list')
    return render(request, 'red/red_form.html', {'form': form})


@login_required
def red_delete(request, pk):
    red = get_object_or_404(Red, pk=pk)
    if request.method == 'POST':
        red.delete()
        return redirect('red_list')
    return render(request, 'red/red_confirm_delete.html', {'red': red})


@login_required
def informacionsuministroelectrico_list(request):
    informacionessuministroelectrico = InformacionSuministroElectrico.objects.all()
    return render(request, 'informacionsuministroelectrico/informacionsuministroelectrico_list.html', {'informacionessuministroelectrico': informacionessuministroelectrico})


@login_required
def informacionsuministroelectrico_create(request):
    form = InformacionSuministroElectricoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('informacionsuministroelectrico_list')
    return render(request, 'informacionsuministroelectrico/informacionsuministroelectrico_form.html', {'form': form})


@login_required
def informacionsuministroelectrico_update(request, pk):
    informacionsuministroelectrico = get_object_or_404(
        InformacionSuministroElectrico, pk=pk)
    form = InformacionSuministroElectricoForm(
        request.POST or None, instance=informacionsuministroelectrico)
    if form.is_valid():
        form.save()
        return redirect('informacionsuministroelectrico_list')
    return render(request, 'informacionsuministroelectrico/informacionsuministroelectrico_form.html', {'form': form})


@login_required
def informacionsuministroelectrico_delete(request, pk):
    informacionsuministroelectrico = get_object_or_404(
        InformacionSuministroElectrico, pk=pk)
    if request.method == 'POST':
        informacionsuministroelectrico.delete()
        return redirect('informacionsuministroelectrico_list')
    return render(request, 'informacionsuministroelectrico/informacionsuministroelectrico_confirm_delete.html', {'informacionsuministroelectrico': informacionsuministroelectrico})

### informacion distribucion tarifa ###
@login_required
def informaciondistribuciontarifa_list(request):
    informacionesdistribuciontarifa = InformacionDistribucionTarifa.objects.all()
    return render(request, 'informaciondistribuciontarifa/informaciondistribuciontarifa_list.html', {'informacionesdistribuciontarifa': informacionesdistribuciontarifa})


@login_required
def informaciondistribuciontarifa_create(request):
    form = InformacionDistribucionTarifaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('informaciondistribuciontarifa_list')
    return render(request, 'informaciondistribuciontarifa/informaciondistribuciontarifa_form.html', {'form': form})


@login_required
def informaciondistribuciontarifa_update(request, pk):
    informaciondistribuciontarifa = get_object_or_404(
        InformacionDistribucionTarifa, pk=pk)
    form = InformacionDistribucionTarifaForm(
        request.POST or None, instance=informaciondistribuciontarifa)
    if form.is_valid():
        form.save()
        return redirect('informaciondistribuciontarifa_list')
    return render(request, 'informaciondistribuciontarifa/informaciondistribuciontarifa_form.html', {'form': form})


@login_required
def informaciondistribuciontarifa_delete(request, pk):
    informaciondistribuciontarifa = get_object_or_404(
        InformacionDistribucionTarifa, pk=pk)
    if request.method == 'POST':
        informaciondistribuciontarifa.delete()
        return redirect('informaciondistribuciontarifa_list')
    return render(request, 'informaciondistribuciontarifa/informaciondistribuciontarifa_confirm_delete.html', {'informaciondistribuciontarifa': informaciondistribuciontarifa})

### InformacionAPR ###
@login_required
def informacionapr_list(request):
    informacionapr = InformacionAPR.objects.filter(
        informacion_administrativa__usuario=request.user)
    return render(request, 'informacionapr/informacionapr_list.html', {'informacionapr': informacionapr})


@login_required
def informacionapr_create(request):
    form = InformacionAPRForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('informacionapr_list')
    return render(request, 'informacionapr/informacionapr_form.html', {'form': form})


@login_required
def informacionapr_update(request, pk):
    informacionapr = get_object_or_404(InformacionAPR, pk=pk)
    form = InformacionAPRForm(request.POST or None, instance=informacionapr)
    if form.is_valid():
        form.save()
        return redirect('informacionapr_list')
    return render(request, 'informacionapr/informacionapr_form.html', {'form': form})


@login_required
def informacionapr_delete(request, pk):
    informacionapr = get_object_or_404(InformacionAPR, pk=pk)
    if request.method == 'POST':
        informacionapr.delete()
        return redirect('informacionapr_list')
    return render(request, 'informacionapr/informacionapr_confirm_delete.html', {'informacionapr': informacionapr})


# Lista de todos los MiAPR
class MiAPRListView(LoginRequiredMixin, ListView):
    model = MiAPR
    template_name = 'miapr/miapr_list.html'
    context_object_name = 'miapr_list'
    paginate_by = 10

# Detalles de un MiAPR específico
class MiAPRDetailView(LoginRequiredMixin, DetailView):
    model = MiAPR
    template_name = 'miapr/miapr_detail.html'
    context_object_name = 'miapr'

# Crear un nuevo MiAPR
class MiAPRCreateView(LoginRequiredMixin, CreateView):
    model = MiAPR
    template_name = 'miapr/miapr_create.html'
    fields = ['informacion_apr', 'usuario']
    success_url = reverse_lazy('miapr-list')

# Actualizar un MiAPR existente
class MiAPRUpdateView(LoginRequiredMixin, UpdateView):
    model = MiAPR
    template_name = 'miapr/miapr_update.html'
    fields = ['informacion_apr', 'usuario']
    success_url = reverse_lazy('miapr-list')

# Eliminar un MiAPR existente
class MiAPRDeleteView(LoginRequiredMixin, DeleteView):
    model = MiAPR
    template_name = 'miapr/miapr_delete.html'
    success_url = reverse_lazy('miapr-list')
