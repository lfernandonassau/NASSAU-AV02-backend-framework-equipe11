from django.db import models
from django.contrib.auth.models import User

class Conta(models.Model):
    nome = models.CharField(max_length=100)
    saldo_inicial = models.DecimalField(max_digits=12, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contas')

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categorias')

class TipoTransacao(models.Model):
    nome = models.CharField(max_length=20)  # 'ENTRADA' / 'SAIDA'

class Transacao(models.Model):
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transacoes')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='transacoes')
    tipo = models.ForeignKey(TipoTransacao, on_delete=models.PROTECT, related_name='transacoes')

class MetaFinanceira(models.Model):
    nome = models.CharField(max_length=100)
    valor_objetivo = models.DecimalField(max_digits=12, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='metas')

class DespesaFixa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='despesas_fixas')

class FonteRenda(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fontes_renda')