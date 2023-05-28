from django.contrib import admin
from django.urls import path, include
from rest.views import google_calendar_init_view, google_calendar_redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include('rest.urls')),
    path('', google_calendar_init_view, name='google_permission'),  # Root URL pattern
    path('v1/calendar/init/', google_calendar_init_view, name='google_permission'),
    path('v1/calendar/redirect/', google_calendar_redirect_view, name='google_redirect'),
]

