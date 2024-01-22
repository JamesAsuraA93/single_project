from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    # path('<int:display_1_item_id>', views.display_1_item, name='display_1_item'),
]
