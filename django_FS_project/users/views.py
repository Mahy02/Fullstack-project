from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  #customed forms from django
from django.contrib import messages
from django.contrib.messages import success, error
from .forms import  ProfileUpdateForm, ProfileRegisterForm,UserUpdateForm
from django.contrib.auth.hashers import make_password
#UserRegisterForm
#UserRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView


#making a new instance of the form 
#we need to create a new form that inherits from user creation form


#rg3na elmessage hena lao 3mlt moshkla neshlha---------m
# Create your views here.
def signup(request):
    if request.method=='POST':
        #u_form=UserRegisterForm(request.POST)
        
        p_form=ProfileRegisterForm(request.POST)
        #if u_form.is_valid() and p_form.is_valid():
        if  p_form.is_valid():
            
            username1=request.POST['username']
            ps=request.POST['password1']
            email1=request.POST['email']
            user1=User(username=username1,password=make_password(ps),email=email1)
            user1.save()
            birth=request.POST['birthdate']
            first=request.POST['first_name']
            last=request.POST['last_name']
            gender=request.POST['gender']
            nation=request.POST['nationality']
            print("hello signup here")
            #u_form.save()
            profile = Profile(user=user1,first_name=first,last_name=last,birth_date=birth,gender=gender,nationality=nation)
            profile.save()
            
            #user_group = p_form.cleaned_data.get('user_type')
            #profile.user_type = user_group
            # profile.save()
            
            #profile = Profile.objects.create(user=user, first_name=p_form.cleaned_data['first_name'], last_name=p_form.cleaned_data['last_name'], gender=p_form.cleaned_data['gender'], birth_date=p_form.cleaned_data['birthdate'], nationality=p_form.cleaned_data['nationality'])
            #profile.save()
            
            #username=form.cleaned_data.get('username') #grab username subbited
            #a flash message to show we recieved a valid data
			#flash messages send one time alerts to a template that will only just be displayer once then disappear on next request
            messages.success(request, f'Your account is now created! you are now able to login.')
            #Account created for {username} !
            return redirect('login')  #name of blog home page //in our case will be redirected to Matches reservation page
    else:
        #u_form=UserRegisterForm()
        p_form=ProfileRegisterForm()
    
    context= {
        #'uform': u_form,
        'p_form': p_form
        }
    
    return render(request, 'users/signup.html', context)
#end signup

#login-logout had class based views



#mahy edited profile here on 2/1######################

# #updating
# @login_required
# def profile(request):

#      #new things: ############################
#     user_not=User.objects.filter(id=request.user.id).first()   #for the instance of the user
#     user = Profile.objects.get(user=user_not)    #for profile intance for this current user
#     #################################################

#     if request.method=='POST':

#         #new things: ############################
        

#         u_form=UserUpdateForm(request.POST, instance= user_not )
#         p_form=ProfileRegisterForm(request.POST, instance= user)

#         #######################################################


#         #u_form=UserUpdateForm(request.POST, instance= request.user)
#         #p_form=ProfileRegisterForm(request.POST, instance= request.user.profile)
#         #p_form= ProfileUpdateForm(request.POST, instance= request.user)
#        # print(p_form)
       
#         # return render(request, 'users/profile.html', context)
#         if p_form.is_valid() and u_form.is_valid():
#             u_form.save()
#             p_form.save()

#             birth=request.POST['birthdate']
#             first=request.POST['first_name']
#             last=request.POST['last_name']
#             gender=request.POST['gender']
#             nation=request.POST['nationality']

#            # use=User.objects.filter(id=request.user.id).first()

#             #profile=Profile.objects.filter(user=use).first()
#             #profile=Profile.objects.filter(user=user_not).first()
            
              #new things: #####################################
#             user.first_name=first
#             user.last_name=last
#             user.gender=gender
#             user.nationality=nation
#             user.save()
              ########################################################

#             # profile.first_name=first
#             # profile.last_name=last
#             # profile.gender=gender
#             # profile.nationality=nation
#             # profile.save()

#             messages.success(request, f'Your account is Updated!')
#             return redirect('profile')   #get not post so dont have to tell u ur data will be lost
#     else:
#         #u_form= UserUpdateForm(request.POST, instance=request.user)
#         #p_form= ProfileUpdateForm(request.POST, instance= request.user)

