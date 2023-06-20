from django.urls import path
from app.views import dollar

urlpatterns = [
    path('', dollar),
    path('<int:usd>', dollar),
]
