from django import template

register = template.Library()


@register.filter()
def multiply(value, arg):
    return float(value) * arg


# @register.filter()
# @register.inclusion_tag('store/sell_details.html', takes_context=True)
# def own_store_filter(all_products):
#     if all_products:
#         request = context['request']
#         data = all_products.filter(store=request.user.user_store)
#         return data
#     return all_course
