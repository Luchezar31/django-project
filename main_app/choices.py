from django.db import models


class BrandChoices(models.TextChoices):
    ASUS = 'Asus', 'Asus'
    ACER = 'Acer', 'Acer'
    APPLE = 'Apple', 'Apple'
    LENOVO = 'Lenovo', 'Lenovo'
    DELL = 'Dell', 'Dell'


class OperationSystemChoices(models.TextChoices):
    WINDOWS = 'Windows', 'Windows'
    MACOS = 'MacOS', 'MacOS'
    LINUX = 'Linux', 'Linux'
    CHROMEOS = 'Chrome OS', 'Chrome OS'