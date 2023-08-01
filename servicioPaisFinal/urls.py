from django.contrib import admin
from django.urls import path, include
from fichasAPR.views import (
    CustomLoginView,
    customuser_list, customuser_create, customuser_update, customuser_delete,
    informacionsuministro_list, informacionsuministro_create, informacionsuministro_update, informacionsuministro_delete,
    abastecimiento_list, abastecimiento_create, abastecimiento_update, abastecimiento_delete,
    informacionpozos_list, informacionpozos_create, informacionpozos_update, informacionpozos_delete,
    informacionadministrativa_list, informacionadministrativa_create, informacionadministrativa_update, informacionadministrativa_delete,
    bombas_list, bombas_create, bombas_update, bombas_delete,
    red_list, red_create, red_update, red_delete,
    informacionsuministroelectrico_list, informacionsuministroelectrico_create, informacionsuministroelectrico_update, informacionsuministroelectrico_delete,
    informaciondistribuciontarifa_list, informaciondistribuciontarifa_create, informaciondistribuciontarifa_update, informaciondistribuciontarifa_delete,
    informacionapr_list, informacionapr_create, informacionapr_update, informacionapr_delete, home, CustomLogoutView, MiAPRListView, MiAPRDetailView, MiAPRCreateView, MiAPRUpdateView, MiAPRDeleteView,create_user)

urlpatterns = [
    # Rutas de Django Admin
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create_user/', create_user, name='create_user'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('customuser/', customuser_list, name='customuser_list'),
    path('customuser/create/', customuser_create, name='customuser_create'),
    path('customuser/update/<int:pk>/',
         customuser_update, name='customuser_update'),
    path('customuser/delete/<int:pk>/',
         customuser_delete, name='customuser_delete'),

    ### informacion suministro ###
    path('informacionsuministro/', informacionsuministro_list,
         name='informacionsuministro_list'),
    path('informacionsuministro/create/', informacionsuministro_create,
         name='informacionsuministro_create'),
    path('informacionsuministro/update/<int:pk>/',
         informacionsuministro_update, name='informacionsuministro_update'),
    path('informacionsuministro/delete/<int:pk>/',
         informacionsuministro_delete, name='informacionsuministro_delete'),
    path('abastecimiento/', abastecimiento_list, name='abastecimiento_list'),
    path('abastecimiento/create/', abastecimiento_create,
         name='abastecimiento_create'),
    path('abastecimiento/update/<int:pk>/',
         abastecimiento_update, name='abastecimiento_update'),
    path('abastecimiento/delete/<int:pk>/',
         abastecimiento_delete, name='abastecimiento_delete'),
    path('informacionpozos/', informacionpozos_list,
         name='informacionpozos_list'),
    path('informacionpozos/create/', informacionpozos_create,
         name='informacionpozos_create'),
    path('informacionpozos/update/<int:pk>/',
         informacionpozos_update, name='informacionpozos_update'),
    path('informacionpozos/delete/<int:pk>/',
         informacionpozos_delete, name='informacionpozos_delete'),
    path('informacionadministrativa/', informacionadministrativa_list,
         name='informacionadministrativa_list'),
    path('informacionadministrativa/create/', informacionadministrativa_create,
         name='informacionadministrativa_create'),
    path('informacionadministrativa/update/<int:pk>/',
         informacionadministrativa_update, name='informacionadministrativa_update'),
    path('informacionadministrativa/delete/<int:pk>/',
         informacionadministrativa_delete, name='informacionadministrativa_delete'),

    ### bombas###
    path('bombas/', bombas_list, name='bombas_list'),
    path('bombas/create/', bombas_create, name='bombas_create'),
    path('bombas/update/<int:pk>/', bombas_update, name='bombas_update'),
    path('bombas/delete/<int:pk>/', bombas_delete, name='bombas_delete'),

    ### red###
    path('red/', red_list, name='red_list'),
    path('red/create/', red_create, name='red_create'),
    path('red/update/<int:pk>/', red_update, name='red_update'),
    path('red/delete/<int:pk>/', red_delete, name='red_delete'),
    path('informacionsuministroelectrico/', informacionsuministroelectrico_list,
         name='informacionsuministroelectrico_list'),
    path('informacionsuministroelectrico/create/', informacionsuministroelectrico_create,
         name='informacionsuministroelectrico_create'),
    path('informacionsuministroelectrico/update/<int:pk>/',
         informacionsuministroelectrico_update, name='informacionsuministroelectrico_update'),
    path('informacionsuministroelectrico/delete/<int:pk>/',
         informacionsuministroelectrico_delete, name='informacionsuministroelectrico_delete'),

    ### informaciondistribuciontarifa ###
    path('informaciondistribuciontarifa/', informaciondistribuciontarifa_list,
         name='informaciondistribuciontarifa_list'),
    path('informaciondistribuciontarifa/create/', informaciondistribuciontarifa_create,
         name='informaciondistribuciontarifa_create'),
    path('informaciondistribuciontarifa/update/<int:pk>/',
         informaciondistribuciontarifa_update, name='informaciondistribuciontarifa_update'),
    path('informaciondistribuciontarifa/delete/<int:pk>/',
         informaciondistribuciontarifa_delete, name='informaciondistribuciontarifa_delete'),
    path('informacionapr/', informacionapr_list, name='informacionapr_list'),
    path('informacionapr/create/', informacionapr_create,
         name='informacionapr_create'),
    path('informacionapr/update/<int:pk>/',
         informacionapr_update, name='informacionapr_update'),
    path('informacionapr/delete/<int:pk>/',
         informacionapr_delete, name='informacionapr_delete'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),


    path('miapr/', MiAPRListView.as_view(), name='miapr-list'),
    path('miapr/<int:pk>/', MiAPRDetailView.as_view(), name='miapr-detail'),
    path('miapr/create/', MiAPRCreateView.as_view(), name='miapr-create'),
    path('miapr/<int:pk>/update/', MiAPRUpdateView.as_view(), name='miapr-update'),
    path('miapr/<int:pk>/delete/', MiAPRDeleteView.as_view(), name='miapr-delete'),

]