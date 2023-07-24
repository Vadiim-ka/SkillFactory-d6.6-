from django import template

register = template.Library()

censu = ['Редиска', 'Дурак', 'Дура', 'Боль']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError()

    for word in value.split():
        if word.lower() in censu:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 2)}{word[-1]}")
    return value
