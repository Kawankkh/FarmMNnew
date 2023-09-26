from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from geeksforgeeks import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.http import JsonResponse
from datetime import datetime
from django.db import models
from .models import *
# Create your views here.
from .models import Production_Bill
def AddCustomer(request):
    if request.method == 'POST':
        print(request.POST)
        Custormer_ = Custormer()
        Custormer_.customer_name = request.POST.get('name')
        Custormer_.customer_contact = request.POST.get('tel')
        Custormer_.save()
        return redirect('customer')
    else:
        return redirect('customer')
def RemoveCustomer(request):
    if request.method == 'POST':
        print(request.POST)
        Custormer_ = Custormer.objects.get(custormer_id=request.POST.get('remove_id'))
        Custormer_.delete()
        return JsonResponse({"data":"ok"},status=200)
    else:
        return  redirect('farmmer')
def CustomerService(request):
    if request.method == 'POST':
        print(request.POST)
        Farmer.objects.create(Farmer_name =request.POST.get('farmmerName') ,Farmer_contact =request.POST.get('farmmerTel') )
        return redirect('farmmer')
    else:
        return redirect('farmmer')
def Editstockitem(request):
    if request.method == 'POST':
        print(request.POST)
        product = Product.objects.get(product_id=request.POST.get('edit_id'))
        product.product_description = request.POST.get('edit_name')
        product.product_price = request.POST.get('edit_price')
        product.save()
        return  redirect('stock_item')
    else:
        return  redirect('stock_item')
def Removestockitem(request):
    if request.method == 'POST':
        print(request.POST)
        product = Product.objects.get(product_id=request.POST.get('remove_id'))
        product.delete()
        return JsonResponse({"data":"ok"},status=200)
    else:
        return  redirect('stock_item')
def Addstockitem(request):
    if request.method == 'POST':
        print(request.POST)
        Product.objects.create(product_description =request.POST.get('Itemname') ,product_price =request.POST.get('Price') )
        return  redirect('stock_item')
    else:
        return  redirect('stock_item')
def Editfarmmer(request):
    if request.method == 'POST':
        print(request.POST)
        Farmer_ = Farmer.objects.get(Farmer_id=request.POST.get('edit_id'))
        Farmer_.Farmer_name =request.POST.get('edit_name')
        Farmer_.Farmer_contact = request.POST.get('edit_Tel')
        Farmer_.save()
        return  redirect('farmmer')
    else:
        return  redirect('farmmer')
def Removefarmmer(request):
    if request.method == 'POST':
        print(request.POST)
        Farmer_ = Farmer.objects.get(Farmer_id=request.POST.get('remove_id'))
        Farmer_.delete()
        return JsonResponse({"data":"ok"},status=200)
    else:
        return  redirect('farmmer')

def BillService(request):
    if request.method == 'POST':
        print(request.POST)
        foarmer_id = request.POST.get('famerid')
        farmer = Farmer.objects.get(Farmer_id=request.POST.get('famerid'))
        bill_op = Bill_OP()
        bill_op.Farmer = farmer  
        bill_op.billdate = request.POST.get('date') 
        bill_op.Pay_status = False  
        bill_op.save()

        print(bill_op.Bill_id)
        try:
            Exchange_ = Exchange.objects.get(Bill_OP__Farmer__Farmer_id =foarmer_id, iscomplete = False)
            product = Product.objects.get(product_id=9) 
            # bill_OP = Bill_OP.objects.get(Bill_id=bill_op.Bill_id)
            current_datetime = datetime.now()
            print(Exchange_)
            Order_Bill_ = Order_Bill()
            Order_Bill_.Product =  product
            Order_Bill_.Bill_OP = bill_op
            Order_Bill_.Qty = abs(Exchange_.price)
            Order_Bill_.Total_price = abs(Exchange_.price)
            Order_Bill_.Order_Date = current_datetime.strftime('%Y-%m-%d')
            Order_Bill_.save()
        except:
            pass
        
        
        url = f'farmmerdetail/{foarmer_id}'
        return redirect(url)
    else:
        return redirect('farmmer')
