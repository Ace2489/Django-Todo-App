from . import views
from django.urls import path

urlpatterns = [path('', views.getTasks, name = 'tasks'),
               path('<int:pk>',views.getTaskDetails, name = 'details'),
               path('create',views.createTask, name = 'create'),
               path('update/<int:pk>',views.updateTask, name = 'update'),
               path('delete/<int:pk>',views.deleteTask, name = 'delete'),
               path(r'search', views.searchTask, name = 'search'),
               path('logout', views.logout_user, name = 'logout'),
               path('login', views.login_page, name = 'login'),
               path('signup', views.signup, name = 'signup' ) 
            ]