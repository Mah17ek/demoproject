from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import HomePage,Admin_reg
# Create your views here.
import smtplib
import email.message
from smtplib import SMTP 

import random
def Index(request):
    return HttpResponse('<h1>Hello python class</h1>')

def Rough(request):
    return render(request,'login_details/Rough.html') 

def Home(request):
    return render(request,'login_details/Home.html') 

def Forget(request):
    if request.POST:
        em = request.POST['email23']
        no = request.POST['numbar23']
        try:
            valid = HomePage.objects.get(Email=em)
            if int(valid.phone) == int(no):
                print(em)
                request.session['useremail'] = em
                
                numbers = [1,2,3,4,5,6,7,8,9,0]
                num = ""
                for i in range(4):
                    num += str(random.choice(numbers))
                
                num = int(num)
                print(num)
                
                # ============== Email ==============
                
                sender_email = "devarshmistry25@gmail.com"  
                sender_pass = "dev@rsh2602"
                receiver_email = em

                server = smtplib.SMTP('smtp.gmail.com',587)

                your_message =  "This Is Your OTP Number = "+str(num)

                print(your_message)

                msg = email.message.Message()
                msg['Subject'] = "Your OTP From Advance Billing System"
                msg['From'] = sender_email
                msg['To'] = receiver_email
                password = sender_pass
                msg.add_header('Content-Type','text/html')
                msg.set_payload(your_message)

                server.starttls()
                server.login(msg['From'],password)
                server.sendmail(msg['From'],msg['To'],msg.as_string())
                
                # ============== End Email ===========
                
                request.session['otp'] = num
                return redirect('Otp')
                
            else:
                print("No Contact No...")
            
        except:
            return render(request,'login_details/Forget.html')        
        
    return render(request,'login_details/Forget.html')

def Otp(request):
    if 'otp' in request.session.keys():
        if request.POST:
            ot = request.POST['otp']
            if str(ot) == str(request.session['otp']):
                del request.session['otp']
                return redirect('newpassword')
            else:
                return render(request,'login_details/Forget.html')  
        return render(request,'Otp.html')
    else:
        return render(request,'login_details/Forget.html')        

def newpassword(request):
    if request.session.has_key('useremail'):
        if request.POST:
            pass_1 = request.POST['password1']
            pass_2 = request.POST['password2']
            
            if pass_1 == pass_2:
                valid = HomePage.objects.get(Email=request.session['useremail'])
                valid.password = pass_2
                valid.save()
                del request.session['useremail']
                return redirect('sign')
            else:
                return HttpResponse("<h2><a href=''>Passwords Are Not Same ...</a></h2>")
        return render(request,'login_details/newpassword.html')
    
    return render(request,'login_details/newpassword.html')


def Home1(request):
    return render(request,'login_details/Home1.html') 

def Admindash(request):
    return render(request,'login_details/Admindash.html') 

# def Display(request):
#     data = HomePage.objects.all()
#     return render(request,'home.html',{'data':data})

def SignIn(request):
    if request.POST:
        uname  = request.POST['username']
        Email = request.POST['email']
        psw = request.POST['password2']
        cpassword   = request.POST.get('confpassword')
        # dateob = request.POST['dob']
        # join_time = request.POST['join_time']
        
        print(uname ,Email,cpassword, psw)

        obj = HomePage()
        obj.name = uname
        obj.Email =  Email
        obj.password = psw
        obj.cpassword  = cpassword 
        obj.save()
        # obj.dob = dateob
        # obj.join_time =join_time

    return render(request,'login_details/SignIn.html')
def admin(request):
    if request.POST:
        uname  = request.POST['username']
        Email = request.POST['email']
        psw = request.POST['password2']
        cpassword   = request.POST.get('confpassword')
        # dateob = request.POST['dob']
        # join_time = request.POST['join_time']
        
        print(uname ,Email,cpassword, psw)

        obj = Admin_reg()
        obj.aname = uname
        obj.aEmail =  Email
        obj.apassword = psw
        obj.acpassword  = cpassword 
        obj.save()
        # obj.dob = dateob
        # obj.join_time =join_time

    return render(request,'login_details/SignIn.html')
   
def Singup(request):
    if request.method == "POST":
        try:
            print(request.POST.get('usname'))
            print(request.POST['password2'])
            m = HomePage.objects.get(name = request.POST.get('usname'))
            if m.password == request.POST['password2']:
                print(m.Email)
                request.session['User'] = m.name
                return redirect('home1')
            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password</a></h2>")
        except:
            h= Admin_reg.objects.get(aname = request.POST.get('usname'))
            if h.apassword == request.POST['password2']:
                        print(h.aEmail)
                        request.session['User'] = h.aname
                        return redirect('home1')
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'login_details/SignIn.html')

# def Dashboard(request):
#     if 'User' in request.session.keys();
#     data = request.session['User']
#     user= UserData.objects.get(email = data)
#     prods = UserProducts.objectss.filter(users = user)
#     return 

# def otpcheck(request):
#     if request.session.has_key('otp'):
#         if request.POST:
#             otp = request.POST['otp']
#             if int(request.session['otp']) == int(otp):
#                 del request.session['otp']
#                 return redirect('newpassword')
#             else:
#                 return HttpResponse("<h2><a href=""> You Have Entered Wrong OTP </a></h2>")
#         else:
#             return redirect('forgotpass')
#     return redirect('login')

