from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Matches
from .models import Tickets
from .models import Stadiums
from .models import Seats
from json import dumps
from django.contrib.auth.models import User   #user table
from django.contrib import messages
#from django.http import HttpResponse
# Create your views here.


#views handle the logic

#the sec arg of render takes the template name we want to render
#the third arg takes any parameters we want to pass to the views =======>we can get sth from database and want to show it on frontend so we pass this to templates
#we have a variable or a list that is gonna be passed as thrid ard ==> this var or list has a doctionary where it must have a key: value (from daravase)
#where key is the thing used in templates to access everything

def home(request):  #it should return the html for home page
    context={
        'matches': Matches.objects.all(),
        'tickets': Tickets.objects.all(),
        'stadiums': Stadiums.objects.all()
    }
    #dataJSON = dumps(context)
    return render(request, 'FiFa/home.html', context )

def about(request):   #should retyrn html for it
    context={
        'matches': Matches.objects.all(),
        'tickets': Tickets.objects.all(),
        'stadiums': Stadiums.objects.all()
        }
   # dataJSON = dumps(context)
    return  render(request, 'FiFa/about.html',  context)

def matches(request):
    if request.method=='POST':
            mat=request.POST['btn']
            # print(request.POST['btn'])
            dict={
                'mat':mat
            }
            return redirect('fifa-reserve',param=dict)
            #return  render(request, 'FiFa/reserve.html',  dict)
            # return reservation(request=request,param=mat)
    context={
        'matches': Matches.objects.all(),
        'tickets': Tickets.objects.all(),
        'stadiums': Stadiums.objects.all()
        }
   
    return  render(request, 'FiFa/viewmatches.html',  context)


def reservation(request):
    if request.method=='POST':
        mat=request.POST['btn']
        # print(request.POST['btn'])
        m =Matches.objects.filter(id=mat).values("venue")
        ven=m.first()['venue']
        seats=Tickets.objects.filter(match=mat).values("ticket_seat").all()
        temp=[]
        for dict1 in seats:
            temp.append(dict1['ticket_seat'])
       

    # print("resevre called")
    # if request.method=='POST':
    #         messages.success(request, f'Your seats have been reserved!')
    #         return redirect('fifa-reserve') 
        context={
        'match': Matches.objects.filter(id=mat),
        'tickets':temp,
         'seats': Seats.objects.filter(venue=ven)
        # 'stadiums': Stadiums.objects.all(),
        # 'mat':mat
        }
        # print(context['tickets'])
        return  render(request, 'FiFa/reserve.html',  context)
tickets_temp=[]
match_num=0
def payment(request):   #should retyrn html for it

    if request.method=='POST':
        tickets=request.POST['confirm']
        ticket_array= tickets.split(",")
        print(ticket_array)
        match_id=ticket_array.pop()

        global tickets_temp
        tickets_temp=ticket_array.copy()
        global match_num
        match_num=match_id
        print("global",tickets_temp,match_num)

     
    context={
        'tickets':ticket_array,
        'match_id':match_id
        }
    print("tickets",ticket_array)
    print("natch",match_id)
   # dataJSON = dumps(context)
    return  render(request, 'FiFa/payment.html',context)

def confirm(request):   #should retyrn html for it
    customer=request.POST['pay']
    print(customer)
    if request.method=='POST':
        for tick in tickets_temp:
            ticket = Tickets(match=Matches.objects.filter(id=int(match_num)).first(), ticket_seat=Seats.objects.filter(id=int(tick)).first(),ticket_user=User.objects.filter(id=int(customer)).first())
            ticket.save()

      
   # dataJSON = dumps(context)
    return  render(request, 'FiFa/confirm_payment.html')

dummy=0
def mymatches(request):  #it should return the html for home page
    customer=0
    if request.method=='POST':
        customer=request.POST['hello']
        global dummy
        dummy=customer
        print("I am alive",customer)
        seats=Tickets.objects.filter(ticket_user=customer)
        print(seats)
    context={
        'tickets': Tickets.objects.filter(ticket_user=customer)
    }
    #dataJSON = dumps(context)
    return render(request, 'FiFa/my_matches.html', context )

def delete_reserve(request):
    if request.method=='POST':
        num=request.POST['del']
        member = Tickets.objects.get(id=num)
        member.delete()
   
    #dataJSON = dumps(context)
    return render(request, 'FiFa/delete.html' )
    
