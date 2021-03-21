from django.urls import path
from tempapp import views
urlpatterns =[
    path('tuser',views.tuserfunction,name="tuser"),
    path('tuser1',views.tuser1function,name="tuser1"),
    path('tuser2',views.tuser2function,name="tuser2"),
    path('tuser3',views.tuser3function,name='tuser3'),
]