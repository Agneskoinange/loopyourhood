from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app import views as hood_views
from users import views as user_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('accounts/register/',user_views.register_user,name='register_user'),
    path('accounts/login',user_views.user_login,name='user_login'),
    path('logout/',user_views.user_logout, name='user_logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django_registration.backends.one_step.urls')),
    # path('api-token-auth/', obtain_auth_token),
    # path("users/", include("users.urls"))
]