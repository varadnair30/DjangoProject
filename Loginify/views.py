import json
from django.shortcuts import render, redirect
from django.contrib import messages

from Loginify.serializer import UserDetailsSerializer
from .models import UserDetails

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# def hello_world_view(request):
#     return HttpResponse("Hello, world!")


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'signup.html')
        
        #New user
        try:
            user = UserDetails.objects.create(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'signup.html')
            
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            #Check user
            user = UserDetails.objects.get(email=email, password=password)
            
            return HttpResponse(f"Welcome, {user.username}!")
        except UserDetails.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


# Create your views here.


def list_all_users_view(request):
    
    if request.method == 'GET':
        data = UserDetails.objects.all()
        
        s_data = UserDetailsSerializer(data, many=True)
        
        return JsonResponse(s_data.data, safe=False)
    
    


def get_user_details_by_email_view(request, email):
    if request.method == 'GET':
        
        data = UserDetails.objects.get(email=email)
        s_data = UserDetailsSerializer(data)
        
        return JsonResponse(s_data.data, safe=False)
    
@csrf_exempt
def update_user_details_view(request, email):
    user=UserDetails.objects.get(email=email)
    if request.method == 'PUT':
        
        input_data = json.loads(request.body)
        qs= UserDetailsSerializer(user,data=input_data)
        if qs.is_valid():
            qs.save()
            return JsonResponse({"success" : True}, status=200)
    return JsonResponse({"success" : False, "error" : qs.errors}, status=500)                

@csrf_exempt
def delete_user_view(request, email):

    user = UserDetails.objects.get(email=email)
    if request.method == 'DELETE':
        if user: user.delete()
        return JsonResponse({"success": True}, status=200)
    elif not user:
        
        return JsonResponse({"success": False, "error": "User not available"}, status=405)
    return JsonResponse({"success": False}, status=405)





