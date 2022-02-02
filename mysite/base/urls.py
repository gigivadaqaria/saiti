from django.urls import path
from . import views



urlpatterns =[
    path('login/',  views.LoginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/',  views.registerPage, name="register"),
    path('', views.home, name ="home"),
    path('post/<int:pk>/',views.seemore, name="seemore"),
    path('topics/', views.topicpage, name="topicpage"),
    path('know/', views.knowpage, name="know"),
    path('cre-edit/', views.createpost, name="create-edit"),
    path('addcomment/<str:pk>', views.createcomment, name="create-comment"),
    path('addtopic/', views.createtopic, name="create-topic"),
    path('updatepost/<int:pk>/', views.updatepost, name ="edit-post"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('error/',views.error, name="error"),
]
