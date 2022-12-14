# Generated by Django 4.1.1 on 2022-09-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товар'},
        ),
        migrations.AddField(
            model_name='material',
            name='amount',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='material',
            name='document',
            field=models.CharField(max_length=100, null=True, verbose_name='Номер и дата документа'),
        ),
        migrations.AddField(
            model_name='material',
            name='height',
            field=models.PositiveIntegerField(null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='material',
            name='length',
            field=models.PositiveIntegerField(null=True, verbose_name='Длина'),
        ),
        migrations.AddField(
            model_name='material',
            name='note',
            field=models.TextField(null=True, verbose_name='Примечание'),
        ),
        migrations.AddField(
            model_name='material',
            name='organization',
            field=models.CharField(max_length=50, null=True, verbose_name='Организация'),
        ),
        migrations.AddField(
            model_name='material',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Стоимость за еденицу'),
        ),
        migrations.AddField(
            model_name='material',
            name='serial',
            field=models.CharField(max_length=20, null=True, verbose_name='Серийный номер'),
        ),
        migrations.AddField(
            model_name='material',
            name='size',
            field=models.CharField(max_length=20, null=True, verbose_name='Размер'),
        ),
        migrations.AddField(
            model_name='material',
            name='width',
            field=models.PositiveIntegerField(null=True, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.CharField(max_length=20, null=True, verbose_name='Группа'),
        ),
    ]
