from django.urls import path
from tempapp import views

urlpatterns=[
    path('index',views.index,name='index_page'),
    path('login',views.login,name='login_page'),
    #path('mgr-log-in',views.managerlogin,name='mgr-log-in_page'),
    path('mgrlogout',views.managerlogout,name='mgr-log-out_page'),
    path('check-manager',views.checkmanager,name='check-manager_page'),
    path('registered-users',views.registeredusers,name='registered-users_page'),
    path('pro-log',views.prolog,name='pro-log_page'),
    path('partner-logistics',views.partnerlogistics,name='logistic-partners_page'),
]