from django.shortcuts import render,redirect
from django.http import HttpResponse
from .decorators import user_has_hood
from .models import NeighbourHood,EmergencyService,Business,Post
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from .forms import BusinessForm,NewPostForm,UserProfileForm

@login_required(login_url='/accounts/login')
def home_page(request):


  hoods=NeighbourHood.get_all_neighbourhoods()
  if request.user.profile.neighbourhood:
    bss=Business.get_all_bs_by_hood(request.user.profile.neighbourhood_id)
    posts=Post.objects.filter(neighbourhood=request.user.profile.neighbourhood)
    police_services=EmergencyService.objects.filter(neighbourhood=request.user.profile.neighbourhood,service_type='Police') 
    hos_services=EmergencyService.objects.filter(neighbourhood=request.user.profile.neighbourhood,service_type='Hospital') 
    fire_services=EmergencyService.objects.filter(neighbourhood=request.user.profile.neighbourhood,service_type='Fire') 
    context={
      'hoods':hoods,
      'bss':bss,
      'p_services':police_services,
      'h_services':hos_services,
      'f_services':fire_services,
      'posts':posts
    }
  else:
    context={
      'hoods':hoods
    }
  return render(request,'home.html',context)



@login_required(login_url='/accounts/login')
def join_hood(request,hood_id):
  hood=NeighbourHood.find_neighbourhood(hood_id)
  Profile.objects.filter(user=request.user).update(neighbourhood=hood)
  NeighbourHood.objects.filter(id=hood_id).update(hood_occupants=F("hood_occupants") + 1)  
  messages.success(request, f'You joined {hood.hood_name} neighbourhood.')
  return redirect ('home_page')


@login_required(login_url='/accounts/login')
@user_has_hood
def e_services(request):
  police_services=EmergencyService.objects.filter(neighbourhood=request.user.profile.neighbourhood,service_type='Police') 
  hos_services=EmergencyService.objects.filter(neighbourhood=request.user.profile.neighbourhood,service_type='Hospital') 
  fire_services=EmergencyService.objects.filter(neighbourhood=request.user.profile.neighbourhood,service_type='Fire') 
  context={
    'p_services':police_services,
    'h_services':hos_services,
    'f_services':fire_services
  }

  return render(request,'e_services.html',context) 



@login_required(login_url='/accounts/login')
@user_has_hood
def hood_bs(request):
  bss=Business.get_all_bs_by_hood(request.user.profile.neighbourhood_id)

  if request.method == "POST":
      form = BusinessForm(request.POST, request.FILES)
      if form.is_valid():
          business = form.save(commit=False)
          business.user = request.user
          business.neighbourhood=request.user.profile.neighbourhood
          business.save()
          messages.success(request, f'Business successfully added')
          form = BusinessForm() 
  else:
      form = BusinessForm()


  context={
    'bss':bss,
    'form':form
  }

  return render(request,'hood_businesses.html',context)   




@login_required(login_url='/accounts/login')
@user_has_hood
def hood_posts(request):
  posts=Post.objects.filter(neighbourhood=request.user.profile.neighbourhood)

  if request.method == "POST":
      form = NewPostForm(request.POST)
      if form.is_valid():
          post = form.save(commit=False)
          post.user = request.user
          post.neighbourhood=request.user.profile.neighbourhood
          post.save()
          messages.success(request, f'Post successfully uploaded')
          form = NewPostForm()
  else:
      form = NewPostForm()

  context={
    'posts':posts,
    'form':form
  }

  return render(request,'hood_posts.html',context)


@login_required(login_url='/accounts/login')
def my_profile(request):
  profile=request.user.profile
  if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully')
            return redirect('my_profile')
  else:
      form = UserProfileForm(instance=request.user.profile)
  

  context={
    'profile':profile,
    'form':form
  }

  return render(request,'my_profile.html',context)  


@login_required(login_url='/accounts/login')
@user_has_hood
def search_business(request):

    if 'bs_name' in request.GET and request.GET["bs_name"]:
        search_term = request.GET.get("bs_name")
        bss =Business.search_business(search_term,request.user.profile.neighbourhood_id)
        message = f"{search_term}"
        
        context={
          "message":message,
          'bss':bss
        }
        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any business"
        context={
          "message":message,
        }
        return render(request, 'search.html',context) 