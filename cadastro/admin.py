from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id_custom', 'nome', 'cpf', 'telefone1', 'data_registro')
    search_fields = ('nome', 'cpf', 'telefone1')
    list_filter = ('data_registro',)
    ordering = ('nome',)

admin.site.register(Pessoa, PessoaAdmin)