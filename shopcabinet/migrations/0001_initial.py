# Generated by Django 4.0.2 on 2022-03-01 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=60)),
                ('name_ru', models.CharField(max_length=60)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_uz', models.CharField(max_length=120)),
                ('subject_ru', models.CharField(max_length=120)),
                ('content_uz', models.TextField()),
                ('content_ru', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=60)),
                ('name_ru', models.CharField(max_length=60)),
                ('content_uz', models.TextField()),
                ('content_ru', models.TextField()),
                ('anons_uz', models.CharField(max_length=60)),
                ('anons_ru', models.CharField(max_length=60)),
                ('price', models.BigIntegerField()),
                ('dicount_person', models.SmallIntegerField(default=0)),
                ('dicount_start', models.DateTimeField(default=None, null=True)),
                ('dicount_end', models.DateTimeField(default=None, null=True)),
                ('availability', models.IntegerField(default=0)),
                ('vendor_code', models.CharField(max_length=20)),
                ('photo0', models.ImageField(upload_to='')),
                ('photo1', models.ImageField(upload_to='')),
                ('photo2', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('availability', models.IntegerField(default=0)),
                ('used', models.IntegerField(default=0)),
                ('discount', models.SmallIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=60)),
                ('name_ru', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.SmallIntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='availability_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.unit'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.category'),
        ),
        migrations.CreateModel(
            name='PostCommit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.postcommit')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.post')),
            ],
        ),
    ]