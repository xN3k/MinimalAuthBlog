from django.urls import path
from accounts.views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name = 'signup'),
]