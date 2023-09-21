from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot, name='forgot'),
   path('login/',views.login, name='login'),
<<<<<<< HEAD
   path('about/',views.about, name='about'),
=======
   path('history/',views.history, name='history'),
>>>>>>> 2ddecdc6c65721b5b3f5d0a9f1c5fc325cfd571d
]