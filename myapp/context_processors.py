from .models import *

def category(request):
    categories = Category.objects.all()

    return {'categories': categories}

def tag(request):
    tags = Tag.objects.all()
    return {'tags': tags}