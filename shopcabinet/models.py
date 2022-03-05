from django.db import models
# from aldryn_translation_tools.models import TranslationHelperMixin
from django.utils.translation import get_language


class TranslateHelperMixin:
    def __getattr__(self, item):
        if item in self.translate_fields:
            lang = get_language()
            return getattr(self, '{}_{}'.format(item, lang))
        return super(TranslateHelperMixin, self).__getattr__(item)



class Review(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, default=None, blank=True)
    name_uz = models.CharField(max_length=60)
    name_ru = models.CharField(max_length=60)

    @property
    def children(self):
        return Category.objects.filter(parent=self).all()

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name_uz


class Unit(models.Model):
    name_uz = models.CharField(max_length=60)
    name_ru = models.CharField(max_length=60)

    class Meta:
        verbose_name = "O'lchov birligi"
        verbose_name_plural = "O'lchov birliglari"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    availability_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=60)
    name_ru = models.CharField(max_length=60)
    content_uz = models.TextField()
    content_ru = models.TextField()
    anons_uz = models.CharField(max_length=60)
    anons_ru = models.CharField(max_length=60)
    price = models.BigIntegerField()
    dicount_person = models.SmallIntegerField(default=0)
    dicount_start = models.DateTimeField(default=None, null=True)
    dicount_end = models.DateTimeField(default=None, null=True)
    availability = models.IntegerField(default=0)
    vendor_code = models.CharField(max_length=20)
    photo0 = models.ImageField()
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class ProductReview(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    star = models.SmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mahsulot izohi"
        verbose_name_plural = "Mahsulot izohlari"


class PromoCode(models.Model):
    code = models.CharField(max_length=25, primary_key=True)
    availability = models.IntegerField(default=0)
    used = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=10)

    class Meta:
        verbose_name = "Promo kod"
        verbose_name_plural = "Promo kodlar"


class Setting(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.TextField()

    class Meta:
        verbose_name = "Sozlash"
        verbose_name_plural = "Sozlashlar"


class Post(models.Model, TranslateHelperMixin):
    POST_STATUS = (
        (1, "Faol"),
        (2, "Nofaol")
    )
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT, null=True, blank=True)
    subject_uz = models.CharField(max_length=120)
    subject_ru = models.CharField(max_length=120)
    content_uz = models.TextField()
    content_ru = models.TextField()
    photo = models.ImageField(upload_to='media')
    status = models.SmallIntegerField(choices=POST_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    translate_fields = ['subject', 'content']

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"


class PostCommit(models.Model):
    parent = models.ForeignKey('PostCommit', on_delete=models.RESTRICT, null=True, default=None)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Maqola izohi"
        verbose_name_plural = "Maqola izohlari"


