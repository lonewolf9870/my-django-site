from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("events/",views.events,name="events"),
    path('register/',views.register_event,name="register_event"),
    path("success/",views.success_page,name="success_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)