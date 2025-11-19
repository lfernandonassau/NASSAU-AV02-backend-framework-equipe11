from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Conta, Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda
from .serializers import RegisterSerializer, ContaSerializer, CategoriaSerializer, TipoTransacaoSerializer, TransacaoSerializer, MetaFinanceiraSerializer, DespesaFixaSerializer, FonteRendaSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    s = RegisterSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    user = s.save()
    return Response({'id': user.id, 'username': user.username}, status=201)

class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Conta.objects.filter(usuario=self.request.user)
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

# Crie os viewsets para Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda seguindo o mesmo padrão: filtrar por request.user e salvar usuario quando necessário.
