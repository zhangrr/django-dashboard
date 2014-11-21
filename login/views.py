from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response,render,get_object_or_404    
from django.http import HttpResponse, HttpResponseRedirect    
#from django.contrib.auth.models import User    
from django.contrib import auth  
from django.contrib import messages  
from django.template.context import RequestContext  
  
#from django.forms.formsets import formset_factory  
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  
  
#from bootstrap_toolkit.widgets import BootstrapUneditableInput  
from django.contrib.auth.decorators import login_required  
  
from .forms import LoginForm, ChangepwdForm
  
def login(request):  
    if request.method == 'GET':  
        form = LoginForm()  
        return render_to_response('login.html', RequestContext(request, {'form': form,}))  
    else:  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username', '')  
            password = request.POST.get('password', '')  
            user = auth.authenticate(username=username, password=password)  
            if user is not None and user.is_active:  
                auth.login(request, user)  
                #return render_to_response('index.html', RequestContext(request))  
    		return HttpResponseRedirect("/dashboard/p/list")
            else:  
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))  
        else:  
            return render_to_response('login.html', RequestContext(request, {'form': form,}))

def logout(request):  
    auth.logout(request)  
    return HttpResponseRedirect("/accounts/login/")

@login_required
def changepwd(request):  
    context = RequestContext(request)
    if request.method == 'GET':  
        form = ChangepwdForm()  
        #return render_to_response('changepwd.html', RequestContext(request, {'form': form,}))  
        return render_to_response('changepwd.html', {'form':form}, context)
    else:  
        form = ChangepwdForm(request.POST)  
        if form.is_valid():  
            username = request.user.username  
            oldpassword = request.POST.get('oldpassword', '')  
            user = auth.authenticate(username=username, password=oldpassword)  
            if user is not None and user.is_active:  
                newpassword = request.POST.get('newpassword1', '')  
                user.set_password(newpassword)  
                user.save()  
                #return render_to_response('index.html', RequestContext(request,{'changepwd_success':True}))  
                #return render_to_response('index.html', {'form':form,'changepwd_success':True}, context)
                return HttpResponseRedirect("/dashboard/p/list/")
            else:  
                return render_to_response('changepwd.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))  
        else:  
            return render_to_response('changepwd.html', RequestContext(request, {'form': form,}))
