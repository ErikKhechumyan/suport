from django.shortcuts import render,redirect
from .models import Yerkir,Qaxaq,Poxoc,Shenq,Bnakaran,Molorak,Support
# Create your views here.

def yerkir(request):
    Yerkir_list = Yerkir.objects.all()
    return render(request,"page1.html",context={
        'Yerkir_list': Yerkir_list
    })
def qaxaq(request,id):
    Qaxaq_list = Yerkir.objects.filter(pk=id)
    return render(request,"page2.html",context={
        'Qaxaq_list': Qaxaq_list
    })
    
def poxoc(request,id):
    Poxoc_list = Qaxaq.objects.filter(pk=id)
    return render(request,"page3.html",context={
        'Poxoc_list': Poxoc_list
    })   
    
def shenq(request,id):
    Shenq_list = Poxoc.objects.filter(pk=id)
    return render(request,"page4.html",context={
        'Shenq_list': Shenq_list
    })   
    
def bnakaran(request,id):
    Bnakaran_list = Shenq.objects.filter(pk=id)
    return render(request,"page5.html",context={
        'Bnakaran_list': Bnakaran_list
    })   
    
def molorak(request,id):
    Molorak_list = Bnakaran.objects.filter(pk=id)
    return render(request,"page6.html",context={
        'Molorak_list': Molorak_list
    })  
     
def support(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_text = request.POST.get('text')
        Support.objects.create(email = user_email,text = user_text)
        return redirect('support')
    return render(request,'support.html',context={
        
    })