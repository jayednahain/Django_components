from django.shortcuts import render

def get_cookie_fun(request):
   #showing all cokie
   if request.COOKIES:
      print("hellow")
      print(request.COOKIES)

      #get sepcific cookie value
      cookie_data=request.COOKIES['name']

      #getting value using get
      cookie_data = request.COOKIES.get('name')



      return render(request,'get_cookie.html',{'cookie_data':cookie_data})
   else:
      return render(request, 'get_cookie.html', {'cookie_data': "data deleted"})

