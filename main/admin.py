from django.contrib import admin

from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "business_name", "phone", "email", "business_type", "website_requirement", "created_at")
    list_filter = ("business_type", "website_requirement", "created_at")
    search_fields = ("name", "business_name", "email", "phone")
    ordering = ("-created_at",)
