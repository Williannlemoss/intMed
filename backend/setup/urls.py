from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clinica.views import *

router = routers.DefaultRouter()
router.register('especialidades', EspecialidadesViewSet, basename='especialidades')
router.register('medicos', MedicoViewSet, basename='medicos')
router.register('consultas', ConsultaViewSet, basename='consultas')
router.register('agendas', AgendaViewSet, basename='agendas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