def RemoveFarmLoop(request):
    if request.method == 'POST':
        print(request.POST.get('remove_id'))
        bill_op_ = Bill_OP.objects.get(Bill_id=request.POST.get('remove_id'))
        bill_op_.delete()
        return JsonResponse({"data":"ok"},status=200)
    else:
        return  redirect('farmmer')
def AddproducctToLoop(request):
    if request.method == 'POST':
        print(request.POST)
        product = Product.objects.get(product_id=request.POST.get('Product_id')) 
        bill_OP = Bill_OP.objects.get(Bill_id=request.POST.get('Add_Bill_id'))
        Order_Bill_ = Order_Bill()
        Order_Bill_.Product =  product
        Order_Bill_.Bill_OP = bill_OP
        Order_Bill_.Qty = request.POST.get('Qty') 
        Order_Bill_.Total_price = int(request.POST.get('Qty')) * int(product.product_price)
        Order_Bill_.Order_Date = request.POST.get('Date')  
        Order_Bill_.save()
        url = f'farmmerdetail/{bill_OP.Farmer.Farmer_id}'
        return redirect(url)
    else:
        return redirect('farmmer')
def RemoveproducctToLoop(request):
    if request.method == 'POST':
        print(request.POST)
        Order_Bill_ = Order_Bill.objects.get(Order_Bill_id=request.POST.get('remove_id'))
        Order_Bill_.delete()
        return JsonResponse({"data":"ok"}, safe=False)
    else:
        return redirect('farmmer')
def get_products_bill(request):
    bill_op = int(request.GET.get('Bill_OP', None))
    print(bill_op)
    if bill_op > 0:
        try:
            # Use select_related to fetch related Product data
            order_bills = Order_Bill.objects.filter(Bill_OP__Bill_id=bill_op).select_related('Product')
            
            # Create a list to store the result
            result = []
            
            for order_bill in order_bills:
                order_info = {
                    'Order_Bill_id': order_bill.Order_Bill_id,
                    'Qty': order_bill.Qty,
                    'Total_price': order_bill.Total_price,
                    'Order_Date': order_bill.Order_Date,
                    'Product': {
                        'Product_id': order_bill.Product.product_id,
                        'Product_description': order_bill.Product.product_description,
                        'Product_price': order_bill.Product.product_price,
                    }
                }
                result.append(order_info)
            
            return JsonResponse(result, safe=False)
        except Order_Bill.DoesNotExist:
            return JsonResponse({'error': 'No matching records found'}, status=404)
    else:
        return JsonResponse({"data":"NG"}, safe=False)
def get_Production_bill(request):
    # Your view logic here
    bill_op = int(request.GET.get('Bill_OP', None))  # Replace with your desired value
    
    # Retrieve Production_Bill objects based on the 'bill_op'
    production_bills = Production_Bill.objects.filter(Bill_OP__Bill_id=bill_op)
    res = []
    for i in production_bills:
        Production_Bill_add = {
                    'Production_Bill_id': i.Production_Bill_ID,
                    'Custormer_name': i.Custormer.customer_name,
                    'Car':i.Car_driver,
                    'H_Qty': i.H_Qty,
                    'T_Qty': i.T_Qty,
                    'M_Qty': i.M_Qty,
                    'L_Qty': i.L_Qty,
                    'Production_Date': i.Production_Date,
                    
                }
        res.append(Production_Bill_add)
       
    return JsonResponse(res, safe=False)


