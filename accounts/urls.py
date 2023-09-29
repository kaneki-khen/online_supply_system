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
   path('campus_director/requester/', views.campus_director_requester,name='campusD_requester'),
   path('campus_director/notification/', views.campus_director_notification,name='campusD_notification'),
   path('campus_director/resolution/', views.campus_director_resolution,name='campusD_resolution'),
   path('campus_director/history/', views.campus_director_history,name='campusD_history'),
   path('campus_director/about/', views.campus_director_about,name='campusD_about'),
   path('supply_office/home/', views.supply_office_home,name='supply_office_home'),
   path('supply_office/notification/', views.supply_office_notification,name='supply_office_notification'),
   path('supply_office/history/', views.supply_office_history,name='supply_office_history'),
   path('supply_office/about/', views.supply_office_about,name='supply_office_about'),
   
   
]