from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('contas', ContaViewSet, basename='conta')
router.register('categorias', CategoriaViewSet,  basename='categoria')
router.register('tipos', TipoTransacaoViewSet, basename='tipo-transacao')
router.register('transacoes', TransacaoViewSet, basename='transacao')
router.register('metas', MetaFinanceiraViewSet, basename='meta-financeira')
router.register('despesas', DespesaFixaViewSet, basename='despesa-fixa')
router.register('rendas', FonteRendaViewSet, basename='fonte-renda')

urlpatterns = [
    path('auth/register/', register),
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/', include(router.urls)),
]