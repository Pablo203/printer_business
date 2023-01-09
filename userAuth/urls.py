from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homePage'),
    path('login/', LoginView.as_view(), name='loginView'),
    path('register/', RegisterView.as_view(), name='registerView'),
    path('recover/', RecoverPassword.as_view(), name='recoverPass'),
    path('forgot/', ForgotPassword.as_view(), name="forgotPass"),

    path('login/execute/', loginExecute, name='loginExecute'),
    path('register/execute/', registerExecute, name='registerExecute'),
    path('recover/execute/', recoverExecute, name='recoverPassExecute'),
    path('forgot/execute/', forgotPassExecute, name="forgotPassExecute"),
]