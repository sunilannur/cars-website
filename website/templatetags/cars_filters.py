from django import template
from django.db.models import F
from website.models import Transmission


register = template.Library()

@register.inclusion_tag('filter_template.html', takes_context=True)
def filters(context):
    context_dict = {}
    context_dict["transmission"] = []
    transmission_fils = Transmission.objects.all()

    for each in transmission_fils:
        context_dict["transmission"].append({
            "id":each.id,
            "name":each.name
        })
    return context_dict