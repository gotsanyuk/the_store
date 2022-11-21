from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.safestring import mark_safe

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_show', 'name', 'price', 'status', 'updated', 'created')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'category', 'created')
    list_editable = ('price', 'status')
    raw_id_fields = ('category',)
    actions = ('change_status',)

    @admin.action(description='change status of model')
    def change_status(self, request, queryset):
        rows_count = queryset.update(status=True)
        self.message_user(request, f'{rows_count} status has changed')

    def image_show(self, obj):
        if obj.image_url:
            return mark_safe("<img src='{}' width='60' />".format(obj.image_url))
        return 'None'

    image_show.__name__ = 'Зображення'