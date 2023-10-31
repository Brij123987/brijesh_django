# Generated by Django 4.2.5 on 2023-10-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_cusorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusRatingFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_code', models.IntegerField(default=1)),
                ('ratings', models.FloatField()),
                ('feedback', models.CharField(max_length=200)),
                ('user_name', models.CharField(default='username', max_length=200)),
                ('user_type', models.CharField(default='Cust', max_length=200)),
            ],
        ),
    ]