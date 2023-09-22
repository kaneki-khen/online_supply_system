from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),
   path('register/',views.register),
   path('login/',views.login, name='login'),
   path('tracker/',views.tracker, name='tracker'),

   path('forgot/',views.forgot, name='forgot'),

   path('login/',views.login, name='login'),
   path('notif/',views.notification, name='notification'),

   path('about/',views.about, name='about'),
   
   path('history/',views.history, name='history'),
]