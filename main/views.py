from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from . import data
from .forms import EnquiryForm


def _base_context():
    """Context shared by every page (used for SEO defaults, nav, etc.)."""
    return {
        "site_name": settings.SITE_NAME,
        "whatsapp_number": settings.WHATSAPP_NUMBER,
        "contact_email": settings.CONTACT_EMAIL,
        "instagram_handle": settings.INSTAGRAM_HANDLE,
    }


def home(request):
    context = _base_context()
    context.update({
        "meta_title": "WebOra | Modern Website Design & Development",
        "meta_description": "WebOra builds modern, responsive and professional websites for businesses, restaurants, cafes, salons, real estate, e-commerce and more.",
        "services": data.SERVICES,
        "who_we_build_for": data.WHO_WE_BUILD_FOR,
        "portfolio": data.PORTFOLIO[:6],
        "why_webora": data.WHY_WEBORA,
        "technologies": data.TECHNOLOGIES,
        "pricing": data.PRICING,
        "process_steps": data.PROCESS_STEPS,
        "trust_strip": data.TRUST_STRIP,
        "faqs": data.FAQS[:5],
    })
    return render(request, "main/home.html", context)


def services(request):
    context = _base_context()
    context.update({
        "meta_title": "Services | WebOra",
        "meta_description": "Explore WebOra's website design and development services for businesses, restaurants, salons, real estate, healthcare and e-commerce.",
        "services": data.SERVICES,
        "why_webora": data.WHY_WEBORA,
    })
    return render(request, "main/services.html", context)


def portfolio(request):
    context = _base_context()
    context.update({
        "meta_title": "Our Work | WebOra",
        "meta_description": "See demonstration projects showcasing the kind of websites WebOra can design and build for modern businesses.",
        "portfolio": data.PORTFOLIO,
    })
    return render(request, "main/portfolio.html", context)


def pricing(request):
    context = _base_context()
    context.update({
        "meta_title": "Pricing | WebOra",
        "meta_description": "Simple, transparent website development pricing from WebOra. Domain, hosting and third-party costs are always billed separately.",
        "pricing": data.PRICING,
    })
    return render(request, "main/pricing.html", context)


def process(request):
    context = _base_context()
    context.update({
        "meta_title": "Our Process | WebOra",
        "meta_description": "See how WebOra takes a website from idea to launch — discuss, plan, design, develop and launch.",
        "process_steps": data.PROCESS_STEPS,
    })
    return render(request, "main/process.html", context)


def about(request):
    context = _base_context()
    context.update({
        "meta_title": "About | WebOra",
        "meta_description": "WebOra helps businesses establish a stronger digital presence through modern website design and custom web development.",
        "why_webora": data.WHY_WEBORA,
        "technologies": data.TECHNOLOGIES,
    })
    return render(request, "main/about.html", context)


def faq(request):
    context = _base_context()
    context.update({
        "meta_title": "FAQ | WebOra",
        "meta_description": "Answers to common questions about WebOra's website development pricing, process, hosting and more.",
        "faqs": data.FAQS,
    })
    return render(request, "main/faq.html", context)


def contact(request):
    context = _base_context()
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your enquiry has been received. WebOra will get back to you shortly.",
            )
            return redirect("main:contact")
    else:
        form = EnquiryForm()

    context.update({
        "meta_title": "Contact | WebOra",
        "meta_description": "Get in touch with WebOra to discuss your website project. Tell us about your business and requirements.",
        "form": form,
    })
    return render(request, "main/contact.html", context)
