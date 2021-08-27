from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
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
    path('message/<slug:pk>/', views.MessageCreate.as_view(), name='message_create'),
    path("message/<slug:pk>/delete", views.message_delete, name="message_delete"),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

# if settings.DEBUG:  # pragma: no cover
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
