from django.shortcuts import render

def set_cookie_fun(request):
   color = request.GET.get('color_data')
   theme =request.GET.get('theme_data')
   print(request.GET)
   response = render(request, 'set_cookie.html')
   response.set_cookie('color', color)
   response.set_cookie('theme', theme)
   response.set_cookie('name', 'nahian')
   print("cookie set complete")
   return response