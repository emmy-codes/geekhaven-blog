from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogGrid.as_view(), name='homepage')
]
