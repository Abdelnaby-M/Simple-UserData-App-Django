from django.contrib import admin
from django.urls import path
from users.views import userView, authView, statusView


urlpatterns = [
    
    path('user', userView.as_view(), name='user'),
    path('admin/', admin.site.urls),
    path('user/token', authView.as_view(), name="authToken"),
    path('user/status', statusView.as_view(), name="statusView")
    
]
