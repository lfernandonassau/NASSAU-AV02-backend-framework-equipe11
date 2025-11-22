from rest_framework import serializers
from .models import Conta, Categoria, TipoTransacao, Transacao, MetaFinanceira, DespesaFixa, FonteRenda
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta:
        model = User
        fields = ('id','username','email','password')
    def create(self, validated):
        return User.objects.create_user(username=validated['username'], email=validated.get('email',''), password=validated['password'])
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ContaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Conta
        fields = ['id', 'nome', 'saldo_inicial', 'usuario']

      
class CategoriaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'usuario']


class TipoTransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransacao
        fields = ['id', 'nome']


class TransacaoSerializer(serializers.ModelSerializer):
    conta = serializers.PrimaryKeyRelatedField(queryset=Conta.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoTransacao.objects.all())

    class Meta:
        model = Transacao
        fields = [
            'id',
            'descricao',
            'valor',
            'data',
            'conta',
            'categoria',
            'tipo'
        ]


class MetaFinanceiraSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = MetaFinanceira
        fields = ['id', 'nome', 'valor_objetivo', 'usuario']


class DespesaFixaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = DespesaFixa
        fields = ['id', 'nome', 'valor', 'usuario']



class FonteRendaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = FonteRenda
        fields = ['id', 'descricao', 'valor', 'usuario']

