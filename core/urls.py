from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. The new starting page becomes the main URL ('')
    path('', views.landing_view, name='landing'),
    
    # 2. The URL for "Vraj kha h"
    path('vraj-kha-h/', views.vraj_kha_h_view, name='vraj_kha_h'),
    
    # 3. The URL for the form we built earlier
    path('vrajs-new-one/', views.home_view, name='vrajs_new_one'),
]