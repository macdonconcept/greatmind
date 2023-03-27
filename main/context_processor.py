from .models import *

def dropdown(request):
     info= AppInfo.objects.get(pk=1)
     fcat = Category.objects.all()


     context = {
          'info': info,
          'fcat': fcat,
          
     }

     return context

def cartcount(request):
     count= Cart.objects.filter(user__username= request.user.username, paid=False)

     itemcount=0

     for item in count:
          itemcount += item.quantity

     context = {
          'itemcount': itemcount
     }

     return context
     