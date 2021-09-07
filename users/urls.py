from django.urls import path
from .views import SignUpView, GetUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>', GetUserView.as_view(), name='user_details'),
]