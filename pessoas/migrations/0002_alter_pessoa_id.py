# Generated by Django 3.2.15 on 2022-09-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
