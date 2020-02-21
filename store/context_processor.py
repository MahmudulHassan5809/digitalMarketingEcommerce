from .models import Category

def categories(request):
    parent_cats = Category.objects.filter(parent=None)
    all_cats = Category.objects.all()
    return {'categories': parent_cats, 'all_categories': all_cats}