from django.urls import path
from .views import ListTodo, DetailTodo
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
