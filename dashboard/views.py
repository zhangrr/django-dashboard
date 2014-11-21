from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.decorators import login_required

import pdb 
from netaddr import *
from django.db import connection
from django.utils import timezone

import json

from models import *  
from forms import *  

from celery import task, current_task
from celery.result import AsyncResult
from time import sleep

@login_required

def highcharts(request):
    context = RequestContext(request)
    return render_to_response('highcharts.html', {}, context)

def ajax_data(request,num):
        json0 = {}
        json1 = {}
        json2 = {}
        json3 = {}
        list_a = []
        list_b = []
        list_c = []
        list_d = []
        cur = connection.cursor()
        cur.execute("SELECT substring(yzhou,12,5) FROM cmdb.monit01 WHERE xzhou='172.23.64.2' order by id desc limit "+num)
        result=cur.fetchall()
        for row in result:
            list_a.append(row[0])
        cur.execute("SELECT shuzhi FROM cmdb.monit01 WHERE xzhou='172.23.64.2' order by id desc limit "+num)
        result=cur.fetchall()
        for row in result:
            list_b.append(row[0])
        cur.execute("SELECT shuzhi FROM cmdb.monit01 WHERE xzhou='172.23.64.4' order by id desc limit "+num)
        result=cur.fetchall()
        for row in result:
            list_c.append(row[0])
        cur.execute("SELECT shuzhi FROM cmdb.monit01 WHERE xzhou='172.23.64.5' order by id desc limit "+num)
        result=cur.fetchall()
        for row in result:
            list_d.append(row[0])
        cur.close()
        json0['name'] = "Time"
        list_a.reverse()
        json0['data'] = list_a
        json1['name'] = "172.23.64.2"
        list_b.reverse()
        json1['data'] = list_b
        json2['name'] = "172.23.64.4"
        list_c.reverse()
        json2['data'] = list_c
        json3['name'] = "172.23.64.5"
        list_d.reverse()
        json3['data'] = list_d
        return HttpResponse(json.dumps([json0,json1,json2,json3], ensure_ascii=False),content_type="application/json")

def list_vimage(request):
    lines = Vimage.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('list_vimage.html', RequestContext(request, {'lines': show_lines,}))

