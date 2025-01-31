from django.urls import path
from django.contrib.auth import views as auth_views

from usersapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name = 'logout'),
    path('register/', views.register, name='register'),
    path('profil/', views.profil, name='profil'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('patient_credentials/<str:username>/', views.patient_credentials, name='patient_credentials'),
    path('patient_list/', views.patient_list, name='patient_list'), 
    path('patient_infos/<int:patient_id>/', views.patient_info, name='patient_infos'),
    path('update_patient_left/<int:patient_id>/', views.update_patient_left, name='update_patient_left'),
    path('create_text/', views.create_text, name='create_text'),
    path('my-text-list/', views.my_text_list, name='my_text_list'),
    path('search-texts/', views.search_texts, name='search_texts')
]