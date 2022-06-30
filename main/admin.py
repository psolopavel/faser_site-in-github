from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import Category, Salesman, Shop_name, Product, product_Shorts, Rating_star, Rating, Reviews, Purchase
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductAdminForm(forms.ModelForm):
    descriptin_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    descriptin_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name','description','url', 'id')

class ReviewsInlaine(admin.TabularInline):
    model = Reviews
    extra = 1


class ProductShortsInlayn(admin.TabularInline):
    model = product_Shorts
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
    get_image.shorts_description = 'Изоброжение'


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'Shop_name', 'url', 'draft')
    search_fields = ('title', 'Shop_name__name')
    readonly_fields = ('get_image',)
    inlines = [ProductShortsInlayn, ReviewsInlaine]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ['publish','unpublish']
    form = ProductAdminForm
    fieldsets = (
        (None,{
            'fields': (( 'title', 'price'),)
        }),
        (None, {
            'fields': ('descriptin', ('poster','get_image'),)
        }),
        (None, {
            'fields': (('category', 'Shop_name','salesman','number'),)
        }),
        (None, {
            'fields': ('url', 'draft')
        })

    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = 'Постер'

    def unpublish(self, request, queryset):

        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} запесей обновленио'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):

        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} запесей обновлени'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'опубликовать'
    publish.allowed_permission = ('change',)

    unpublish.short_description = 'снять публикаций'
    unpublish.allowed_permission = ('change',)

    get_image.short_description = 'Постер'



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'parent')
    readonly_fields = ('name', 'email')
    inlines = [ReviewsInlaine]

@admin.register(Salesman)
class SalesmanAdmin(TranslationAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
    get_image.shorts_description = 'Изоброжение'


@admin.register(Shop_name)
class Shop_nameAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(product_Shorts)
class product_ShortsAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'get_image', 'id', 'product')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.shorts_description = 'Изоброжение'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'product')

admin.site.register(Rating_star)

admin.site.site_title = 'Папин сайт'
admin.site.site_header = 'Папин сайт'
# Register your models here.

admin.site.register(Purchase)