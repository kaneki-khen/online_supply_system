from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester, name='requester'),
   path('products/',views.products, name='products'),
   path('status/',views.status, name='status'),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot, name='forgot'),
   path('reset/',views.reset, name='reset'),
   path('login/',views.login, name='login'),
   path('notif/',views.notification, name='notification'),
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('about/',views.about, name='about'),
   path('history/',views.history, name='history'),
   path('profile/',views.profile, name='profile'),
   path('director_requester', views.director_requester,name='director_requester'),
   path('cash/',views.cash, name='cash'),
   path('drequester/', views.drequester,name='drequester'),
   path('dnotification/', views.dnotification,name='dnotification'),
   path('dresolution/', views.dresolution,name='dresolution'),
]