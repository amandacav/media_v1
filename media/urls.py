
"""media URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from store.models import Order
from store import views 

app_name = 'store'



urlpatterns = [

#main views

    url(r'^$', views.home, name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/', views.home, name='home'),
#   url(r'^invalid', 'store_views.invalid_login'),
#   url(r'^hijack/', include('hijack.urls')), #to hijack other users


#user views
##Inventory
    url(r'^inventory/$', views.inventory, name='inventory'),
#    $ allows you to build on the URL while using different views
    url(r'^inventory/new', views.create_item, name='new_item'),
    url(r'^inventory/(?P<id>[0-9]*)$', views.single_item, name='single_item'),
    url(r'^inventory/(?P<id>[0-9]*)/edit$', views.update_item, name='edit_single_item'),
    url(r'^services/', views.services, name='services'),

##orders
    url(r'^order/new', views.create_order, name='create_order'),
    url(r'^order/edit/(?P<id>[0-9]*)$', views.edit_order, name='edit_order'),
    url(r'^order/view', views.view_order, name='view_order'),
    url(r'^order', views.view_order, name='view_order'),
    url(r'^order/copy/(?P<id>[0-9]*)$', views.copy_order, name='copy_order'),
    url(r'^export/xls/$', views.export_orders, name='export_orders'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_order, name="delete_order"),

##Search
    # url(r'^order/search', SearchListView.as_view(), name='Search'),

##email
    url(r'^(?P<id>[0-9]*)/email$', views.email_form, name='email'),

##sign-out
    url(r'^signout', views.current_sign_outs, name='signout'),

#add link to dump to Resource Matrix here


#Admin Interface
#	url(r'^admin_dashboard/$*', 'store_views.admin_dashboard', name = 'admin_dashboard'),
#	url(r'^order_delete', 'store_views.delete_order', name = 'delete_order')"""

#services
#	url(r'^service/$', 'media')


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
