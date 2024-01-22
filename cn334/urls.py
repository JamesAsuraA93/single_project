"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from ecommerce import views as ecom_views

# from django.contrib import admin
# from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', ecom_views.ecommerce_product_view, name="home"),  # index page home
    path('', include('ecommerce.urls')),
    path('admin/', admin.site.urls),
    path("ecommerce/", ecom_views.ecommerce_index_view),
    path("ecommerce/item/<item_id>", ecom_views.item_view),
    path("ecommerce/product/", ecom_views.ecommerce_product_view),
    path("ecommerce/product/<int:product_id>/",
         ecom_views.display_product_by_id),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
