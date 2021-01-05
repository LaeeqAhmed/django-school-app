from django.urls import path
from .import views
urlpatterns = [
    path('Enrollment/create', views.create.as_view(), name='create'),
    path('Enrollment/', views.listView.as_view(), name='listView'),
    path('Enrollment/<pk>', views.detailView.as_view(), name='detailView'),
    path('Enrollment/update/<pk>', views.update.as_view(), name='update'),
    path('Enrollment/delete/<pk>', views.delete.as_view(), name='delete'),
]