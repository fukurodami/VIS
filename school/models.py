from django.db import models
from tabnanny import check
from django.db import models

class Material(models.Model):
    """Мотериальная ценность
    группа
    количество
    намер и дата документа
    организация
    стоимость за 1 ед
    размер ширина длина высота серийный номер
    примечание
    индивидуальные характеристики: название количество характеристика
    сведения о перемещении: вид операици остаточная стоимость МОЛ помещение
    ремонт\модернизация: вид работ дата описание акт работ"""

    title = models.CharField("Название", max_length=100)
    category = models.CharField("Группа",  max_length=20, null=True)
    amount = models.PositiveIntegerField("Количество", null=True)
    document = models.CharField("Номер и дата документа",  max_length=100, null=True)
    organization = models.CharField("Организация",  max_length=50, null=True)
    price = models.PositiveIntegerField("Стоимость за еденицу", null=True)
    size = models.CharField("Размер",  max_length=20, null=True)
    width = models.PositiveIntegerField("Ширина", null=True)
    length = models.PositiveIntegerField("Длина", null=True)
    height = models.PositiveIntegerField("Высота", null=True)
    serial = models.CharField("Серийный номер", max_length=20, null=True)
    note = models.TextField("Примечание", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товар"