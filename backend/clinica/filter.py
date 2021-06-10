import django_filters
from clinica.models import *

class EspecialidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='exact')

    class Meta:
        model = Especialidade
        fields = ['nome']

class MedicoFilter(django_filters.FilterSet):
    especialidade = django_filters.CharFilter()

    class Meta:
        model = Medico
        fields = ['especialidade']

# class ConsultaFilter(django_filters.FilterSet):
#     data_agendamento = django_filters.DateFilter(lookup_expr='gt')
#
#     class Meta:
#         model = Consulta
#         fields = ['data_agendamento']

class AgendaFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='dia', lookup_expr='gte')
    data_final = django_filters.DateFilter(field_name='dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = ['medico']


