from django.urls import path

from account import views
from account.views import ProductUpdateView, ProductDetailView, ProductListView, ProductDeleteView

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('task/', ProductListView.as_view(), name='task'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete')
]
