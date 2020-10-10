from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Id_password.urls')),
    path('travel/', include('travel.urls'))
]
