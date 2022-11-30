from .models import MainCategory, Category
from .forms import addCategoryForm

def categories_processor(request):
    form = addCategoryForm()
    mainCategories = MainCategory.objects.all()
    categories = Category.objects.all()
    return {
        'mainCategories': mainCategories, 
        'categories': categories, 
        'form': form
        }