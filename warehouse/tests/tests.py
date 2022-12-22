from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.urls import reverse
from ..models import MainCategory, Category, Position, CategoryValue
from ..views.views import CategoryValuesList, CategoryValuesDelete 
import logging
_logger = logging.getLogger('django')
# Create your tests here.
class UrlsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.mainCategory = MainCategory.objects.create(name="TestTop")
        self.category = Category.objects.create(
            name = "Test",
            topCategory = self.mainCategory
        )
        self.position = Position.objects.create(
            name = "TestPosition",
            category = self.category,
            imagePath = "",
            amount = 10,
        )
        self.categoryValue = CategoryValue.objects.create(
            propertyName="TestValue",
            category = self.category
        )


    def test_warehouse_main_view(self):
        response = self.client.get(reverse('warehouseMain'))
        self.assertEqual(response.status_code, 200)


    def test_category_values_list(self):
        preparedKwargs = {
            'mainCategoryId': self.mainCategory.id,
            'categoryId': self.category.id
        }
        response = self.client.get(reverse('showCategoryValues', kwargs=preparedKwargs))

        
        self.assertEqual(response.status_code, 200)

    def test_category_values_delete_view(self):
        preparedKwargs = {
            'mainCategoryId': self.mainCategory.id,
            'categoryId': self.category.id,
            'propertyName': self.categoryValue.propertyName
        }

        response = self.client.get(reverse('categoryValueDelete', kwargs=preparedKwargs))

        self.assertEqual(response.status_code, 200)

    def test_category_values_create(self):
        preparedKwargs = {
            'mainCategoryId': self.mainCategory.id,
            'categoryId': self.category.id
        }
        response = self.client.get(reverse('categoryValueCreate', kwargs=preparedKwargs))

        self.assertEqual(response.status_code, 200)