# Generated by Django 3.1.12 on 2021-06-08 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questioncategory',
            options={'verbose_name_plural': 'Question Categories'},
        ),
    ]