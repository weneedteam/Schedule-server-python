# Generated by Django 2.1.5 on 2019-01-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0002_auto_20190106_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='holiday',
            options={'ordering': ('year', 'month', 'day')},
        ),
        migrations.AlterField(
            model_name='holiday',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]