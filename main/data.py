"""
Static site content for WebOra.

Kept separate from views.py so page copy can be edited without touching
view logic. Nothing here is a database model because this content is
managed by the agency, not end users.
"""

SERVICES = [
    {
        "icon": "briefcase",
        "title": "Business Websites",
        "description": "Professional websites for companies and local businesses.",
    },
    {
        "icon": "cafe",
        "title": "Restaurant & Cafe Websites",
        "description": "Modern menus, galleries, location information, contact and reservation-focused experiences.",
    },
    {
        "icon": "sparkle",
        "title": "Salon & Beauty Websites",
        "description": "Elegant websites designed to showcase services, pricing, gallery and contact options.",
    },
    {
        "icon": "cart",
        "title": "E-commerce Websites",
        "description": "Online stores with product catalogs, shopping functionality and scalable architecture.",
    },
    {
        "icon": "home",
        "title": "Real Estate Websites",
        "description": "Property-focused websites with listings, images, enquiry forms and location information.",
    },
    {
        "icon": "cross",
        "title": "Doctor & Clinic Websites",
        "description": "Professional websites for doctors, clinics and healthcare businesses.",
    },
    {
        "icon": "user",
        "title": "Portfolio Websites",
        "description": "Personal and professional portfolio websites for individuals and professionals.",
    },
    {
        "icon": "code",
        "title": "Custom Web Applications",
        "description": "Custom web applications and business solutions using modern technologies.",
    },
]

WHO_WE_BUILD_FOR = [
    {"title": "Restaurants", "icon": "restaurant"},
    {"title": "Cafes", "icon": "cafe"},
    {"title": "Salons", "icon": "sparkle"},
    {"title": "Clothing Stores", "icon": "shirt"},
    {"title": "Doctors & Clinics", "icon": "cross"},
    {"title": "Real Estate", "icon": "home"},
    {"title": "Local Shops", "icon": "shop"},
    {"title": "Startups", "icon": "rocket"},
    {"title": "Professionals", "icon": "user"},
]

PORTFOLIO = [
    {
        "slug": "cafe",
        "title": "Cafe Website",
        "category": "Food & Beverage",
        "description": "A warm, inviting site concept with menu highlights, gallery and a simple location & hours layout.",
        "image": "img/portfolio-cafe.svg",
        "accent": "cafe",
    },
    {
        "slug": "restaurant",
        "title": "Restaurant Website",
        "category": "Food & Beverage",
        "description": "A refined dining experience online — full menu, ambience gallery and reservation-focused contact section.",
        "image": "img/portfolio-restaurant.svg",
        "accent": "restaurant",
    },
    {
        "slug": "salon",
        "title": "Salon Website",
        "category": "Beauty & Wellness",
        "description": "An elegant showcase of services and pricing designed to make booking an appointment effortless.",
        "image": "img/portfolio-salon.svg",
        "accent": "salon",
    },
    {
        "slug": "clothing",
        "title": "Clothing Store Website",
        "category": "Retail / E-commerce",
        "description": "A clean, catalog-style layout built to highlight collections and drive product enquiries.",
        "image": "img/portfolio-clothing.svg",
        "accent": "clothing",
    },
    {
        "slug": "real-estate",
        "title": "Real Estate Website",
        "category": "Real Estate",
        "description": "Property listings with imagery, key details and a straightforward enquiry form for leads.",
        "image": "img/portfolio-realestate.svg",
        "accent": "realestate",
    },
    {
        "slug": "business",
        "title": "Business Website",
        "category": "Corporate",
        "description": "A trust-building corporate layout with services, credentials and a clear path to contact.",
        "image": "img/portfolio-business.svg",
        "accent": "business",
    },
]

WHY_WEBORA = [
    {
        "icon": "design",
        "title": "Modern Design",
        "description": "Websites designed to create a strong first impression.",
    },
    {
        "icon": "mobile",
        "title": "Mobile First",
        "description": "Your website looks great on phones, tablets and desktops.",
    },
    {
        "icon": "speed",
        "title": "Performance Focused",
        "description": "Clean development and performance-conscious implementation.",
    },
    {
        "icon": "seo",
        "title": "SEO-Friendly Structure",
        "description": "Built with a structure that supports search engine visibility.",
    },
    {
        "icon": "target",
        "title": "Business Focused",
        "description": "Design decisions are made around your business goals and customers.",
    },
    {
        "icon": "price",
        "title": "Transparent Pricing",
        "description": "Clear development pricing with external costs explained separately.",
    },
]

