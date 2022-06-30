from . import views
from django.urls import path
urlpatterns = [
    path('', views.ProductView.as_view(), name='main'),
    path('filter/', views.FilterProductView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('json_filter', views.FilterJsonProductView.as_view(), name='json_filter'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_url'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("purchase/<int:pk>/", views.AddPurchase.as_view(), name='add_purchase'),
    path("salesman/<str:slug>/", views.SalesmanView.as_view(), name='salesman_detail'),
]