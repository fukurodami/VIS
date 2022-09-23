# Generated by Django 4.1.1 on 2022-09-23 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_serialmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialmodel',
            name='details',
            field=models.TextField(blank=True, null=True, verbose_name='Описание составляющих и характеристик'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='face',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Приянял МЦ'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='lifetime',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Срок полезного использования (мес)'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.material', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='numb_seral',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер инвентарной карты'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='transfer',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Место эксплуатации'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='view_material',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Вид товара'),
        ),
        migrations.AlterField(
            model_name='serialmodel',
            name='work',
            field=models.TextField(blank=True, null=True, verbose_name='Описание работы'),
        ),
    ]