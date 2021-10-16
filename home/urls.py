from django.contrib import admin
from django.urls import path, include
from home import views

# django admin header costimization
admin.site.site_header ="Login Developer"
admin.site.site_title= "Welcome to the Dashboard"
admin.site.index_title="Portfolio"

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact/', views.contact, name='contact')
]