from django.urls import path
from myapp import views
urlpatterns = [
   # path('',views.indexfunction,name="index"),
    path('user',views.userfunction,name="user"),
    path('guest',views.guestfunction,name="user1"),
    path('user/<int:id>',views.userfunction1,name="user_1"),
    path('guest/<int:id>',views.guestfunction1,name="guest_1"),
    path('calcadd/<int:a>/<int:b>',views.addfunction,name="add"),
    path('calcsub/<int:a>/<int:b>',views.subfunction,name="sub"),
    path('calc/<str:name>',views.strfunction,name="str"),
    path('calc/<str:name>/<int:id>',views.str1function,name="str1"),
    path('calc/<int:id>*<int:id>',views.calcmul,name="mul_calc"),
    #path('myappindex/',views.appindexfunction,name="p_index"),
    #path('myappindex/cus/',views.contact,name="contact"),
    path('index',views.index,name="index"),
    #path('adminpage',views.adminpage,name="admin"),
    #path('userpage',views.userpage,name="user"),
    path('adminlogin',views.adminlogin,name="admin_login"),
    path('userlogin',views.userlogin,name="user_login"),
    path('userreg',views.userreg,name="user_reg"),
    path('contactpage',views.contactpage,name="contact_page"),
    path('checkadmin',views.checkadmin,name="checkadmin"),
]
