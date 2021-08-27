from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
import debug_toolbar
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '', 
        views.RoomList.as_view(), 
        name='index'
    ),
    path(
        'room-list/',
        views.RoomList.as_view(),
        name='room_list',
    ),
    path('<slug:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('<slug:pk>/message_create', views.MessageCreate.as_view(), name='message_create'),
    path('message/<int:message_id>/delete', views.message_delete, name='message_delete'),
    path('quickstart/<slug:pk>/', TemplateView.as_view(template_name='broadcast_example.html')),
    path('quickstart/send', views.send_broadcast),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)