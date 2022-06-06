from django.shortcuts import render

# Create your views here.
from user_app.forms import UserForm,UserProfileInfoForm

def index(request):
    return render(request,'user_app/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        UserForm = UserForm(data =request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if  user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_pasword(user.pasword)
            user.save()

            prfile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request:
                profile.profile_pic = request.FILES['proffile_pic']

            prfile.save()

            registerd = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        UserForm = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user_app/registration',{
        'user_form':UserForm,
        'profile_fprm':profile_form,
        'registered':registered
        })



