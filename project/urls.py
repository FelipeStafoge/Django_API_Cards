from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls'), name='index'),
    path('take_a_card/', include('home.urls'), name='take_a_card'),
    path('admin/', admin.site.urls),
]
