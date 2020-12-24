from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from .forms import fibonacci_form,ackermann_form,factorial_form
import sys

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

            return render(request,'index.html',context)





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