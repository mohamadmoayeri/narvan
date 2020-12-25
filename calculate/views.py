from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import TemplateView

from .forms import fibonacci_form,ackermann_form,factorial_form
import sys

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Serial

sys.setrecursionlimit(40000)


class calculator(TemplateView):

     def get(self,request):
         f1=fibonacci_form()
         f2=ackermann_form()
         f3=factorial_form()
         context={
             'f1':f1,'f2':f2,'f3':f3
         }

         return render(request,'index.html',context)

def Fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
def  fibonacci(request):
    f1=fibonacci_form()
    f2=ackermann_form()
    f3=factorial_form()
    if request.method=='POST':
        f1=fibonacci_form(request.POST)
        if f1.is_valid():

         n=f1.cleaned_data['x']
         context={
             'F_n':n,'F_response':Fibonacci(n)
         }

         return render(request,'cal.html',context)
        else:
            context={
             'f1':f1,'f2':f2,'f3':f3
         }

            return redirect('home')





cache = {}
def A(m, n):
    if m == 0:
        return n + 1

    if (m,n) in cache:
        return cache[(m, n)]

    if n == 0:
        r = cache[(m,n)] = A(m - 1,1)
        return r

    r1 = A(m, n - 1)
    r2 = A(m - 1, r1)
    r = cache[(m, n)] = r2
    return r

 
     
    


def ackermann(request):
    f1=fibonacci_form()
    f2=ackermann_form()
    f3=factorial_form()
    if request.method=='POST':
        f2=ackermann_form(request.POST)
        if f2.is_valid():

         n=f2.cleaned_data['n']
         m=f2.cleaned_data['m']

         context={
             'a_n':n,'a_m':m,'a_response':A(n,m)
         }

         return render(request,'cal.html',context)
        else:
            context={
             'f1':f1,'f2':f2,'f3':f3
         }

            return render(request,'index.html',context)
    










def Factorial(n):
    a=1
    while n>0:
        a=a*n
        n=n-1
    return a

def factorial(request):
    f1=fibonacci_form()
    f2=ackermann_form()
    f3=factorial_form()
    if request.method=='POST':
        f3=factorial_form(request.POST)
        if f3.is_valid():

         n=f3.cleaned_data['z']
         context={
             'f_n':n,'f_response':Factorial(n)
         }

         return render(request,'cal.html',context)
        else:
            context={
             'f1':f1,'f2':f2,'f3':f3
         }

            return render(request,'index.html',context)




@api_view(['POST'])
def api_calculate(request):
    ser = Serial(data=request.data)

    if ser.is_valid() and 'm' not in ser.data:
        n = ser.data['n']
        func = ser.data['func']

        if func == "fibonacci":
            return Response({"result":Fibonacci(n)},
                            status=status.HTTP_200_OK)

        elif func== "factorial":
            return Response({"result":Factorial(n)},
                            status=status.HTTP_200_OK)
        else:

            return Response({"error": "send a valid func"},
                            status=status.HTTP_400_BAD_REQUEST)
    elif ser.is_valid():
        n = ser.data['n']
        m = ser.data['m']
        func = ser.data['func']

        if func == "ackermann":
            return Response({"result": A(n,m)},
                            status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "send a valid func"},
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)