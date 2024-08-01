from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs) -> str:
    updated = request.GET.copy()
    for key, vel in kwargs.items():
        if vel is not None:
            updated[key] = vel
        else:
            updated.pop(key, 0)
    return updated.urlencode()
