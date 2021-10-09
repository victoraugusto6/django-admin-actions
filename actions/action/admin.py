from django.contrib import admin
from django.contrib.admin import ModelAdmin

from actions.action.models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(ModelAdmin):
    list_display = ('nome', 'ativo', 'categoria', 'created_at', 'uploaded_at')
