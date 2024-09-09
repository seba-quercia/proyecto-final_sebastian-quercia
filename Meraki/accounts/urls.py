from django.urls import path
from .views import SignUpView, LoginView, LogoutView, AccountSettingsView, MessageView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account-settings/', AccountSettingsView.as_view(), name='account_settings'),
    path('messages/', MessageView.as_view(), name='messages'),
    path('messages/<int:message_id>/', MessageView.as_view(), name='message_detail'),
]
