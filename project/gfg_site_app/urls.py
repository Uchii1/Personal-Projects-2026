"""
URL configuration for studySoft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gfg_site_app.urls')),
]

"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import PlaceholderView

# Designign login page
from django.urls import path, include

# Designing sign up page
from .views import SignUpView

# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),  # provides "login"
    path("signup/", SignUpView.as_view(), name="signup"),
    
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
    # Registering the view to save quiz results
    path('api/submit-quiz/', views.submit_quiz, name='submit_quiz'),

    path("geometric-formulas/", views.geometric_formulas, name="geometric_formulas"),
    path("pomodoro-timer/", views.pomodoro_timer, name="pomodoro_timer"),
    path("break-resources/", views.break_resources, name="break_resources"),
    #path("progress/", views.performance, name="progress"),
    path("about/", views.about, name="about"),

    path('progress/', views.progress, name='progress'),
    path('api/progress-data/', views.progress_data, name='progress-data'),
    path("guess-game/", views.guess_game_page, name="guess_game"),
    path("guess-game/guess/", views.guess_game_guess, name="guess_game_guess"),
    
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("accessibility/", views.accessibility, name="accessibility"),

    path("syllabus/", views.syllabus, name="syllabus"),
    path("contact/", views.contact, name="contact"),
    path("font/", views.choose_font, name="choose_font"),
]




# Debugging text
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



