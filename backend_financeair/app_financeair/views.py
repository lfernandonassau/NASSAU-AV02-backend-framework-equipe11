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


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)



class TipoTransacaoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoTransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TipoTransacao.objects.all()



class TransacaoViewSet(viewsets.ModelViewSet):
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transacao.objects.filter(conta__usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save()



class MetaFinanceiraViewSet(viewsets.ModelViewSet):
    serializer_class = MetaFinanceiraSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MetaFinanceira.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)



class DespesaFixaViewSet(viewsets.ModelViewSet):
    serializer_class = DespesaFixaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DespesaFixa.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)



class FonteRendaViewSet(viewsets.ModelViewSet):
    serializer_class = FonteRendaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FonteRenda.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)