from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('signup/login/', views.custom_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),  # Added trailing slash
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'),
    path('remove/', views.remove_recipe, name='remove_recipe'),
   

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

