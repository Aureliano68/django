from django.shortcuts import render
from .form import input1,input2,input3,input4
# Create your views here.

def form1(request):
    forms=input1()
    contex={
        'form':forms
    }
    return render(request,'forms/form1.html',contex)

def form2(request):
    forms=input2()
    contex={
        'form':forms
    }
    return render(request,'forms/form2.html',contex)

def form3(request):
    forms=input3()
    contex={
        'form':forms
    }
    return render(request,'forms/form3.html',contex)


def form4(request):
    contex={}
    if request.method =='POST':
        form=input4(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data['name'],data['family'],data['age']) 
            
    else:
        form=input4()
    contex['form']=form
        
    return render(request,'forms/form4.html',contex)
