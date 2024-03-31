from .models import Property, Category
from django.urls import resolve

def global_context(request):
    if resolve(request.path_info).app_name == "property":
        categories = Category.objects.all()
        property_choices = dict(Property.property_choices)
        return {"categories": categories, "property_choices": property_choices}
    return {}
