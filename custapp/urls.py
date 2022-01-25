from django.urls import path
from custapp.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]