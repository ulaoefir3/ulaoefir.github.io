# Generated by Django 4.2.1 on 2023-12-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_equipmentmanufacturer_filtervalue_namefilter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Значение фильтра:')),
            ],
            options={
                'verbose_name': 'Сервисные центры',
                'verbose_name_plural': 'Сервисные центры',
            },
        ),
        migrations.AlterModelOptions(
            name='equipmentmanufacturer',
            options={'verbose_name': 'Производитель оборудования', 'verbose_name_plural': 'Производитель оборудования'},
        ),
        migrations.AlterModelOptions(
            name='filtervalue',
            options={'verbose_name': 'Значение фильтра', 'verbose_name_plural': 'Значение фильтра'},
        ),
        migrations.AlterModelOptions(
            name='namefilter',
            options={'verbose_name': 'Название фильтра', 'verbose_name_plural': 'Название фильтра'},
        ),
        migrations.AlterField(
            model_name='equipmentmanufacturer',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Производитель:'),
        ),
        migrations.AlterField(
            model_name='filtervalue',
            name='value',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Значение фильтра:'),
        ),
        migrations.AlterField(
            model_name='namefilter',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название фильтра:'),
        ),
    ]
