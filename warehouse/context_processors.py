from .models import MainCategory, Category

def categories_processor(request):
    mainCategories = MainCategory.objects.all()
    categories = Category.objects.all()
    return {'mainCategories': mainCategories,'categories': categories}