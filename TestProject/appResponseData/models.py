from django.db import models
import random
import datetime
from .utils import generate_number


class GenerateTab(models.Model):
    number = models.PositiveIntegerField("Число", null=False, default=generate_number)
    status = models.BooleanField("Разрешение", null=False, default=True)
    help_text = "Да (Активный) / Нет (Неактивный)"

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "число"
        verbose_name_plural = "Числа"


class GenerateData(models.Model):
    date_time = models.DateTimeField(
        "Дата и время", null=False, default=datetime.datetime.now, editable=False
    )

    status = models.BooleanField(
        "Разрешение",
        null=True,
        blank=True,
        default=True,
        help_text="Да (Активный) / Нет (Неактивный)",
    )

    def __str__(self):
        return str(self.date_time)

    class Meta:
        verbose_name = "дату и время"
        verbose_name_plural = "Дата и время"
