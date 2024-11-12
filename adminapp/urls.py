from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('category-edit', views.categoryedit, name='category-edit'),
    path('subcategory', views.subcategory, name='subcategory'),
    path('subcategory-edit', views.subcategoryedit, name='subcategory-edit'),
    path('city', views.city, name='city'),
    path('city-edit', views.cityedit, name='city-edit'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('product', views.product, name='product'),
    path('product-edit', views.productedit, name='productedit'),
    path('feedback', views.feedback, name='feedback'),
    path('user', views.user, name='user'),
    path('payment', views.payment, name='payment'),
    path('pendingbooking', views.pendingbooking, name='pendingbooking'),
    path('completebooking', views.completebooking, name='completebooking'),
    path('cancelbooking', views.cancelbooking, name='cancelbooking'),
    path('userreport', views.userreport, name='userreport'),
    path('feedbackreport', views.feedbackreport, name='feedbackreport'),
    path('productsreport', views.productsreport, name='productssreport'),
    path('bookingreport', views.bookingreport, name='bookingreport'),
    path('generatebill', views.generatebill, name='generatebill'),
    path('discontinuerent', views.discontinuerent, name='discontinuerent'),
    path('paymentreport', views.paymentreport, name='paymentreport'),
]
   