from django.urls import path
from users.views import UserCreateView, UserDetailView
from users.routers import router


urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    path('update/<int:pk>', UserDetailView.as_view()),
]
# urlpatterns += router.urls