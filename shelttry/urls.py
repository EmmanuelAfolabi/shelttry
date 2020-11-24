from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('search', views.search, name='search'),
    path('abou', views.about, name='about'),
    path('list', views.list, name='list'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('ago-iwoye', views.ago, name='ago'),
    path('ijebu-igbo', views.ijebu, name='ijebu'),
    path('oru', views.oru, name='oru'),
    #path('delete/<int:id>', views.delete, name='delete'),
    path('success', views.success, name='success'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, {}, name='edit'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('houses', views.dashboardhouses, name='houses'),
    path('login', views.user_log, name='login'),
    path('policy', views.policy, name='policy'),
    path('privacy', views.privacy, name='privacy'),
    path('register', views.register, name='signup'),
    path('logout', views.logoutUser, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('detail', views.d, name='detail'),


]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
