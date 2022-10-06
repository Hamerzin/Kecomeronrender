from django.urls import path
from users.views import UserCreateView
from users.customuser import *
from users.routers import router
urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    
    

]
urlpatterns += router.urls