#         #new things:#########################################
#         u_form=UserUpdateForm(request.POST, instance= user_not )
#         p_form=ProfileRegisterForm(request.POST, instance= user)

#         ########################################
#         #print("else")
#         #print(request.user.id)

#         #use=User.objects.filter(id=request.user.id).first()
#         #print(use)
#         #profile=Profile.objects.filter(user=use).first()
#         # profile=''
#         #print(profile.birth_date)
#         context={
#             'u_form':u_form,
#             'p_form': p_form,
#             'profile':profile
#         }
#         return render(request, 'users/profile.html', context)
    
#     #return render(request, 'users/editdata.html', context)
        
# #end profile

#updating
@login_required
def profile(request):

    if request.method=='POST':
        p_form= ProfileUpdateForm(request.POST, instance= request.user)
        print(p_form)
       
        # return render(request, 'users/profile.html', context)
        if p_form.is_valid():
            p_form.save()
            birth=request.POST['birthdate']
            first=request.POST['first_name']
            last=request.POST['last_name']
            gender=request.POST['gender']
            nation=request.POST['nationality']
            use=User.objects.filter(id=request.user.id).first()
            profile=Profile.objects.filter(user=use).first()
            profile.first_name=first
            profile.last_name=last
            profile.gender=gender
            profile.nationality=nation
            profile.save()
            # messages.success(request, f'Your account is Updated!')
            return redirect('profile')   #get not post so dont have to tell u ur data will be lost
    else:
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, instance= request.user)
        print("else")
        print(request.user.id)
        use=User.objects.filter(id=request.user.id).first()
        print(use)
        profile=Profile.objects.filter(user=use).first()
        # profile=''
        print(profile.birth_date)
        context={
            'u_form':u_form,
            'p_form': p_form,
            'profile':profile
        }
        return render(request, 'users/profile.html', context)
    
    #return render(request, 'users/editdata.html', context)
        
#end profile


#############################################################################################



def request_admin_authority(request):
    if request.method=='POST':
        print("hello profile")
    user_id=request.POST['authority']
    user_not=User.objects.filter(id=request.user.id).first()
    user = Profile.objects.get(user=user_not)
    # user = request.user
    user.request_status = "requested"
    user.save()
    print("saved")
    # success(request, f'{user.username} has requested admin authority')
    #send_notification_to_admin(user)  # function to send a notification to the admin
    return render(request, 'users/confirm.html')


#Mahy edited login view on 2/1 ######################################
class CustomLoginView(LoginView):
    def form_valid(self, form):
        # call the parent's form_valid method to log in the user
        response = super().form_valid(form)
        # the user has been authenticated, check if they are a superuser


       
        user_not=User.objects.filter(id=self.request.user.id).first()
        user = Profile.objects.get(user=user_not)

        if self.request.user.is_superuser:
            # the user is a superuser, redirect to the Django admin page
            #return redirect("admin/")
            return redirect("admin:index")
        #elif self.request.user.request_status=="approved":
       # elif self.request.user.username=="approved":
          #  return redirect("admin/")
        elif user.request_status=="approved":
            self.request.user.is_superuser=True
            self.request.user.is_staff=True
            self.request.user.save()
            return redirect("admin:index")
        else:
            # the user is a normal user, redirect to their profile page
            return redirect("profile")

###################################################################################################### idont think the followinga r necessary 
def approve_request(request, user_id):
    user = User.objects.get(id=user_id)
    user.profile.request_status = "approved"
    user.save()
    error(request, 'Your request for admin authority has been Approved')
    #send_notification_to_user(user)  # function to send a notification to the user
    return redirect("admin")

def deny_request(request, user_id):
    user = User.objects.get(id=user_id)
    user.profile.request_status = "denied"
    user.save()
    error(request, 'Your request for admin authority has been denied')
    #send_notification_to_user(user)  # function to send a notification to the user
    return redirect("admin")

def edit_database(request):
    if request.method=='POST':
        user_id= request.POST.get('user_id')
        request_status= request.POST.get('request_status')
    # update the database as desired
        user = User.objects.get(pk=user_id)
        user.profile.request_status = request_status
        user.save()

    # call the desired function
    request_admin_authority()

    return render(request, 'profile.html')

##################################################################################






   
