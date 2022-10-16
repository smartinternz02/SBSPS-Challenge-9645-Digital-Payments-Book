from django.urls import path
from account.views import *
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('purchasehistory/', GetPurchaseHistory.as_view(), name='purchase-history'),
    path('carthistory/', CartPurchaseHistory.as_view(), name='cart-history'),
    path('paymenthistory/',PaymentHistory.as_view(),name='payment-history'),
    path('cart/', GetCartHistory.as_view(), name='purchase-history'),
    path('addproduct/',Addproduct.as_view(),name="Addproduct"),
    path('addtocart/',GenerateProductHistory.as_view(),name="add-to-cart"),
    path('user-purchase-history/',GetPurchaseHistoryByUser.as_view(),name="user-purchase-history"),
    path('update-status/',UpdatePaymentStatus.as_view(),name="user-status")
]