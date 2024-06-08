from django.db import models
from django.utils.translation import gettext_lazy as _


class GoodsModel(models.Model):
    name = models.CharField(_("Название товара"), max_length=100)
    price = models.DecimalField(_("Цена товара"), max_digits=12, decimal_places=2, default=0)
    # category =
    # image =
    count_goods = models.SmallIntegerField(_("Кол-во товара"), default=0)
    description = models.TextField(_("Описание товара"))