from django.shortcuts import render, redirect
from django.views import View
from .models import FoodMenu, OrderModel, Category, DailyFood
from django.contrib.auth.models import User
from django.views.generic import ListView
from  datetime import date
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'food/base.html')


            
class OrderListView(ListView):
    model = OrderModel
    template_name = 'users/ordered_list.html'
        
def OrderList(request):
    
    if request.method=='POST' and 'search' in request.POST:
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = OrderModel.objects.filter(date__gte=fromdate,date__lte=todate)   
        context = {
            'searchresult': searchresult,
        }
        return render(request, 'users/ordered_list.html', context)

    elif request.method=='POST' and 'Export' in request.POST:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=ordered_list1.csv'
        
        fromdate1 = request.POST.get('fromdate')
        todate1 = request.POST.get('todate')
        datat = OrderModel.objects.filter(date__gte=fromdate1,date__lte=todate1)
        #datat = OrderModel.objects.raw('select employee_id, id ,price, date, created_on from food_ordermodel where date between "'+fromdate1+'" and "'+todate1+'"') 
        writer = csv.writer(response)
        writer.writerow(['Name', 'Items', 'Price', 'Date'])

        for y in datat:  
            writer.writerow([y.employee, [i.name for i in y.items.all()],  y.price, y.date])
        return response
    else:
        displaydata = OrderModel.objects.all()
        context = {
            'displaydata': displaydata
        }
        return render(request, 'users/ordered_list.html', context)

# class Profile(View):
#     def get(self, request, *args, **kwargs):
#         current_user = request.user
#         useri = OrderModel.objects.filter(employee__username__contains=current_user)  
#         context = {
#             'useri': useri,
#         }
    
#         return render(request, 'users/profile.html', context)

def UploadFile(request):
    useri = OrderModel.objects.filter(employee__username__contains=request.user)
    if request.method == 'POST':
                
        obj = OrderModel.objects.get(pk=1)
        obj.fatura = request.FILES['fatura']
        obj.save()
        messages.success(request, "product saved")
        return redirect('/')
    context = {
            'useri': useri,
        }        
    return render(request, 'users/profile.html', context)        

class Order(View):
    def get(self, request, *args, **kwargs):
        menuja = DailyFood.objects.all()
        for menu in menuja:
            if menu.date != date.today():
                menu.delete()

        context = { 
            'menu': menuja,
        }
        if not menuja:
               return render(request, 'food/no_food_yet.html')
        else:       
            return render(request, 'food/order.html', context)


    def post(self, request, *args, **kwargs):
            order_items = {
                'items': []
            }

            items = request.POST.getlist('items[]')
            for item in items:     
                menu_item = FoodMenu.objects.get(pk__contains=int(item))
                item_data = {
                    'id': menu_item.pk,
                    'name': menu_item.name,
                    'price': menu_item.price
                }

                order_items['items'].append(item_data)

                price = 0
                item_ids = []


            for item in order_items['items']:
                price += item['price']   
                item_ids.append(item['id'])

            punonjesi = OrderModel.objects.filter(employee__username__contains=request.user)
        
            for x in punonjesi:
                if x.date == date.today(): 
                    return render(request, 'food/ordered_today.html')

            if price > 5:
                return render(request, 'food/order_notacepted.html')
            else:  
            
                order = OrderModel.objects.create(price=price, employee=request.user)  
                order.items.add(*item_ids)
                context = {
                    'items': order_items['items'],
                    'price': price,
                }
                return render(request, 'food/order_confirmation.html', context)
#for category in Category.objects.all(): context[category.name] = FoodMenu.objects.filter(categroy__name__contains='category.name')
