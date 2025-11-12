from django.contrib import admin
from .model import Conta, Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda

admin.site.register({Conta, Categoria, TipoTransacao, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda })