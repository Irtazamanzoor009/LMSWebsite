from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='first_paragraph')
def first_paragraph(value):
    soup = BeautifulSoup(value, "html.parser")
    first_p = soup.find('p')
    return str(first_p) if first_p else ''
