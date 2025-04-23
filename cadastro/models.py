'''
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  # 000.000.000-00
    celular1 = models.CharField(max_length=15)  # (99) 99999-9999
    celular2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)  # Verifique se esse campo existe
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Verifique se esse campo existe
    data_nascimento = models.DateField(null=False)  # Verifique se esse campo existe
    endereco = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
'''
from django.db import models
from datetime import datetime

class Pessoa(models.Model):
    id_custom = models.CharField(max_length=20, unique=True, editable=False)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    numero_casa = models.CharField(max_length=10)
    zona_rural = models.BooleanField(default=False)
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)
    cartao_produtor = models.CharField(max_length=30, blank=True, null=True)
    checkbox_1 = models.BooleanField(default=False)
    checkbox_2 = models.BooleanField(default=False)
    checkbox_3 = models.BooleanField(default=False)
    checkbox_4 = models.BooleanField(default=False)
    relatorio = models.TextField(blank=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['nome', 'cpf']

    def save(self, *args, **kwargs):
        if not self.id_custom:
            ano = datetime.now().year
            count = Pessoa.objects.count() + 1
            self.id_custom = f"{ano}{count:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
