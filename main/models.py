from django.db import models


class Enquiry(models.Model):
    """A lead captured through the WebOra contact / enquiry form."""

    BUSINESS_TYPE_CHOICES = [
        ("business", "Business Website"),
        ("restaurant", "Restaurant / Cafe"),
        ("salon", "Salon / Beauty"),
        ("ecommerce", "E-commerce"),
        ("real_estate", "Real Estate"),
        ("clinic", "Doctor / Clinic"),
        ("portfolio", "Portfolio"),
        ("custom", "Custom Web Application"),
        ("other", "Other"),
    ]

    REQUIREMENT_CHOICES = [
        ("new", "New Website"),
        ("redesign", "Website Redesign"),
        ("ecommerce", "E-commerce Store"),
        ("webapp", "Custom Web Application"),
        ("not_sure", "Not Sure Yet"),
    ]

    name = models.CharField(max_length=120)
    business_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.CharField("Phone / WhatsApp", max_length=30)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE_CHOICES, default="other")
    website_requirement = models.CharField(max_length=20, choices=REQUIREMENT_CHOICES, default="new")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.business_name or 'N/A'} ({self.created_at:%d %b %Y})"
