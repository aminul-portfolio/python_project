from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

# ✅ Home Page
def home(request):
    return render(request, 'core/home.html')

# ✅ Generic Page Renderer (used by all lambda routes)
def topic_page(request, template_name, page_name):
    comments = Comment.objects.filter(page_name=page_name).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.page_name = page_name
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()

    return render(request, template_name, {
        'form': form,
        'comments': comments,
    })

# ✅ Optional: Homepage Sections Overview
def home_view(request):
    sections = [
        {"emoji": "📚", "label": "00 - Object & Data Structures", "url": "numbers", "action": "Start"},
        {"emoji": "🔍", "label": "01 - Comparison Operators", "url": "comparison_operators", "action": "Explore"},
        {"emoji": "📄", "label": "02 - Python Statements", "url": "python_statement", "action": "Learn"},
        {"emoji": "🧠", "label": "03 - Methods & Functions", "url": "methods", "action": "Practice"},
        {"emoji": "🧪", "label": "04 - Milestone Project 1", "url": "warm_project", "action": "Start Project"},
        {"emoji": "🏗️", "label": "05 - OOP in Python", "url": "object", "action": "Dive In"},
        {"emoji": "📦", "label": "06 - Modules & Packages", "url": "mod_pack", "action": "View"},
        {"emoji": "🧪", "label": "07 - Error & Exception", "url": "error_hand_unit", "action": "Handle Errors"},
        {"emoji": "🧪", "label": "08 - Milestone Project 2", "url": "blackjack_walkthrough", "action": "Play Blackjack"},
        {"emoji": "🚧", "label": "09 - Empty Section", "url": "all_empty_all", "action": "Explore"},
        {"emoji": "🎯", "label": "10 - Decorators", "url": "home_decorator", "action": "🧠 Decorators Intro"},
        {"emoji": "🌀", "label": "11 - Generators", "url": "generators_iterator", "action": "Generate"},
        {"emoji": "⚙️", "label": "12 - Advanced Modules", "url": "pods_advanced_all_in_one", "action": "View"},
        {"emoji": "🌐", "label": "13 - Web Scraping", "url": "scraping_web", "action": "Scrape Web"},
        {"emoji": "🖼️", "label": "14 - Images", "url": "image_working", "action": "View Images"},
        {"emoji": "📄", "label": "15 - PDFs & Excel", "url": "some_practice", "action": "Access Files"},
        {"emoji": "📧", "label": "16 - Emailing", "url": "emailing_python", "action": "Send Email"},
        {"emoji": "🔍", "label": "17 - Advanced Python Objects", "url": "advanced_solution", "action": "View Objects"},
        {"emoji": "🧩", "label": "18 - GUI Projects", "url": "widget_bonus", "action": "Try GUI"},
    ]
    return render(request, "home.html", {"sections": sections})
