from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import product

# Create your views here.

class home(View):
    def get(self,request):
        return render(request,template_name='home.html')

class productinput(View):
    def get(self,request):
        return render(request,template_name='product.html')

class Insert(View):
    def get(self,request):
        p_id=int(request.GET['t1'])
        p_name=(request.GET['t2'])
        p_cost=float(request.GET['t3'])
        p_mfdt=(request.GET['t4'])
        p_expdt=(request.GET['t5'])
        p1=product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res=HttpResponse('product addede successfuly')
        return res
        
 
class displayview(View):
    def get(self,request):
        q=product.objects.all()
        con_dict={'record':q}
        return render(request,template_name='display.html',context=con_dict)

class deletinput(View):
    def get(self,request):
        qs=product.objects.all()
        con_dict={'record':qs}
        return render(request,template_name='delete.html',context=con_dict)

class deleteview(View):
    def get(self,request):
        #p_id=int(request.GET['t1'])
        p_name=request.GET['t2']
        prod=product.objects.filter(pname=p_name)
        prod.delete()
        res=HttpResponse('Deleted successfuly')
        return res
    
class UpdateInput(View):
    def get(self,request):
        qs = product.objects.all()
        condic = {"records": qs}
        return render(request, 'updateinput.html', context=condic)
class UpdateDetails(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=product.objects.get(pid=p_id)
        condic={'rec':prod}
        return render(request,'update.html',context=condic)
class Update(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=product.objects.get(pid=p_id)
        prod.pname=request.GET["t2"]
        prod.pcost=float(request.GET["t3"])
        prod.pmfdt=request.GET["t4"]
        prod.pexpdt=request.GET["t5"]
        prod.save()
        return redirect('/smart/display')