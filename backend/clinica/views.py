from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from datetime import date

from clinica.filter import *
from clinica.serializer import *

class EspecialidadesViewSet(viewsets.ModelViewSet):
    '''Exebindo todos as especialidades'''
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)

class MedicoViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os medicos'''
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('nome',)
    filter_class = MedicoFilter


class AgendaViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as agendas'''
    queryset = Agenda.objects.filter(dia__gte=date.today(), horario__isnull=False).order_by('dia')
    serializer_class = AgendaSerializer
    filter_class = AgendaFilter

class ConsultaViewSet(viewsets.ModelViewSet):
    '''Exibindo todos as consultas'''
    queryset = Consulta.objects.filter(dia__gte=date.today()).order_by('dia', 'horario')
    serializer_class = ConsultaSerializer
