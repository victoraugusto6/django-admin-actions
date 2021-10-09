from django.contrib import admin
from django.contrib.admin import ModelAdmin

from actions.action.models import Pessoa


@admin.action(description='Habilitar Pessoa')
def enable_person(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.action(description='Desabilitar Pessoa')
def disable_person(modeladmin, request, queryset):
    queryset.update(ativo=False)


@admin.action(description='Trocar para Motorista')
def change_to_driver(modeladmin, request, queryset):
    queryset.update(categoria='motorista')


@admin.action(description='Trocar para Passageiro')
def change_to_passenger(modeladmin, request, queryset):
    queryset.update(categoria='passageiro')


@admin.register(Pessoa)
class PessoaAdmin(ModelAdmin):
    list_display = ('nome', 'ativo', 'categoria', 'created_at', 'uploaded_at')
    actions = [enable_person, disable_person, change_to_driver, change_to_passenger]
