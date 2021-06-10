from django.db import models
from django.contrib.postgres.fields import ArrayField

class Especialidade(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'especialidade'

class Medico(models.Model):
    nome = models.CharField(max_length=30)
    crm = models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    especialidade = models.OneToOneField(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'medico'

class Agenda(models.Model):
    dia = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = ArrayField(models.TimeField(), null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'agenda'

class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dia)

    class Meta:
        db_table = 'consulta'