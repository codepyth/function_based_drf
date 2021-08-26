from django.urls import path
from .views import productCreate, productDelete, productDetail, productUpdate

urlpatterns = [
    # path('', ProductList.as_view()),
    path('create/', productCreate),
    path('detail/<int:pk>/', productDetail),
    path('delete/<int:pk>/', productDelete),
    path('update/<int:pk>/', productUpdate),
]