# Generated by Django 4.2.4 on 2023-09-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='for_user',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eveniet, et iste earum error consequuntur aspernatur aperiam similique natus voluptate repellat assumenda sapiente. Deleniti, natus molestias. Necessitatibus provident quis officiis dolor.', max_length=500),
        ),
    ]
