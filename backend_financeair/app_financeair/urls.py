from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('contas', ContaViewSet)
router.register('categorias', CategoriaViewSet)
router.register('tipos', TipoTransacaoViewSet)
router.register('transacoes', TransacaoViewSet)
router.register('metas', MetaFinanceiraViewSet)
router.register('despesas', DespesaFixaViewSet)
router.register('rendas', FonteRendaViewSet)

urlpatterns = [
    path('auth/register/', register),
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/', include(router.urls)),
]