from django.urls import path
from .views import musician_create

urlpatterns = [
    # http://127.0.0.1:8000/exam/
    # http://127.0.0.1:8000/exam/musician/create/
    path("musician/create/", musician_create, name="musician_create"),
]
