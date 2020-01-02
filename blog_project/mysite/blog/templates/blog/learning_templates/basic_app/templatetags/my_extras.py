from django import  template

register = template.Library()
# {% load my_extras %} in template
@register.filter(name='cutOne')
def cutOne(value,arg):
    """
    this cuts out all values of 'arg'
    """
    return value.replace(arg,'Redacted')

# register.filter('cut',cut)
