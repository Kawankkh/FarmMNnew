from django.contrib import admin
from django.urls import path, include
from authentication import views
urlpatterns = [
    path('homepage', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', views.signin, name='signin'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dashborad', views.dashborad, name='dashborad'),
    path('customer', views.customer, name='customer'),
    path('farmmer', views.farmmer, name='farmmer'),
    path('farmmerdetail/<int:famer_id>', views.farmmerdetail, name='farmmerdetail'),
    path('stock_item', views.stock_item, name='stock_item'),

    path('CustomerService', views.CustomerService, name='CustomerService'),
    path('BillService', views.BillService, name='BillService'),
    path('Addstockitem', views.Addstockitem, name='Addstockitem'),
    path('Editstockitem', views.Editstockitem, name='Editstockitem'),
    path('Removestockitem', views.Removestockitem, name='Removestockitem'),

    path('Editfarmmer', views.Editfarmmer, name='Editfarmmer'),
    path('Removefarmmer', views.Removefarmmer, name='Removefarmmer'),

    path('RemoveFarmLoop', views.RemoveFarmLoop, name='RemoveFarmLoop'),
    path('AddproducctToLoop', views.AddproducctToLoop, name='AddproducctToLoop'),
    path('get_products_bill', views.get_products_bill, name='get_products_bill'),
    path('RemoveproducctToLoop', views.RemoveproducctToLoop, name='RemoveproducctToLoop'),

    path('AddCustomer', views.AddCustomer, name='AddCustomer'),
    path('RemoveCustomer', views.RemoveCustomer, name='RemoveCustomer'),

    path('Addproduction', views.Addproduction, name='Addproduction'),
    path('Removeproduction', views.Removeproduction, name='Removeproduction'),
    path('get_Production_bill', views.get_Production_bill, name='get_Production_bill'),
    
    path('get_All_bill', views.get_All_bill, name='get_All_bill'),
    path('Confirmbill', views.Confirmbill, name='Confirmbill'),
    
    path('get_customer_bill', views.get_customer_bill, name='get_customer_bill'),
    path('CustomerConfirmbill', views.CustomerConfirmbill, name='CustomerConfirmbill'),
]
