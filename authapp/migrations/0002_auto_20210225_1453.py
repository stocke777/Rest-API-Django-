# Generated by Django 3.1.5 on 2021-02-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite',
            field=models.TextField(),
        ),
    ]