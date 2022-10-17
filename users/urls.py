from django.urls import path
from users.views import UserCreateView, UserDetailView, reset_user_password
from users.routers import router


urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    path('update/<int:pk>', UserDetailView.as_view()),
    path('password/reset/confirm/<str:uid>/<str:token>/',reset_user_password, name='PasswordResetView'),
    # url(r'^reset/password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', PasswordResetView.as_view(),),
]

urlpatterns += router.urls