# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Route to index view
    path('download-cv/<int:resume_id>/', views.download_cv, name='download_cv'),
    path("contact/", views.contact_form, name="contact_form"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)