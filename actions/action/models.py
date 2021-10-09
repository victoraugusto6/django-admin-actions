from django.db import models

CATEGORIA = [
    ('motorista', 'Motorista'),
    ('passageiro', 'Passageiro')
]


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField()
    categoria = models.CharField(choices=CATEGORIA, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
