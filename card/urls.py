"""
URL configuration for card project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from card import settings
from card_personnel import views

app_name = 'card_personnel'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('', views.personel_list, name='personel_list'),
    path('personel_detail/<int:id>/', views.personel_detail, name='personel_detail'),

    path('personel_create/', views.personel_create, name='personel_create'),
    path('personel_delete/<int:id>/', views.personel_delete, name='personel_delete'),
    path('personel_edit/<int:id>/', views.personel_edit, name='personel_edit'),

    path('phone_create/<int:id>/', views.phone_create, name='phone_create'),
    path('phone_delete/<int:id>/<int:phone_id>/', views.phone_delete, name='phone_delete'),
    path('phone_edit/<int:phone_id>/', views.phone_edit, name='phone_edit'),

    path('work_create/<int:id>/', views.work_create, name='work_create'),
    path('work_delete/<int:id>/<int:work_id>/', views.work_delete, name='work_delete'),
    path('work_edit/<int:work_id>/', views.work_edit, name='work_edit'),

    path('education_create/<int:id>/', views.education_create, name='education_create'),
    path('education_delete/<int:id>/<int:education_id>/', views.education_delete, name='education_delete'),
    path('education_edit/<int:education_id>/', views.education_edit, name='education_edit'),

    path('language_skill_create/<int:id>/', views.language_skill_create, name='language_skill_create'),
    path('language_skill_delete/<int:id>/<int:language_skill_id>/', views.language_skill_delete, name='language_skill_delete'),
    path('language_skill_edit/<int:language_skill_id>/', views.language_skill_edit, name='language_skill_edit'),

    path('family_create/<int:id>/', views.family_create, name='family_create'),
    path('family_delete/<int:id>/<int:family_id>/', views.family_delete, name='family_delete'),
    path('family_edit/<int:family_id>/', views.family_edit, name='family_edit'),

    path('spravka/<int:id>', views.spravka, name='spravka'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
