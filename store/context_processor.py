from .models import Category, WishList
from taggit.models import Tag


def categories(request):
    parent_cats = Category.objects.filter(parent=None)
    all_cats = Category.objects.all()
    return {'categories': parent_cats, 'all_categories': all_cats}


def all_tag(request):
    all_tag = Tag.objects.all()
    print(all_tag)
    return {'all_tag': all_tag}


def wishlist_length(request):
    wishlist_length = WishList.objects.all().count()
    return {'wishlist_length': wishlist_length}
