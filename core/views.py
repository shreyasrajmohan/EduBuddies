from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "core/index.html")

from django.shortcuts import render

def student_profile(request):
    return render(request, "core/student_profile.html")

def flashcards(request):
    return render(request, "core/flashcards.html")

def quizzes(request):
    return render(request, "core/quizzes.html")

def backlog(request):
    return render(request, "core/backlog.html")

def performance(request):
    return render(request, "core/performance.html")

def library(request):
    return render(request, "core/library.html")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('library')

from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

from django.shortcuts import render

def login_page(request):
    return render(request, "login_page.html")

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')

           #return redirect("/")   # ✅ Redirect to homepage after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login_page.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import StudentProfile  # we'll create this

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        user_type = request.POST.get("user_type")  # school or college
        grade = request.POST.get("grade")
        year = request.POST.get("year")
        school_name = request.POST.get("school_name")
        college_name = request.POST.get("college_name")
        course = request.POST.get("course")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        student_id = request.POST.get("student_id")
        age = request.POST.get("age")
        dob = request.POST.get("dob")

        # create Django user (for authentication)
        user = User.objects.create_user(
            username=email,
            email=email,
            password="defaultpassword123",  # 🔑 replace with secure password handling
            first_name=name
        )
        user.save()

        # create student profile
        StudentProfile.objects.create(
            user=user,
            user_type=user_type,
            grade=grade,
            year=year,
            school_name=school_name,
            college_name=college_name,
            course=course,
            phone=phone,
            student_id=student_id,
            age=age,
            dob=dob
        )

        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect("home")

    return render(request, "signup.html")

from django.shortcuts import render

def home(request):
    return render(request, "index.html")   # make sure index.html is in templates/

from django.shortcuts import render

def login_view(request):
    return render(request, "login_page.html")   # make sure login_page.html is in templates/

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student_dashboard")
        else:
            return render(request, "login_page.html", {"error": "Invalid username or password"})
    return render(request, "login_page.html")

@login_required
def student_dashboard(request):
    return render(request, "student_dashboard.html")

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

from django.shortcuts import render

def signup(request):
    return render(request, "signup.html")  # you’ll need to create signup.html

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_dashboard')  # go to dashboard after login
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  # stay on login page if wrong
    return render(request, "login_page.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == "POST":
        # handle form data (later you can save user info here)
        return redirect("login")  # after signup, go to login
    return render(request, "signup.html")

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("login")  # send user back to login after logging out

from django.shortcuts import render

def home(request):
    return render(request, "index.html")   # make sure index.html is inside templates/
