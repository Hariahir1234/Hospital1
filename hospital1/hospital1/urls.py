"""hospital1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('uploadpat/',views.uploadpat,name='uploadpatients'),
    path('uploaddoc/',views.uploaddoc,name='uploaddoctors'),
    path('updatepat/<int:pat_id>',views.updatepatient),
    path('deletepat/<int:pat_id>',views.deletepatient),
    path('updatedoc/<int:doc_id>',views.updatedoctor),
    path('deletedoc/<int:doc_id>',views.deletepatient),
    path('appointment/',views.appointment,name='appointmentdetail'),   
    path('uploadappoint/',views.uploadappoint,name='uploadappointments'),
    path('updateappoint/<int:appoint_id>',views.updateappointment),
    path('deleteappoint/<int:appoint_id>',views.deleteappointment),

]
