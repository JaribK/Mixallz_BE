from django.urls import path
from . import views

urlpatterns = [
    path('listfeatures/', views.ListFeaturesList.as_view()),
    path('listfeatures/<int:pk>/', views.ListFeaturesDetail.as_view()),
    path('code/', views.CodeListCreateView.as_view()),
    path('code/redeem/', views.CodeRedeemView.as_view()),
]