from django.urls import path
from app6.views import newpassword,SignIn, Home, Forget, Otp,Singup, Rough, HomePage, Home1, Admindash,admin
# , Display
# Home_page, Login,

urlpatterns = [
    # path('index/', Index),
    # path('', Index),
    path('Rough/', Rough,name='rough'),
    path('HomePage/', HomePage,name='homepage'),
    path('Home/', Home,name='home'),
    path('Home1/', Home1,name='home1'),
    path('admin/',admin,name="admin"),
    path('Admindash/', Admindash,name='admindash'),
    path('newpassword/', newpassword,name='newpassword'),
    path('Forget/', Forget,name='Forget'),
    path('Otp/', Otp,name='Otp'),
    path('SignIn/', SignIn,name='sign'),
    path('Signup/', Singup,name='signup'),
    # path('',Display),
]