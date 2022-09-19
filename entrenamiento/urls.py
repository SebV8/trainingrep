from django.urls import path
from entrenamiento import views

urlpatterns = [
    path('', views.training, name='training'),
    path('create_pr/', views.create_pr, name='create_pr'),
    path('update_pr/<int:id>/', views.update_pr, name='update_pr'),
    path('delete_pr/<int:id>/', views.delete_pr, name='delete_pr'),
    
    path('create_rm/', views.create_rm, name='create_rm'),
    path('update_rm/<int:id>/', views.update_rm, name='update_rm'),
    path('delete_rm/<int:id>/', views.delete_rm, name='delete_rm'),
]