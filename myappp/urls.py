from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import ProfileViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router = DefaultRouter()
router.register('profiles',ProfileViewSet)
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('saveprofile/',views.save_profile,name='save_profile'),
    path('<int:id>/',views.resume,name='resume'),
    path('download/<int:id>/',views.download_resume,name='download_resume'),
    path('edit/<int:id>/',views.edit_profile,name='edit_profile'),
    path('delete/<int:id>/',views.delete_profile,name='delete_profile'),
    path('signup/',views.signup,name='signup'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(),name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
]