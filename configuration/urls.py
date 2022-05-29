"""configuration URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('country/', include('country.urls')),
    path('region/', include('region.urls')),
    path('shrine/', include('shrine.urls')),
    path('tour/', include('tour.urls')),
    path('gallery/', include('gallery.urls')),
    path('relation/', include('relation.urls')),
    path('auth/', include('auth_user.urls')),
    path('', include('language.urls')),
]
urlpatterns += doc_url

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
