from django.urls import path,include
from . import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),
    # path('reset_password/', include('django_rest_passwordreset.urls', namespace='reset_password')),
]