def Addproduction(request):
    print(request.POST)
    if request.method == 'POST':
        
        Production_Bill_ = Production_Bill()
        Bill_OP_ = Bill_OP.objects.get(Bill_id = request.POST.get('Add_Bill_id_production'))
        Custormer_ = Custormer.objects.get(custormer_id = request.POST.get('custormer_id'))
        Production_Bill_.Custormer = Custormer_
        Production_Bill_.Bill_OP = Bill_OP_
        Production_Bill_.Car_driver = request.POST.get('car')
        Production_Bill_.H_Qty = request.POST.get('H_Qty')
        Production_Bill_.T_Qty = request.POST.get('T_Qty')
        Production_Bill_.M_Qty = request.POST.get('M_Qty')
        Production_Bill_.L_Qty = request.POST.get('L_Qty')
        Production_Bill_.Pay_status = False
        Production_Bill_.Production_Date  =request.POST.get('date')
        Production_Bill_.save()
        url = f'farmmerdetail/{Bill_OP_.Farmer.Farmer_id}'
        return redirect(url)
def Removeproduction(request):
    if request.method == 'POST':
        print(request.POST)
        Production_Bill_ = Production_Bill.objects.get(Production_Bill_ID=request.POST.get('remove_id'))
        Production_Bill_.delete()
        return JsonResponse({"data":"ok"}, safe=False)
    else:
        return redirect('farmmer')

def get_All_bill(request):
    # Your view logic here
    bill_op = int(request.GET.get('Bill_OP', None))  # Replace with your desired value
    
    # Retrieve Production_Bill objects based on the 'bill_op'
    production_bills = Production_Bill.objects.filter(Bill_OP__Bill_id=bill_op)
    return_ = dict()
    res=[]
    sum_H_Qty = 0
    sum_T_Qty = 0
    sum_M_Qty = 0
    sum_L_Qty = 0
    Price_H = 0
    Price_T = 0
    Price_M= 0
    Price_L = 0
    for i in production_bills:
        sum_H_Qty = sum_H_Qty+i.H_Qty
        sum_T_Qty = sum_T_Qty+i.T_Qty
        sum_M_Qty = sum_M_Qty+i.M_Qty
        sum_L_Qty = sum_L_Qty+i.L_Qty
        Price_H = i.H_Price
        Price_T = i.T_Price
        Price_M = i.M_Price
        Price_L = i.L_Price
        
    Production_Bill_add = {
                
                'H_Qty': sum_H_Qty,
                'T_Qty': sum_T_Qty,
                'M_Qty': sum_M_Qty,
                'L_Qty': sum_L_Qty,
                'H_Price': Price_H,
                'T_Price': Price_T,
                'M_Price': Price_M,
                'L_Price': Price_L,

            }
    
    res.append(Production_Bill_add)
    return_['list_Production'] = res
    order_bills = Order_Bill.objects.filter(Bill_OP__Bill_id=bill_op).select_related('Product')
    
    # Create a list to store the result
    result = []


    for order_bill in order_bills:
        order_info = {
            'Order_Bill_id': order_bill.Order_Bill_id,
            'Qty': order_bill.Qty,
            'Total_price': order_bill.Total_price,
            'Order_Date': order_bill.Order_Date,
            'Product': {
                'Product_id': order_bill.Product.product_id,
                'Product_description': order_bill.Product.product_description,
                'Product_price': order_bill.Product.product_price,
            }
        }
        result.append(order_info)
   
    return_['list_expent'] = result
    
    Bill  = Bill_OP.objects.get(Bill_id=bill_op)

    return_['bill_status'] = Bill.Pay_status
    return JsonResponse(return_, safe=False)
