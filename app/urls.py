
from django.urls import path
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
   
    path('post/update/<int:pk>/', views.update_post, name='update_data'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)