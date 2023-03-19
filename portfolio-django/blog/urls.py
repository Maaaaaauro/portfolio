from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views


urlpatterns = [ 
    path('', views.project_list),
    path('<int:project_id>/', views.project_detail),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)