from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView, TemplateView
from django.views.generic.edit import ModelFormMixin, UpdateView
from .models import User
from .forms import UserSignUpForm, UserProfileForm


# class SignUp(CreateView):
#     form_class = UserSignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'


def signup(request):

    registered = False

    if request.method == 'POST':

        user_form = UserSignUpForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(username=username, password=password)

            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('scratch_map:home')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserSignUpForm()
        profile_form = UserProfileForm()

    return render(request, 'accounts/signup2.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

# class EditUser(UpdateView):
#     model = User
#     form_class = UserSignUpForm
#     template_name = 'accounts/update_user_profile.html'
#
#     def get_object(self, *args, **kwargs):
#         user = get_object_or_404(User, pk=self.kwargs['pk'])
#         return user.user





    # second_form_class = UserSignUpForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile_picture'] = self.second_form_class
    #     return context
    #
    # def form_valid(self, form):
    #     user_form = UserSignUpForm(self.request.POST)
    #     if form.is_valid() and user_form.is_valid():
    #         user = form.save()
    #         profile = user_form.save(commit=False)
    #         profile.user = user
    #         profile.save()
    #     return super().form_valid(form)


# def sign_up_view(request):
#     signed_up = False
#
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             profile = profile_form.save(commit=False)
#             profile.user = user
#
#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']
#
#             profile.save()
#
#             signed_up = True
#
#         else:
#             print(user_form.errors, profile_form.errors)
#
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#
#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form,
#         'signed_up': signed_up,
#     }
#
#     return render(request, 'accounts/sign_up.html', context)
#
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 if 'next' in request.POST:
#                     return redirect(request.POST.get('next'))
#                 else:
#                     return redirect('scratch_map:home')
#
#         else:
#             print("Someone tried to login and failed.")
#             print("Username: {} and password {}".format(username, password))
#             return HttpResponse("Invalid login details.")
#
#     else:
#         return render(request, 'accounts/login.html')
#
#
# @login_required
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('scratch_map:home'))
