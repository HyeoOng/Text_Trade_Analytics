from django.urls import path
from .views import AnimalListApiView, AnimalDetailApiView
from .views import RecommendedStockListApiView

app_name = 'stock_api'

urlpatterns = [
    path('animals', AnimalListApiView.as_view()),
    path('animals/<int:animal_id>/', AnimalDetailApiView.as_view()),
    path('recommended_stocks', RecommendedStockListApiView.as_view())
]