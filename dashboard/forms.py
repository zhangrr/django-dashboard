# -*- coding: utf-8 -*-
from django import forms  
from django.forms import ModelForm
from django.db import models
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

from .models import *

class CreateVimageForm(forms.Form):
    img_url = forms.CharField(  
        required=True,
        label=u'虚机镜像地址(http)', 
        error_messages={'required': u'请输入虚机镜像的下载地址'},
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'虚机镜像下载地址',
            }
        ),
    )

class EditVimageForm(ModelForm):
    img_url = forms.CharField(
        required=True,
        label=u'虚机镜像地址(http)',
        error_messages={'required': u'请输入虚机镜像的下载地址'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'虚机镜像下载地址',
            }
        ),
    )
    class Meta:
        model = Vimage
        fields = ['img_url']

class DeleteVimageForm(ModelForm):
    img_url = forms.CharField(
        required=True,
        label=u'虚机镜像地址(http)',
        error_messages={'required': u'请输入虚机镜像的下载地址'},
        widget=BootstrapUneditableInput(),
    )
    class Meta:
        model = Vimage
        fields = ['img_url']

class CreatePmachineForm(forms.Form):  
    ip = forms.GenericIPAddressField(  
        required=True,  
        label=u'IP地址',
        error_messages={'required': u'请输入IP地址'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'IP地址',
            }  
        ),  
    )      
    cpu = forms.CharField(  
        required=True,  
        label=u'CPU核心数',  
        error_messages={'required': u'请输入CPU核心数'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'CPU核心数',
            }  
        ),  
    )     
    disk = forms.CharField(  
        required=True,  
        label=u'硬盘大小',
        error_messages={'required': u'请输入硬盘大小(G)'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'硬盘大小',
            }  
        ),  
    )      
    memory = forms.CharField(  
        required=True,  
        label=u'内存大小',
        error_messages={'required': u'请输入内存大小'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'硬盘大小',
            }  
        ),  
    )      
    maxvm = forms.IntegerField(  
        required=True,  
        label=u'可产虚机数',
        error_messages={'required': u'请输入最大可产虚机数'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'可产虚机数',
            }  
        ),  
    )

class BatchCreatePmachineForm(forms.Form):  
    ipfirst = forms.GenericIPAddressField(  
        required=True,  
        label=u'起始IP地址',
        error_messages={'required': u'请输入起始IP地址'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'起始IP地址',
            }  
        ),  
    )      
    iplast = forms.GenericIPAddressField(  
        required=True,  
        label=u'终止IP地址',
        error_messages={'required': u'请输入终止IP地址'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'终止IP地址',
            }  
        ),  
    )      
    cpu = forms.CharField(  
        required=True,  
        label=u'CPU核心数',  
        error_messages={'required': u'请输入CPU核心数'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'CPU核心数',
            }  
        ),  
    )     
    disk = forms.CharField(  
        required=True,  
        label=u'硬盘大小',
        error_messages={'required': u'请输入硬盘大小(G)'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'硬盘大小',
            }  
        ),  
    )      
    memory = forms.CharField(  
        required=True,  
        label=u'内存大小',
        error_messages={'required': u'请输入内存大小'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'硬盘大小',
            }  
        ),  
    )      
    maxvm = forms.IntegerField(  
        required=True,  
        label=u'可产虚机数',
        error_messages={'required': u'请输入最大可产虚机数'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'可产虚机数',
            }  
        ),  
    )
      
class EditPmachineForm(ModelForm):  
    ip = forms.GenericIPAddressField(  
        required=True,  
        label=u'IP地址',
        error_messages={'required': u'请输入IP地址'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'IP地址',
            }  
        ),  
    )      
    cpu = forms.CharField(  
        required=True,  
        label=u'CPU核心数',  
        error_messages={'required': u'请输入CPU核心数'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'CPU核心数',
            }  
        ),  
    )     
    disk = forms.CharField(  
        required=True,  
        label=u'硬盘大小',
        error_messages={'required': u'请输入硬盘大小(G)'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'硬盘大小',
            }  
        ),  
    )      
    memory = forms.CharField(  
        required=True,  
        label=u'内存大小',
        error_messages={'required': u'请输入内存大小'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'硬盘大小',
            }  
        ),  
    )      
    maxvm = forms.IntegerField(  
        required=True,  
        label=u'可产虚机数',
        error_messages={'required': u'请输入最大可产虚机数'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'可产虚机数',
            }  
        ),  
    )
    class Meta:
        model = Pmachine
        fields = ['ip', 'cpu', 'disk', 'memory', 'maxvm']

class DeletePmachineForm(ModelForm):
    ip = forms.GenericIPAddressField(  
        label=u'IP地址',
        widget=BootstrapUneditableInput(),
    )      
    cpu = forms.CharField(  
        label=u'CPU核心数',  
        widget=BootstrapUneditableInput(),
    )     
    disk = forms.CharField(  
        label=u'硬盘大小',
        widget=BootstrapUneditableInput(),
    )      
    memory = forms.CharField(  
        label=u'内存大小',
        widget=BootstrapUneditableInput(),
    )      
    maxvm = forms.IntegerField(  
        label=u'可产虚机数',
        widget=BootstrapUneditableInput(),
    )
    class Meta:
        model = Pmachine
        fields = ['ip', 'cpu', 'disk', 'memory', 'maxvm']

class CreateVmachineForm(forms.Form):
    ip = forms.GenericIPAddressField(
        required=True,
        label=u'IP地址',
        error_messages={'required': u'请输入IP地址'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'IP地址',
            }
        ),
    )
    netmask = forms.CharField(
        required=True,
        label=u'子网掩码',
        error_messages={'required': u'请输入子网掩码'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'子网掩码',
            }
        ),
    )
    gateway = forms.CharField(
        required=True,
        label=u'网关地址',
        error_messages={'required': u'请输入网关地址'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'网关地址',
            }
        ),
    )
    pmachine = forms.ModelChoiceField(
        queryset=Pmachine.objects.all(),
        required=True,
        label=u'所属物理宿主机',
        error_messages={'required': u'请选则所属物理宿主机'},
        widget=forms.Select(
            attrs={
                'placeholder':u'所属物理宿主机',
            }
        ),
    )
    vimage = forms.ModelChoiceField(
        queryset=Vimage.objects.all(),
        required=True,
        label=u'所用虚机模板',
        error_messages={'required': u'请选则所用虚机模板'},
        widget=forms.Select(
            attrs={
                'placeholder':u'所用虚机模板',
            }
        ),
    )

class BatchCreateVmachineForm(forms.Form):  
    ipfirst = forms.GenericIPAddressField(  
        required=True,  
        label=u'起始IP地址',
        error_messages={'required': u'请输入起始IP地址'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'起始IP地址',
            }  
        ),  
    )      
    iplast = forms.GenericIPAddressField(  
        required=True,  
        label=u'终止IP地址',
        error_messages={'required': u'请输入终止IP地址'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u'终止IP地址',
            }  
        ),  
    )      
    netmask = forms.CharField(
        required=True,
        label=u'子网掩码',
        error_messages={'required': u'请输入子网掩码'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'子网掩码',
            }
        ),
    )
    gateway = forms.CharField(
        required=True,
        label=u'网关地址',
        error_messages={'required': u'请输入网关地址'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'网关地址',
            }
        ),
    )
    vimage = forms.ModelChoiceField(
        queryset=Vimage.objects.all(),
        required=True,
        label=u'所用虚机模板',
        error_messages={'required': u'请选则所用虚机模板'},
        widget=forms.Select(
            attrs={
                'placeholder':u'所用虚机模板',
            }
        ),      
    )
