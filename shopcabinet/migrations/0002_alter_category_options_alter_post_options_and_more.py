# Generated by Django 4.0.2 on 2022-03-01 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopcabinet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
        migrations.AlterModelOptions(
            name='postcommit',
            options={'verbose_name': 'Maqola izohi', 'verbose_name_plural': 'Maqola izohlari'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Mahsulot', 'verbose_name_plural': 'Mahsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name': 'Mahsulot izohi', 'verbose_name_plural': 'Mahsulot izohlari'},
        ),
        migrations.AlterModelOptions(
            name='promocode',
            options={'verbose_name': 'Promo kod', 'verbose_name_plural': 'Promo kodlar'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Izoh', 'verbose_name_plural': 'Izohlar'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Sozlash', 'verbose_name_plural': 'Sozlashlar'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': "O'lchov birligi", 'verbose_name_plural': "O'lchov birliglari"},
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='shopcabinet.category'),
        ),
    ]
