from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    preference_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('A', 'Any'),
    ]
    
    # Additional fields for the user
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=gender_choices, null=True, blank=True)
    interests = models.TextField(null=True, blank=True)  # Could be ManyToManyField to a new Interest model for scalability
    preferences = models.CharField(max_length=1, choices=preference_choices, null=True, blank=True, default='A')  # Default to 'Any'

    def __str__(self):
        return self.username
    
    

# Post Model (User posts on the platform)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)  # For tagging posts
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False)  # For pinning posts
    is_archived = models.BooleanField(default=False)  # For archiving posts
    likes_count = models.IntegerField(default=0)  # Track likes
    views_count = models.IntegerField(default=0)  # Track views
    shares_count = models.IntegerField(default=0)  # Track shares

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"

    class Meta:
        ordering = ['-created_at']  # Order posts by creation date (newest first)
        db_table = 'Posts'
        
        
# Request Model (Tracks user connection requests)
class Request(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status_choices = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default='P')
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.sender.username} to {self.receiver.username} - Status: {self.get_status_display()}"

    class Meta:
        unique_together = ['sender', 'receiver']  # Prevent duplicate requests
        db_table = 'Requests'
        

# Chat Model (Messages exchanged between users)
class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"

    class Meta:
        ordering = ['timestamp']  # Order messages by timestamp
        db_table = 'Chats'
        

# Like Model (Tracks likes on posts)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked post {self.post.id}"

    class Meta:
        unique_together = ['user', 'post']  # Prevent multiple likes by the same user on the same post
        db_table = 'Likes'


# Comment Model (Tracks comments on posts)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')  # For nested replies

    def __str__(self):
        return f"Comment by {self.user.username} on post {self.post.id}"

    class Meta:
        ordering = ['created_at']  # Order comments by creation date
        db_table = 'Comments'
        
        
from django.db import models
from django.contrib.auth.models import AbstractUser

# Existing User, Post, Request, Chat, Like, Comment models (unchanged)
# ... [Your provided models here] ...

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    related_request = models.ForeignKey('Request', on_delete=models.CASCADE, null=True, blank=True)
    related_chat = models.ForeignKey('Chat', on_delete=models.SET_NULL, null=True, blank=True)
    related_post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)  # Added for likes
    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

    class Meta:
        ordering = ['-created_at']
        db_table = 'Notifications'
        
        
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HiddenUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hidden_users')
    hidden_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hidden_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hidden_user')
        db_table = 'HiddenUsers'

    def __str__(self):
        return f"{self.user.username} hid {self.hidden_user.username}"