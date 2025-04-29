from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import CreateUserView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('pages.urls')),
    path('api/user/register/', CreateUserView.as_view(), name='user-register'),
    path('user-auth/', include('rest_framework.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),   
    path('api/token/',TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token-refresh'),  
] 

# if settings.DEBUG:
#     import debug_toolbar

#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
    
