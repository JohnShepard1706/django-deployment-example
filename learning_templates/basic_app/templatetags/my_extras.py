from django import template

register = template.Library()


# To register the filter (Second Way)
@register.filter(name="cut_str")

def cut(value,arg):
    # This cuts out all the values of "arg" from the string!

    return value.replace(arg,"")

# To register the filter (First Way)
# register.filter("cut_str",cut)