from django.urls import path,include
from .views import index,sucess,checkout

app_name = 'payment'
urlpatterns = [
    path ('',index, name = 'index'),
    path ('checkout/',checkout,name = 'checkout'),
    path ('sucess/', sucess, name = 'sucess')
]
