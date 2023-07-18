from django.urls import path
import appCV.views as views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'appCV'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('languages/', views.languages, name='languages'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
