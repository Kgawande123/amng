from django.urls import  path
from .views import *
urlpatterns = [
    path("vv/",vview),
    path("sv/",sview),
    path("uv/<int:pk>/",uview),
    path("dv/<int:k>/",dview),
    path("hv/",hview)
]