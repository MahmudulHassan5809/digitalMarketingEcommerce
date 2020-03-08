from .models import Category
from taggit.models import Tag


def categories(request):
    parent_cats = Category.objects.filter(parent=None)
    all_cats = Category.objects.all()
    return {'categories': parent_cats, 'all_categories': all_cats}


def all_tag(request):
    all_tag = Tag.objects.all()
    print(all_tag)
    return {'all_tag': all_tag}
