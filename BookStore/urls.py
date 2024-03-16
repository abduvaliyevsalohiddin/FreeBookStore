from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )

schema_view = get_schema_view(
    openapi.Info(
        title="Book Store API",
        default_version='v1',
        description="Test book store API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('bookapp.urls')),
    path('upload/', include('uploadapp.urls')),
    path('user/', include('userapp.urls')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

