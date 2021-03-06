# Generated by Django 4.0 on 2022-04-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0010_remove_product_category_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Category_image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('Category_description', models.TextField(blank=True, null=True)),
                ('Category_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
    ]
