# Generated by Django 4.0.2 on 2023-08-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0011_alter_category_image_alter_item_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_zone',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
