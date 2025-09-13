from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Request, Chat

User = get_user_model()

# Custom User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Custom Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

# Edit Profile Form
class EditProfileForm(forms.ModelForm):
    interests = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
        'placeholder': 'e.g., hiking, music'
    }), help_text="Enter interests separated by commas (e.g., hiking, music)")

    class Meta:
        model = User
        fields = ['bio', 'location', 'interests', 'profile_picture', 'gender', 'preferences']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
                'accept': 'image/*'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white'
            }),
            'preferences': forms.Select(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white'
            }),
        }

# Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
                'placeholder': "What's on your mind?"
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
                'accept': 'image/*'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
                'placeholder': 'e.g., travel, fun'
            }),
        }

# Edit Post Form
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
                'accept': 'image/*'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 dark:border-slate-600 rounded p-2 dark:bg-slate-800 dark:text-white',
                'placeholder': 'Comma-separated tags'
            }),
        }

# Request Form
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = []  # No fields needed; sender/receiver set in view

# Message Form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full px-4 py-2 border border-gray-300 dark:border-slate-600 rounded-lg dark:bg-slate-800 dark:text-white focus:outline-none focus:ring-1 focus:ring-pink-500',
                'placeholder': 'Type your message here...'
            }),
        }
