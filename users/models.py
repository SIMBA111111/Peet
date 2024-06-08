from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    first_name = models.CharField(_("Имя"), max_length=60, blank=True)
    middle_name = models.CharField(_("Фамилия"), max_length=60, )
    last_name = models.CharField(_("Отчество"), max_length=60, blank=True)
    phone_number = PhoneNumberField(_("Номер телефона"), null=True, blank=True)
    # role = 
    balance = models.DecimalField(_("Баланс"), max_digits=10, decimal_places=2)

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        db_table = _("UserModel")
        indexes = [
            models.Index(fields=["first_name", "middle_name", "last_name"], name="fio_idx"),
        ]