def create_vimage(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CreateVimageForm(request.POST)
        if form.is_valid():
            p = Vimage.objects.create(
                img_url = form.cleaned_data['img_url'],
            )
            p.save()
            return HttpResponseRedirect("/dashboard/i/list")
        else:
            return render_to_response('create_vimage.html', {'form': form,'something_is_wrong':True}, context)
    else:
        form = CreateVimageForm()

    return render_to_response('create_vimage.html', {'form': form}, context)

def edit_vimage(request, id):
    context = RequestContext(request)
    one_instance = Vimage.objects.get(id=id)
    form = EditVimageForm(request.POST or None, instance = one_instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            return render_to_response('edit_vimage.html', {'form': form,'something_is_wrong':True}, context)
        return HttpResponseRedirect("/dashboard/i/list")
    return render_to_response('edit_vimage.html', {'form':form}, context)

def delete_vimage(request, id):
    context = RequestContext(request)
    one_instance = Vimage.objects.get(id=id)
    form = DeleteVimageForm(request.POST or None, instance = one_instance)
    if request.method=='POST':
        one_instance.delete()
        return HttpResponseRedirect("/dashboard/i/list")
    return render_to_response('delete_vimage.html', {'form': form}, context)
    
def list_pmachine(request):  
    lines = Pmachine.objects.order_by("-id")
    paginator = Paginator(lines, 10)  
    page = request.GET.get('page')  
    try:  
        show_lines = paginator.page(page)  
    except PageNotAnInteger:  
        # If page is not an integer, deliver first page.  
        show_lines = paginator.page(1)  
    except EmptyPage:  
        # If page is out of range (e.g. 9999), deliver last page of results.  
        show_lines = paginator.page(paginator.num_pages)  
    return render_to_response('list_pmachine.html', RequestContext(request, {'lines': show_lines,}))

def create_pmachine(request):  
    context = RequestContext(request)

    if request.method == 'POST':
        form = CreatePmachineForm(request.POST)
        if form.is_valid():
            p = Pmachine.objects.create(
                ip = form.cleaned_data['ip'],
                cpu = form.cleaned_data['cpu'],
                disk = form.cleaned_data['disk'],
                memory = form.cleaned_data['memory'],
                maxvm = form.cleaned_data['maxvm'], 
            ) 
            #pdb.set_trace()
            p.save() 
            return HttpResponseRedirect("/dashboard/p/list")
        else:
            return render_to_response('create_pmachine.html', {'form': form,'something_is_wrong':True}, context)
    else:
        form = CreatePmachineForm()

    return render_to_response('create_pmachine.html', {'form': form}, context)

def batch_create_pmachine(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = BatchCreatePmachineForm(request.POST)
        if form.is_valid():
            ipfirst = request.POST.get('ipfirst', '')  
            iplast  = request.POST.get('iplast', '')  
            ip_list = list(iter_iprange(ipfirst, iplast))
            for oneip in ip_list:
                p = Pmachine.objects.create(
                    ip = str(oneip),
                    cpu = form.cleaned_data['cpu'],
                    disk = form.cleaned_data['disk'],
                    memory = form.cleaned_data['memory'],
                    maxvm = form.cleaned_data['maxvm'],
                )
                p.save()
            return HttpResponseRedirect("/dashboard/p/list")
        else:
            return render_to_response('create_pmachine.html', {'form': form,'something_is_wrong':True}, context)
    else:
        form = BatchCreatePmachineForm()

    return render_to_response('create_pmachine.html', {'form': form}, context)

def edit_pmachine(request, id):  
    context = RequestContext(request)
    one_instance = Pmachine.objects.get(id=id)
    form = EditPmachineForm(request.POST or None, instance = one_instance)
    if request.method == 'POST':
        #pdb.set_trace()
        if form.is_valid():  
            form.save()
        else:
            return render_to_response('edit_pmachine.html', {'form': form,'something_is_wrong':True}, context)
        return HttpResponseRedirect("/dashboard/p/list")
    return render_to_response('edit_pmachine.html', {'form':form}, context)

def delete_pmachine(request, id):  
    context = RequestContext(request)
    one_instance = Pmachine.objects.get(id=id)
    form = DeletePmachineForm(request.POST or None, instance = one_instance)
    if request.method=='POST':
        one_instance.delete()
        return HttpResponseRedirect("/dashboard/p/list")
    return render_to_response('delete_pmachine.html', {'form': form}, context)

def list_vmachine(request):
    lines = Vmachine.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('list_vmachine.html', RequestContext(request, {'lines': show_lines,}))

def create_vmachine(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CreateVmachineForm(request.POST)
        if form.is_valid():
            p = Vmachine.objects.create(
                ip = form.cleaned_data['ip'],
                netmask = form.cleaned_data['netmask'],
                gateway = form.cleaned_data['gateway'],
                pmachine = form.cleaned_data['pmachine'],
                vimage = form.cleaned_data['vimage'],
                states = 'init',
            )
            p.save()
            q = Task.objects.create(
                creater = request.user,
                vimage = p.vimage,
                vmachine = p,
                createdtime = timezone.now(),
            )
            q.save()
            return HttpResponseRedirect("/dashboard/v/list")
        else:
            return render_to_response('create_pmachine.html', {'form': form,'something_is_wrong':True}, context)
    else:
        form = CreateVmachineForm()

    return render_to_response('create_vmachine.html', {'form': form}, context)

def batch_create_vmachine(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = BatchCreateVmachineForm(request.POST)
        if form.is_valid():
            ipfirst = request.POST.get('ipfirst', '')
            iplast  = request.POST.get('iplast', '')
            ip_list = list(iter_iprange(ipfirst, iplast))
            machine_list =  list( Pmachine.objects.order_by("id") )
            for oneip in ip_list:
                onemachine = machine_list.pop(0)
                if onemachine.vmachines.all().count() < onemachine.maxvm:
                    p = Vmachine.objects.create(
                        ip = str(oneip),
                        netmask = form.cleaned_data['netmask'],
                        gateway = form.cleaned_data['gateway'],
                        pmachine = onemachine,
                        vimage = form.cleaned_data['vimage'],
                        states = 'init',
                    )
                    p.save()
                    q = Task.objects.create(
                        creater = request.user,
                        vimage = p.vimage,
                        vmachine = p,
                        createdtime = timezone.now(),
                    )
                    q.save()
                else:
                    machine_list.remove(onemachine)
                machine_list.append(onemachine)
            return HttpResponseRedirect("/dashboard/v/list")
        else:
            return render_to_response('create_vmachine.html', {'form': form,'something_is_wrong':True}, context)
    else:
        form = BatchCreateVmachineForm()

    return render_to_response('create_vmachine.html', {'form': form}, context)

def list_task(request):
    lines = Task.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('list_task.html', RequestContext(request, {'lines': show_lines,}))

@task()
def do_work():
    """ Get some rest, asynchronously, and update the state all the time """
    for i in range(100):
        sleep(0.1)
        current_task.update_state(state='PROGRESS',
            meta={'current': i, 'total': 100})

def run_task(request):
    if Task.objects.filter(uuid__isnull=True):
      for e in Task.objects.filter(uuid__isnull=True):
        job = do_work.delay()
        e.uuid=job
        e.save()
        return HttpResponseRedirect('/dashboard/t/list')
    return HttpResponseRedirect('/dashboard/t/list')

def poll_state(request):
    """ A view to report the progress to the user """
    if 'job' in request.GET:
        job_id = request.GET['job']
    else:
        return HttpResponse('No job id given.')
    job = AsyncResult(job_id)
    data = job.result or job.state
    return HttpResponse(json.dumps({ "html": data },ensure_ascii=False), content_type="application/json")

