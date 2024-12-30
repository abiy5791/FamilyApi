from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_blogs),
    path('<int:pk>/', views.retrieve_blog),
    path('<int:pk>/update', views.update_blog),
    path('<int:pk>/delete', views.delete_blog)

]
