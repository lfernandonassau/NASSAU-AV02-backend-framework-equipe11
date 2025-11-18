from django.contrib import admin
from models import Conta, Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda

admin.site.register({Conta, Categoria, TipoTransacao, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda })