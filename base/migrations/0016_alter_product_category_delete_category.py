# Generated by Django 4.0 on 2022-05-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
