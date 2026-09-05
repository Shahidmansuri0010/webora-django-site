# WebOra — Website Development Agency Site (Django)

A premium, conversion-focused website for WebOra, a professional web
development agency. Built with Django (backend + templates), vanilla
HTML/CSS/JS on the frontend, and Django's ORM/SQLite for storing contact
enquiries.

## Quick start

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # optional, to view enquiries in /admin/
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project structure

```
webora/                Django project settings, root urls.py
main/                   Primary app
  models.py             Enquiry model (contact form submissions)
  forms.py               EnquiryForm (Django ModelForm)
  views.py               Views for every page
  urls.py                 App URL routes
  admin.py                Enquiry registered in Django admin
  data.py                  Site copy: services, pricing, portfolio, FAQ, etc.
  templates/
    base.html               Shared layout, meta tags, nav/footer includes
    partials/                navbar.html, footer.html, whatsapp_button.html, icons.html
    main/                     home.html, services.html, portfolio.html,
                              pricing.html, process.html, about.html,
                              faq.html, contact.html
static/main/
  css/                     tokens.css, base.css, navbar.css, hero.css,
                            components.css, forms.css
  js/main.js                Navbar scroll state, mobile menu, reveal-on-scroll,
                            FAQ accordion, active-link highlighting
  img/                      Logo assets + generated portfolio preview SVGs
media/                   User-uploaded files (empty by default)
```

## Before going live — configuration checklist

A few values are intentionally left as placeholders since real business
details weren't provided. Edit `webora/settings.py`:

```python
WHATSAPP_NUMBER = ""              # e.g. "919999999999" — no + or spaces.
                                   # Until set, the WhatsApp button links to
                                   # the contact page instead of wa.me.
CONTACT_EMAIL = "hello@webora.example"   # replace with the real business email
INSTAGRAM_HANDLE = "webora.digital"      # replace with the real handle
```

Also update `SECRET_KEY` and set `DEBUG = False` (plus `ALLOWED_HOSTS`)
before deploying to production, per standard Django practice.

## Contact form

Submissions are saved to the `Enquiry` model and viewable at `/admin/`
after creating a superuser. No email backend is configured — wire up
`EMAIL_BACKEND` in settings if you want email notifications on new
enquiries.

## Content notes

- All portfolio items are clearly labeled **"Demo Project"** in the UI —
  they are illustrative mockups (SVG), not real client work.
- No fake testimonials, client logos, review counts, or years-of-experience
  claims are used anywhere, per the brief.
- Pricing sections clearly separate the development fee from domain,
  hosting, deployment, and third-party costs — see the "What Is Not
  Included" panel on the Pricing page and homepage.
