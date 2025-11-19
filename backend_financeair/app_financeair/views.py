<<<<<<< HEAD
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Conta, Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda
from .serializers import RegisterSerializer, ContaSerializer, CategoriaSerializer, TipoTransacaoSerializer, TransacaoSerializer, MetaFinanceiraSerializer, DespesaFixaSerializer, FonteRendaSerializer

=======
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import (
    Conta, Categoria, TipoTransacao, Transacao,
    MetaFinanceira, DespesaFixa, FonteRenda
)
from .serializers import (
    ContaSerializer, CategoriaSerializer, RegisterSerializer, TipoTransacaoSerializer,
    TransacaoSerializer, MetaFinanceiraSerializer,
    DespesaFixaSerializer, FonteRendaSerializer
)

# -----------------------------
# REGISTRO DE USUÁRIO (SIGNUP)
# -----------------------------
>>>>>>> e1ba7a369c84d5867e3f06b2693de0ed62af931f
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    s = RegisterSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    user = s.save()
<<<<<<< HEAD
    return Response({'id': user.id, 'username': user.username}, status=201)

class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Conta.objects.filter(usuario=self.request.user)
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

# Crie os viewsets para Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda seguindo o mesmo padrão: filtrar por request.user e salvar usuario quando necessário.
=======
    return Response({"message": "Usuário criado", "id": user.id})
# -----------------------------
# CONTA
# -----------------------------
class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all() 
    serializer_class = ContaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Conta.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

# -----------------------------
# CATEGORIA
# -----------------------------
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

# -----------------------------
# TIPO DE TRANSAÇÃO
# -----------------------------
class TipoTransacaoViewSet(viewsets.ModelViewSet):
    queryset = TipoTransacao.objects.all()
    serializer_class = TipoTransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

# -----------------------------
# TRANSAÇÃO
# -----------------------------
class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transacao.objects.filter(conta__usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

# -----------------------------
# METAS FINANCEIRAS
# -----------------------------
class MetaFinanceiraViewSet(viewsets.ModelViewSet):
    queryset = MetaFinanceira.objects.all()
    serializer_class = MetaFinanceiraSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MetaFinanceira.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

# -----------------------------
# DESPESAS FIXAS
# -----------------------------
class DespesaFixaViewSet(viewsets.ModelViewSet):
    queryset = DespesaFixa.objects.all()
    serializer_class = DespesaFixaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DespesaFixa.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

# -----------------------------
# FONTES DE RENDA
# -----------------------------
class FonteRendaViewSet(viewsets.ModelViewSet):
    queryset = FonteRenda.objects.all()
    serializer_class = FonteRendaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FonteRenda.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
>>>>>>> e1ba7a369c84d5867e3f06b2693de0ed62af931f
