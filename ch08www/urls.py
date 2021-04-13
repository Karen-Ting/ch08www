from django.contrib import admin
from django.urls import path
from mysite import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<int:pid>/<str:del_pass>', views.index),
    path('list/', views.listing),
    path('post/', views.posting),
    path('contact/', views.contact),
]