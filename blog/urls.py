from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('admin', admin.site.urls),
                  path('', views.home, name='home'),
                  path('<slug:slug>/', views.postdetail, name='postdetail'),
                  path('Contact', views.cong, name='cong'),
                  path('login', views.login, name='login'),
                  path('about', views.about, name='about'),
                   path('services', views.services, name='services'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
