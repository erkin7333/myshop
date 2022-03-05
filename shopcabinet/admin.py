from django.contrib import admin
from .models import Unit, Category, PromoCode, Setting, Post
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'is_staff',
        'is_superuser'
    ]
    class Meta:
        model = User
admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'parent',
        'name_uz',
        'name_ru'
    ]
    list_display = [
        'id',
        'parent',
        'name_uz',
        'name_ru',
    ]
    def name(self, row):
        return row.name

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_uz',
        'name_ru'
    ]
    class Meta:
        model = Unit

admin.site.register(Unit, UnitAdmin)


class SettingAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]
    class Meta:
        model = Setting

admin.site.register(Setting, SettingAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'subject_ru'
    ]
    def subject_ru(self, row):
        return row.subject_ru

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)