TECHNOLOGIES = [
    "HTML", "CSS", "JavaScript", "Python", "Django",
    "MySQL", "PostgreSQL", "REST APIs", "Responsive Design",
]

PRICING = [
    {
        "key": "starter",
        "name": "Starter",
        "price": "₹5,999",
        "label": "Website Development Fee",
        "suited_for": "Small businesses that need a professional online presence.",
        "features": [
            "Up to 5 pages",
            "Professional UI design",
            "Mobile responsive design",
            "Contact form",
            "WhatsApp integration",
            "Social media integration",
            "Basic SEO setup",
            "Basic performance optimization",
        ],
        "cta": "Get Started",
        "highlight": False,
    },
    {
        "key": "business",
        "name": "Business",
        "price": "₹9,999",
        "label": "Website Development Fee",
        "badge": "Most Popular",
        "suited_for": "Businesses looking for a stronger and more complete online presence.",
        "features": [
            "Everything in Starter",
            "Up to 8–10 pages",
            "Premium UI/UX",
            "Gallery / portfolio",
            "Google Maps integration",
            "Advanced contact forms",
            "SEO-friendly structure",
            "Performance optimization",
            "Business-focused layout",
        ],
        "cta": "Choose Business",
        "highlight": True,
    },
    {
        "key": "premium",
        "name": "Premium",
        "price": "₹14,999+",
        "label": "Starting Development Fee",
        "suited_for": "Businesses requiring advanced functionality and custom development.",
        "features": [
            "Everything in Business",
            "Custom UI/UX",
            "Advanced functionality",
            "Database integration",
            "Product/service management",
            "Custom forms",
            "Admin functionality where required",
            "Custom development",
        ],
        "cta": "Discuss Requirements",
        "highlight": False,
    },
]

PROCESS_STEPS = [
    {"number": "01", "title": "Discuss", "description": "We understand your business, audience and requirements."},
    {"number": "02", "title": "Plan", "description": "We define the website structure, content and functionality."},
    {"number": "03", "title": "Design", "description": "We create the visual direction and user experience."},
    {"number": "04", "title": "Develop", "description": "We turn the approved design into a responsive website."},
    {"number": "05", "title": "Launch", "description": "After approval, deployment and hosting setup are completed using the client's chosen infrastructure."},
]

FAQS = [
    {
        "question": "What does the ₹5,999 package include?",
        "answer": "The ₹5,999 package is the website design and development fee for the Starter plan. It covers the design and build of your website. External costs such as domain, hosting and deployment are separate and paid by the client.",
    },
    {
        "question": "Do you provide domain and hosting?",
        "answer": "WebOra does not sell domain or hosting directly. You purchase and own your domain and hosting, and WebOra can assist with the setup and configuration during launch.",
    },
    {
        "question": "Is deployment included?",
        "answer": "Deployment and server infrastructure costs are separate from the development fee. WebOra handles the technical deployment process using the hosting infrastructure you choose.",
    },
    {
        "question": "Can you build an e-commerce website?",
        "answer": "Yes. Custom e-commerce solutions are available and are quoted based on your catalog size, payment requirements and desired functionality.",
    },
    {
        "question": "Will my website work on mobile?",
        "answer": "Yes. Every website WebOra builds is designed to be fully responsive across mobile, tablet and desktop devices.",
    },
    {
        "question": "Can I request custom features?",
        "answer": "Yes. Custom features, integrations and functionality can be added and are quoted according to your specific requirements.",
    },
    {
        "question": "Do you provide maintenance?",
        "answer": "Ongoing maintenance and support can be arranged separately after your website is launched.",
    },
    {
        "question": "How do I start?",
        "answer": "Click \"Get Your Website\" or reach out through WhatsApp or the contact form, and WebOra will get back to you to discuss your project.",
    },
]

TRUST_STRIP = [
    {"icon": "design", "label": "Professional Design"},
    {"icon": "mobile", "label": "Mobile Responsive"},
    {"icon": "speed", "label": "Fast Performance"},
    {"icon": "seo", "label": "SEO-Friendly"},
    {"icon": "target", "label": "Business Focused"},
]
