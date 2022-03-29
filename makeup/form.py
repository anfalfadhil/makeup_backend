
from .models import Comments
from django.contrib.auth.forms import UserCreationForm
from .models import Comments, Post, Profile
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from guardian.mixins import PermissionRequiredMixin


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["post", "name"]
      

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model= User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "content", "slug"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model= User
        fields = ["username", "email"]
       


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ["image"]
        