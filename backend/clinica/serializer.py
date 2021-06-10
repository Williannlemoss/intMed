from rest_framework import serializers
from clinica.models import *
# from clinica.validators import *

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome']

class MedicoSerializer(serializers.ModelSerializer):
    # especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'telefone', 'especialidade']

class AgendaSerializer(serializers.ModelSerializer):
    # medico = MedicoSerializer(read_only=True)

    class Meta:
        model = Agenda
        fields = ['id', 'dia', 'medico', 'horario']

class ConsultaSerializer(serializers.ModelSerializer):
    # medico = MedicoSerializer(many=False, read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']

