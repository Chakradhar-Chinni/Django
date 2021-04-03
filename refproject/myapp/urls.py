from django.urls import path
from . import views

urlpatterns=[
   #path('index',views.index,name='index'),
    path('guest',views.guest,name='guest'),
    path('junk',views.junk,name='junk'),
    #path('add/<int:id>/<int:id>',views.add,name='add_calc'),
    path('calc',views.calcmul,name="mul_calc"),
    path('sub',views.sub,name='sub_calc'),

    path('home',views.home,name='home_page'),
    path('admin-login',views.adminlogin,name='admin_login_page'),
    path('user-reg',views.userregistration,name='user-reg_page'),
    path('user-login',views.userlogin,name='user-login_page'),
    path('contact-us',views.contactus,name='contact-us_page'),
    

    path('checkadmin',views.checkadmin,name="check_admin"),

    #adminhome.html urls
    path('admin-home',views.adminhome,name="admin-home_page"),
    path('view-users',views.viewusers,name="view-users_page"),
    path('admin-log-out',views.adminlogout,name="admin-log-out_page"),
]