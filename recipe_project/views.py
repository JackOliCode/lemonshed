from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm    
from django.shortcuts import render, redirect

########################
# LogIn View #
########################

def login_view(request):
    error_message = None   
    #form object with username and password fields                             
    form = AuthenticationForm() 

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid(): 
            username = form.cleaned_data.get('username')      #read username
            password = form.cleaned_data.get('password')    #read password

            user=authenticate(username=username, password=password) #use Django authenticate function to validate the user
            if user is not None:
                login(request, user)
                return redirect('recipes:list')
            else:                                               #in case of error
                error_message ='ooops.. something went wrong'   #print error message
    
    #prepare data to send from view to template
    context ={                                             
       'form': form,                                 #send the form data
       'error_message': error_message                     #and the error_message
   }
   #load the login page using "context" information
    return render(request, 'auth/login.html', context)  


########################
# LogOut View #
########################

def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html') 