from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ChatForm
import google.generativeai as genai
from dotenv import load_dotenv
import os
from .models import ChatMessage
# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@login_required
def home_view(request):
    profile_name = request.user.username
    old_chats = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')[:5]  # Retrieve last 5 chats for the user
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            response = chat.send_message(question)
            chatbot_response = response.text
            context = {'form': form, 'question': question, 'chatbot_response': chatbot_response, 'profile_name': profile_name, 'old_chats': old_chats}
            ChatMessage.objects.create(user=request.user, message=question)  # Record the user's message
            return render(request, 'chat.html', context)
        else:
            messages.error(request, 'Please enter a valid question.')
    else:
        form = ChatForm()
        context = {'form': form, 'question': '', 'profile_name': profile_name, 'old_chats': old_chats}
    return render(request, 'chat.html', context)
def sidebar_chats(request):
    if request.user.is_authenticated:
        old_chats = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')  # Retrieve last 5 chats for the user
        return {'old_chats': old_chats}
    return {}

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