def Confirmbill(request):
    if request.method == 'POST':
        print(request.POST)
        bill_OP = Bill_OP.objects.get(Bill_id=request.POST.get('Confirm_Bill_id'))

        bill_OP.Pay_status = True  
        bill_OP.save()
        Production_Bill_ = Production_Bill.objects.filter(Bill_OP__Bill_id=request.POST.get('Confirm_Bill_id'))
        for i in Production_Bill_:
            i.H_Price = request.POST.get('price_H')
            i.T_Price = request.POST.get('price_T')
            i.M_Price = request.POST.get('price_M')
            i.L_Price = request.POST.get('price_L')
            i.save()
        url = f'farmmerdetail/{bill_OP.Farmer.Farmer_id}'
        get_bill = Exchange.objects.filter(Bill_OP__Farmer__Farmer_id = bill_OP.Farmer.Farmer_id, iscomplete= False)
        print(get_bill)
        for i in get_bill:
            i.iscomplete = True
            i.save()
        if int(request.POST.get('cost')) < 0 :
            Exchange_ = Exchange()
            Exchange_.Bill_OP = bill_OP
            Exchange_.price = int(request.POST.get('cost'))
            Exchange_.iscomplete = False
            Exchange_.save()
        return redirect(url)
    else:
        return redirect('farmmer')

def get_customer_bill(request):
    print(request.GET)
    Production_Bill_ID = int(request.GET.get('Production_Bill_ID', None))  # Replace with your desired value
    return_ = dict()
    # Retrieve Production_Bill objects based on the 'bill_op'
    production_bills = Production_Bill.objects.get(Production_Bill_ID=Production_Bill_ID)
    production_bills_list = Production_Bill.objects.filter(Production_Bill_ID=Production_Bill_ID).values()
    return_['list_Production'] =list(production_bills_list)
    return_['cus'] = production_bills.Custormer.customer_name
    return_['tel'] = production_bills.Custormer.customer_contact

    return JsonResponse(return_, safe=False)
def CustomerConfirmbill(request):
    if request.method == 'POST':
        print(request.POST)
        Production_Bill_ = Production_Bill.objects.get(Production_Bill_ID=request.POST.get('Production_Bill_ID'))

        Production_Bill_.Pay_status = True  
        Production_Bill_.H_Price_c =request.POST.get('price_H')
        Production_Bill_.T_Price_c =request.POST.get('price_T')
        Production_Bill_.M_Price_c =request.POST.get('price_M')
        Production_Bill_.L_Price_c =request.POST.get('price_L')
        Production_Bill_.save()
    return redirect("customer")
def home(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    fname = request.user.first_name
    return render(request, "authentication/index.html",{"fname":fname})
def farmmer(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    list_famer = Farmer.objects.all()
    print(list_famer)
    return render(request, "authentication/farmmer.html",{"famer":list_famer})
def farmmerdetail(request, famer_id):
    if request.user.is_authenticated:
        print(famer_id)
        list_bill = Bill_OP.objects.filter(Farmer__Farmer_id=famer_id)
        list_product = Product.objects.all()
        list_customer = Custormer.objects.all()
        famer = Farmer.objects.get(Farmer_id=famer_id)
        print(famer)
    else:
        return redirect('signin')
    return render(request, "authentication/farmmerdetail.html",{'list_bill':list_bill,'famer':famer,'list_product':list_product,'list_customer':list_customer})
def customer(request):
    if request.user.is_authenticated:
        list_cutomer = Custormer.objects.all()
        Production_Bill_ = Production_Bill.objects.all()
    else:
        return redirect('signin')
    return render(request, "authentication/customer.html",{'list_cutomer':list_cutomer,'Production_Bill_':Production_Bill_})
def stock_item(request):
    if request.user.is_authenticated:
        
        list_item = Product.objects.all()
    else:
        return redirect('signin')
    
    return render(request, "authentication/stock_item.html",{'data':list_item})
def dashborad(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('signin')
    return render(request, "authentication/dashborad.html")
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to GFG- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
        
        
    return render(request, "authentication/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            print(fname)
            return redirect('home')
            return render(request, "authentication/index.html",{"fname":fname})
        
        else:
            messages.error(request, "Username หรือ Password ไม่ถูกต้อง")
            return redirect('signin')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "authentication/signin.html")


def signout(request):
    print(request)
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')