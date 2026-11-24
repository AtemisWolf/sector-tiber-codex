from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "codex/home.html")


def section(request, section_name):
    return render(
        request,
        "codex/section.html",
        {"section_name": section_name}
    )