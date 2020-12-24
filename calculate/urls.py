
from django.urls import path,include
from .views import calculator,fibonacci,factorial,ackermann
urlpatterns = [
    path('',calculator.as_view(),name='home'),
    path('fibonacci',fibonacci,name='fibonachi'),
    path('ackermann',ackermann,name='ackerman'),
    path('factorial',factorial,name='factorial'),
    
    
]