from django.urls import path
from .views import Products


urlpatterns = [
    path('', Products.as_view()),
#    path('<int:pk>', ProductDetail.as_view())
   ]