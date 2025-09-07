from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    # CRUD
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='student_edit'),
    path('delete/<int:pk>/', views.delete_student, name='student_delete'),

]