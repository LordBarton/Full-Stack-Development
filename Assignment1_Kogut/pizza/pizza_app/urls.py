from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="home"),
   path('login/', views.user_login, name="login"),
   path('signup/', views.user_signup, name="signup"),
   path('logout/', views.user_logout, name="logout"),
   path('order/', views.order_page, name="order"),
   path('user/', views.order_list, name="user"),
   path('order/info/', views.info_page, name="info"),
   path('order/info/final_page/', views.final_page, name="final_page"),
]