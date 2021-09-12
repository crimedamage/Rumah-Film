"""rm_shits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from film.views import get_load_data,RumahFilm,get_link_data,RumahFilm_get,list_link
#from film.admin import RmFilm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin3/data/<int:jumlah>/', get_load_data.page_ad),
    path('admin3/data/link/', get_link_data.check_link),
    path('api/Film_API/<str:link>/<str:data>/<str:key>', RumahFilm.Film_API),
    # path('api/Film_API/detail/<str:data>/<str:key>', RumahFilm.Film_API),
    # path('api/detail/<int:id>', RumahFilm_get.get_details),
    path('api/list_link',list_link)
]
