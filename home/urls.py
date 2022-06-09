
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
    path('link/handler/', link_form_handler, name="link_form_handler"),
    path('ShareProfile/<slug:slu>', shareprofile, name="ShareProfile"),
    path('delete_link/<int:pk>', delete_link, name="delete_link"),
    path('htmx/update_link/<int:pk>/update', update_link, name="update_link"),
    path('htmx/linkform/',Create_linkform,name='linkform'),
    path('htmx/link/<pk>/',detail_link,name='linkdetail'),
    path('htmx/link/<pk>/edit/',Update_linkdata,name='updatelinkdata'),
    path('htmx/link/<pk>/delete/',delete_link,name='deletlink'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
