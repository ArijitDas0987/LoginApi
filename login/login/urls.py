
from django.contrib import admin
from django.urls import path,include
from ManageUserApi.views import Get_Create_User,Retrieve_Update_Delete_User
from LoginApi.views import LoginApi



urlpatterns = [
    path('admin/', admin.site.urls),
    path('UserGetCreateApi/', Get_Create_User.as_view()),
    path('UserRetrieveUpdateDeleteApi/<int:pk>', Retrieve_Update_Delete_User.as_view()),
    path('LoginApi/', LoginApi.as_view()),   
]
