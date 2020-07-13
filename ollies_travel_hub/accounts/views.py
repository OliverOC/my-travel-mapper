from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView, TemplateView, DetailView
from django.views.generic.edit import ModelFormMixin, UpdateView
from .models import User, UserProfile
from .forms import UserSignUpForm, UserProfileForm, UpdateUserProfileForm, UserUpdateForm


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

    return render(request, 'accounts/signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


class UserDetail(DetailView):
    model = UserProfile

    # def get_object(self):
    #     return get_object_or_404(UserProfile, slug=self.kwargs.get('slug'))


class EditUser(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_update.html'
    slug_field = 'username'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse('accounts:profile', kwargs={'slug': slug})


class EditUserProfile(UpdateView):
    model = UserProfile
    form_class = UpdateUserProfileForm
    template_name = 'accounts/userprofile_update.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse('accounts:profile', kwargs={'slug': slug})

