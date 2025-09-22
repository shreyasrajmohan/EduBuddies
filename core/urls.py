from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.student_profile, name='student_profile'),
    path('flashcards/', views.flashcards, name='flashcards'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('backlog/', views.backlog, name='backlog'),
    path('performance/', views.performance, name='performance'),

    # library add/list/delete
    path('library/', views.library, name='library'),
    path('library/delete/<int:note_id>/', views.delete_note, name='delete_note'),

    # auth
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # landing page
]

from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # homepage
    path("login/", views.login_page, name="login"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
]

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]


from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # root URL now goes to index.html
    path("signup/", views.signup, name="signup"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),   # <-- NEW
]

from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # now handles "/"
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("signup/", views.signup, name="signup"),  # ✅ now Django knows "signup"
]

from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  # your existing login view
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # ✅ root URL
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("logout/", views.logout_view, name="logout"),   # 👈 add this
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # 👈 homepage (landing page)
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("logout/", views.logout_view, name="logout"),
]
