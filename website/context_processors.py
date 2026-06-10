def company(request):
    return {
        "company_name": "Pioneer Smart Systems",
        "company_name_ar": "شركة الرواد للأنظمة الذكية",
    }


def language(request):
    current_language = request.session.get("site_language", "en")
    if current_language not in ("en", "ar"):
        current_language = "en"

    return {
        "site_language": current_language,
        "is_arabic": current_language == "ar",
    }
