# Generated by Django 4.1.1 on 2022-09-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_document_alter_material_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='document',
            field=models.CharField(max_length=50, verbose_name='Документ'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]