from django.urls import path
from . views import StudentListCreate, StudentUpdateDelete

urlpatterns = [
    path('read-create/', StudentListCreate.as_view(), name='read'),
    path('read-create/<int:pk>/', StudentUpdateDelete.as_view(), name='update'),
    
]