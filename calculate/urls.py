
from django.urls import path,include
from .views import calculator,fibonacci,factorial,ackermann,api_calculate
urlpatterns = [
    path('',calculator.as_view(),name='home'),
    path('fibonacci',fibonacci,name='fibonachi'),
    path('ackermann',ackermann,name='ackerman'),
    path('factorial',factorial,name='factorial'),
    path('api',api_calculate,name='api'),
    
    
]