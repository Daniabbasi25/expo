
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Login/', LoginPage, name="LoginPage"),
    path('Register/', RegisterUser, name="RegisterPage"),
    path('Logout/', logoutuser, name="Logout"),
    path('', home, name="Home"),
    path('EditProfile/', EditProfile, name="EditProfile"),
    path('Profile/', Profile, name="Profile"),
    path('ShareProfile/<slug:slu>', shareprofile, name="ShareProfile"),
    path('delete_link/<int:pk>', delete_link, name="delete_link"),
    path('update_link/<int:pk>', update_link, name="update_link"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
