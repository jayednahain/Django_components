from django.shortcuts import render

def del_cookie_fun(request):
   return render(request,'set_cookie.html')