from modeltranslation.translator import register, TranslationOptions
from .models import Category, Salesman, Product, product_Shorts

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Salesman)
class SalesmanTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptin')


@register(product_Shorts)
class product_ShortsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

