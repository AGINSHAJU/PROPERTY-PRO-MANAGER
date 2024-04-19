from django.shortcuts import redirect, render
from django.contrib import messages
from .models import booking, car, contact, roombooking, userRegister,payments,room

# Create your views here.
def home(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userRegister.objects.get(EmailID=current_user)
        return render(request,"home.html",{'current_user':current_user,'user':user})
    return render(request,"home.html")
def login(request):
    if request.method=='POST':
        emailid=request.POST['email']
        passw=request.POST['password']
        user=userRegister.objects.filter(EmailID=emailid,Password=passw)
        if user:
            request.session['EmailID']=emailid
            return redirect('/')
    return render(request,"login.html")
def logout(request):
    del request.session['EmailID']
    return redirect('/')
def register(request):
    if request.method=='POST':
        name=request.POST['fname']
        emailid=request.POST['email']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        gend=request.POST['gender']
        emailexists=userRegister.objects.filter(EmailID=emailid)
        nameexists=userRegister.objects.filter(Name=name)
        if emailexists:
            messages.error(request,"Email ID already registered")
        elif nameexists:
            messages.error(request,"Name already taken")
        elif passw!=cpass:
            messages.error(request,"Password does not match")
        else:
            userRegister.objects.create(Name=name,EmailID=emailid,Password=passw,CPassword=cpass,Gender=gend)
            return redirect('/')
    return render(request,"register.html")
def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['message']
        contact.objects.create(Name=name,EmailID=email,Subject=subject,Message=msg)
        return redirect('/')
    return render(request,"contact.html")
def cars(request):
    data=car.objects.all().order_by('Rate')
    return render(request,"cars.html",{'data':data})
def rooms(request):
    data=room.objects.all()
    return render(request,"rooms.html",{'data':data})
def car_detail(request,id):
    data=car.objects.get(id=id)
    return render(request,"cardetail.html",{'data':data})
def room_detail(request,id):
    data=room.objects.get(id=id)
    return render(request,"roomdetail.html",{'data':data})
def booknow(request,id):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userRegister.objects.get(EmailID=current_user)
        data=car.objects.get(id=id)
        if request.method=='POST':
            name=request.POST.get('fname')
            date=request.POST.get('pickup')
            dys=request.POST.get('days')
            proof=request.POST.get('idproof')
            carname=request.POST.get('carname')
            if dys is not None and dys.isdigit():
                try:
                    day=int(dys)
                    rate=data.Rate
                    amount=day * rate
                except ValueError:
                    pass
            
            
                nameexists=booking.objects.filter(Name=name)
                if nameexists:
                    messages.error(request,'You are already booked a car, you cant book another one without return')
                else:
                    booking.objects.create(Name=name,CarName=carname,Date=date,Days=dys,Proof=proof,Amount=amount)
                    return redirect('payment')
            else:
                pass
        return render(request,"booking.html",{'user':user,'current_user':current_user,'data':data})
    else:
        return render(request,"booking.html")
def payment(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userRegister.objects.get(EmailID=current_user)
        name=user.Name
        print(name)
        pay=booking.objects.get(Name=name)
        if request.method=='POST':
            cno=request.POST.get('cardNumber')
            exp=request.POST.get('cardExpiry')
            cv=request.POST.get('cardCVC')
            amt=request.POST.get('couponCode')
            payments.objects.create(Name=name,Card_Number=cno,Expiration=exp,CV_number=cv,Amount=amt)
            return redirect('history')
        return render(request,"payment.html",{'user':user,'current_user':current_user,'pay':pay})
    return render(request,"payment.html")
def profile(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userRegister.objects.get(EmailID=current_user)
        name1=user.Name
        bookedcar=booking.objects.filter(Name=name1)
        bookedroom=roombooking.objects.filter(Name=name1)
        if bookedcar:
            
            book=booking.objects.get(Name=name1)
            pay=payments.objects.filter(Name=name1)
            if pay:
                payt=payments.objects.get(Name=name1)
                if payt:
                    
                    return render(request,"history.html",{'user':user,'current_user':current_user,'booked':book,'payt':payt}) 
            else:
                messages.error(request,"No payments yet")
                return render(request,"history.html",{'user':user})
        if bookedroom:
            
            book=roombooking.objects.get(Name=name1)
            pay=payments.objects.filter(Name=name1)
            if pay:
                payti=payments.objects.get(Name=name1)
                if payti:
                    print(name1)
                    return render(request,"history.html",{'user':user,'current_user':current_user,'roombook':book,'payti':payti}) 
            else:
                messages.error(request,"No payments yet")
                return render(request,"history.html",{'user':user})
        else:
            messages.error(request,"No Cars booked ")
            return render(request,"history.html",{'user':user})
def roombooknow(request,id):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userRegister.objects.get(EmailID=current_user)
        data=room.objects.get(id=id)
        if request.method=='POST':
            name=request.POST.get('fname')
            date=request.POST.get('pickup')
            dys=request.POST.get('days')
            proof=request.POST.get('idproof')
            roomplace=request.POST.get('roomplace')
            if dys is not None and dys.isdigit():
                try:
                    day=int(dys)
                    rate=data.Rate
                    amount=day * rate
                except ValueError:
                    pass
            
            
                nameexists=roombooking.objects.filter(Name=name)
                if nameexists:
                    messages.error(request,'You are already booked a room, you cant book another one without vacate')
                else:
                    roombooking.objects.create(Name=name,RoomPlace=roomplace,Date=date,Days=dys,Proof=proof,Amount=amount)
                    return redirect('roompayment')
            else:
                pass
        return render(request,"roombooking.html",{'user':user,'current_user':current_user,'data':data})
    else:
        return render(request,"roombooking.html")
def roompayment(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=userRegister.objects.get(EmailID=current_user)
        name=user.Name
        print(name)
        pay=roombooking.objects.get(Name=name)
        if request.method=='POST':
            cno=request.POST.get('cardNumber')
            exp=request.POST.get('cardExpiry')
            cv=request.POST.get('cardCVC')
            amt=request.POST.get('couponCode')
            payments.objects.create(Name=name,Card_Number=cno,Expiration=exp,CV_number=cv,Amount=amt)
            return redirect('history')
        return render(request,"roompayment.html",{'user':user,'current_user':current_user,'pay':pay})
    return render(request,"roompayment.html")


def pricefilter(request):
    value = request.POST['priceFilter']
    item=request.POST['item']
    print("ITEM", item)

    if value == 'Low to High' and item == 'car':
        data=car.objects.order_by('Rate')
        item = 'car'
    elif value == 'High to Low' and item == 'car':
        data=car.objects.order_by('-Rate')
        item = 'car'
    elif value == 'Low to High' and item == 'room':
        data=room.objects.order_by('Rate')
        item = 'room'
    else:
        data=room.objects.order_by('-Rate')
        item = 'room'
    return render(request,"filterData.html",{'data':data, 'item':item})
def filterbycarname(request):
    loc=request.POST['location']
    filoc=car.objects.filter(Name=loc)
    return render(request,"cars.html",{'data':filoc})
def filterbyroomplace(request):
    loc=request.POST['location']
    filoc=room.objects.filter(Place=loc)
    return render(request,"rooms.html",{'data':filoc})

    # if item =='car':
    #     print('CAR IF')
    #     if value == 'Low to High':
    #         data=car.objects.order_by('Rate')

        
    #     else:
    #         print('ESLEsssss')
    #         data=car.objects.order_by('-Rate')
    #     return render(request,"filterData.html",{'data':data})    
    # else:
    #     print('RROM ELSE')
    #     if value == 'Low to High':
    #         data=room.objects.order_by('Rate')

        
    #     else:
    #         print('ESLEsssss')
    #         data=room.objects.order_by('-Rate')
    #     return render(request,"filterData.html",{'data':data})