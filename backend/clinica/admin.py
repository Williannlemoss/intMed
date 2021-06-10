from django.contrib import admin
from clinica.models import *

class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'email', 'telefone', 'especialidade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'crm',)
    list_per_page = 20

class Agendas(admin.ModelAdmin):
    list_display = ('id', 'dia', 'medico', 'horario')
    list_display_links = ('id',)
    search_fields = ('dia',)
    list_per_page = 20

class Consultas(admin.ModelAdmin):
    list_display = ('id', 'dia', 'data_agendamento', 'medico')
    list_display_links = ('id',)
    search_fields = ('dia',)
    list_per_page = 20

admin.site.register(Especialidade, Especialidades)
admin.site.register(Medico, Medicos)
admin.site.register(Agenda, Agendas)
admin.site.register(Consulta, Consultas)

