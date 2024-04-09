from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
# Create your views here.
from django.conf import settings


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# @cache_page(CACHE_TTL)
# def recipes_view(request):
#     return render(request, 'cookbook/recipes.html', {
#         'recipes': get_recipes()
#     })