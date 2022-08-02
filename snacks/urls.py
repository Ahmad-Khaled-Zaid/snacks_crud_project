from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', SnackListView.as_view(), name='list_view'),
    path('details/<int:pk>', SnackDetailView.as_view(), name='details_view'),
    path('create/', SnackCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name='delete_view')
]
