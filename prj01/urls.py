from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'prj01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #admin view
    url(r'^admin/', include(admin.site.urls)),

    #index view
    url(r'^$', 'login.views.login'),

    url(r'^accounts/login/$',  'login.views.login'),
    url(r'^accounts/logout/$', 'login.views.logout'),
    url(r'^accounts/changepwd/$', 'login.views.changepwd'),


    #highcharts ajax
    url(r'^dashboard/highcharts/$', 'dashboard.views.highcharts'),
    url(r'^dashboard/ajax/data/(?P<num>[^/]+)/$', 'dashboard.views.ajax_data'),

    #vimage 
    url(r'^dashboard/i/list/$', 'dashboard.views.list_vimage'),
    url(r'^dashboard/i/create/$', 'dashboard.views.create_vimage'),
    url(r'^dashboard/i/edit/(?P<id>[^/]+)/$', 'dashboard.views.edit_vimage'),
    url(r'^dashboard/i/delete/(?P<id>[^/]+)/$', 'dashboard.views.delete_vimage'),

    #pmachine
    url(r'^dashboard/p/list/$', 'dashboard.views.list_pmachine'),
    url(r'^dashboard/p/create/$', 'dashboard.views.create_pmachine'),
    url(r'^dashboard/p/bcreate/$', 'dashboard.views.batch_create_pmachine'),
    url(r'^dashboard/p/edit/(?P<id>[^/]+)/$', 'dashboard.views.edit_pmachine'),
    url(r'^dashboard/p/delete/(?P<id>[^/]+)/$', 'dashboard.views.delete_pmachine'),

    #vmachine
    url(r'^dashboard/v/list/$', 'dashboard.views.list_vmachine'),
    url(r'^dashboard/v/create/$', 'dashboard.views.create_vmachine'),
    url(r'^dashboard/v/bcreate/$', 'dashboard.views.batch_create_vmachine'),
   
    #task 
    url(r'^dashboard/t/list/$', 'dashboard.views.list_task'),
    url(r'^dashboard/t/runall$', 'dashboard.views.run_task'),
    url(r'^dashboard/t/poll_state$', 'dashboard.views.poll_state'),

]

