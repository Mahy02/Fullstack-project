from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views as match_views

urlpatterns = [
    path('', views.home, name='fifa-home'),    #we are gonna want to include this in main urls outside
    path('about/', views.about, name='fifa-about'), 
    path('viewmatches/', views.matches, name='fifa-viewmatches'),
    path('viewmatches/reservation/', views.reservation, name='fifa-reserve'),
    path('viewmatches/reservation/payment/', views.payment, name='fifa-payment'),
    path('viewmatches/reservation/payment/confirm/', views.confirm, name='fifa-confirm_payment'),
    path('mymatches/', views.mymatches, name='fifa-my_matches'),
    path('mymatches/delete/', views.delete_reserve, name='delete'),
]

urlpatterns += staticfiles_urlpatterns()