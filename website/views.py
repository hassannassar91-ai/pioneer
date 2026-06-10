from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme


def set_language(request):
    lang = (request.GET.get("lang") or "en").lower()
    request.session["site_language"] = "ar" if lang == "ar" else "en"
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"
    if not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = "/"
    return redirect(next_url)


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def solutions(request):
    return render(request, "website/solutions.html")


def industries(request):
    return render(request, "website/industries.html")


def products(request):
    return render(request, "website/products.html")


def projects(request):
    return render(request, "website/projects.html")


def contact(request):
    if request.method == "POST":
        is_arabic = request.session.get("site_language") == "ar"
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        message = (request.POST.get("message") or "").strip()
        if not name or not email or not message:
            messages.error(
                request,
                "يرجى تعبئة الاسم الكامل والبريد الإلكتروني والرسالة."
                if is_arabic
                else "Please fill in full name, email address, and message.",
            )
        else:
            messages.success(
                request,
                "شكراً لك — تم استلام رسالتك، وسنتواصل معك قريباً."
                if is_arabic
                else "Thank you — your message was received. We will get back to you soon.",
            )
            return redirect("contact")
    return render(request, "website/contact.html")
