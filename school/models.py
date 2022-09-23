from django.db import models
from tabnanny import check
from django.db import models

categories = (
    ('Ценные МЦ', 'Ценные МЦ'),
    ('Малоценные МЦ', 'Малоценные МЦ'),
    ('Спецодежда', 'Спецодежда'),
)
class Category(models.Model):
    title = models.CharField(max_length=60, null=False, choices=categories)

    def __str__(self):
        return self.title

# class Document(models.Model):
#     title = models.CharField('Название', max_length=100, null=False)
#     date = models.DateField('Дата')
#     note = models.TextField('Содержание')
#
#     def __str__(self):
#         return self.title + self.date

class Material(models.Model):
    """Мотериальная ценность"""
    title = models.CharField("Название", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Группа", null=False, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("Количество", null=False)
    # document = models.ForeignKey(Document, verbose_name="Номер и дата документа", null=False, on_delete=models.CASCADE)
    document = models.CharField('Документ', max_length=50, null=False)
    organization = models.CharField("Организация",  max_length=50, null=False)
    price = models.PositiveIntegerField("Стоимость за еденицу", null=False)
    size = models.CharField("Размер",  max_length=20, null=False)
    width = models.PositiveIntegerField("Ширина", null=False)
    length = models.PositiveIntegerField("Длина", null=False)
    height = models.PositiveIntegerField("Высота", null=False)
    serial = models.CharField("Серийный номер", max_length=20, null=False)
    note = models.TextField("Примечание", null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товар"

class SerialModel(models.Model):
    material = models.ForeignKey(Material, verbose_name="Товар", null=True, on_delete=models.CASCADE, blank=False)
    view_material = models.CharField("Вид товара", max_length=20, null=True, blank=True)
    numb_seral = models.CharField("Номер инвентарной карты", max_length=20, null=True, blank=True)
    face = models.CharField("Приянял МЦ", max_length=150, null=True, blank=True)
    lifetime = models.PositiveIntegerField("Срок полезного использования (мес)", null=True, blank=True)
    details = models.TextField("Описание составляющих и характеристик", null=True, blank=True)
    transfer = models.CharField("Место эксплуатации", max_length=150, null=True, blank=True)
    work = models.TextField("Описание работы", null=True, blank=True)

    def __str__(self):
        return self.material.title

