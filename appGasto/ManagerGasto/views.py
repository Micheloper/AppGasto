from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Activo,Costo
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import LoginForm,SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class Home(LoginRequiredMixin,View):
    login_url = '/login/'
    
    def get(self,request):
        context = {}
        costobj = Costo.objects.filter(user=request.user).order_by('activo')
        activoObj = Activo.objects.filter(user=request.user).order_by('proposito')
        context['costs'] = costobj
        context['activos'] = activoObj


        asub = {}
        for costs in costobj:
            sub = costs.importe
            print('All Activo Data')
            print(costs.activo.id,end=' ')
            print(costs.activo.proposito,end=' ')
            print(costs.activo.importe_Total,end=' ')
            print(costs.activo.fecha)
            print('All Costo Data')
            print(costs.id,end=' ')
            print(costs.descripcion,end=' ')
            print(costs.importe)
            print('===================')
            
            if costs.activo.id in asub.keys():     
                asub[costs.activo.id] = asub[costs.activo.id]-costs.importe
            else:
                asub[costs.activo.id] = costs.activo.importe_Total
                asub[costs.activo.id] = asub[costs.activo.id]-costs.importe
            print('Now avialable',asub[costs.activo.id])


        print('After Substration:',asub)

        context['ailables'] = asub

        # here i create all activos unique dictonary
        fines = {}
        for activoObjs in activoObj:
            fines[activoObjs.proposito] = activoObjs. importe_Total

        print("My activoObj:",fines)
        context['fines'] = fines

        return render(request,'index.html',context)

class AgregarGastos(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Costo
    fields = ['activo','descripcion','importe']
    template_name = 'agregarGastos.html '
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return [(Costo.objects.filter(user = self.request.user)),(Activo.objects.filter(user = self.request.user))]

class AgregarPresupuesto(LoginRequiredMixin,CreateView):
    model = Activo
    fields = ['proposito','importe_Total']
    template_name = 'agregarPresupuesto.html'
    success_url = '/'
    login_url = '/login/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditarGasto(LoginRequiredMixin,UpdateView):
    model = Costo
    fields = ['activo','descripcion','importe']
    template_name = 'editarGasto.html'
    success_url = '/'
    login_url = '/login/'
    def get_queryset(self):
        return Costo.objects.filter(user = self.request.user)

class DeleteCosto(LoginRequiredMixin,DeleteView):
    model = Costo
    context_object_name = 'cost'
    template_name = 'deletecost.html'
    success_url = '/'

class DeleteActivo(LoginRequiredMixin,DeleteView):
    model = Activo
    context_object_name = 'activo'    
    template_name = 'deleteActivo.html'
    success_url = '/'
    login_url = '/login/'

class Userlogin(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request,'login.html',{'form':form})
        else:
            return redirect('/')
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/?next=%s' % request.path)
            else:
                return redirect(('login'))
        return render(request,'login.html',{'form':form})

@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return redirect('login')

class UserSignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
