from django.urls import include, path
from rest_framework import routers
from .views import users,update_attendance



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users', users, name='users'),
    path('attendance/<int:id>', update_attendance, name='attendance'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]