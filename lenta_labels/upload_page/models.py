from django.db import models


# модель для хранения файла на сервере
class UploadFile(models.Model):
    file = models.FileField(upload_to='documents/uploads/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# модель для хранения информации о товаре
class Product(models.Model):
    sap_number = models.BigIntegerField(verbose_name='SAP номер')
    ean_psc = models.BigIntegerField(verbose_name='EAN код изделия')
    ean_ctn = models.BigIntegerField(verbose_name='EAN код коробки изделия')
    manufacturer = models.CharField(verbose_name='Изготовитель, который  '
                                                 'указан на этикетке',
                                    max_length=400, help_text='Не более 400 '
                                                              'символов')
    real_manufacturer = models.CharField(verbose_name='Адрес реального '
                                                      'изготовителя',
                                         max_length=400,
                                         help_text='Не более 400 символов')
    article = models.CharField(verbose_name='Артикул', max_length=20,
                               help_text='Не более 20 символов')
    name = models.CharField(verbose_name='Наименование товара',
                            max_length=100, help_text='Не более 100 символов')
    size = models.CharField(verbose_name='Размер', max_length=20,
                            help_text='Не более 20 символов')
    brand = models.CharField(verbose_name='Бренд',
                             max_length=50, help_text='Не более 20 символов')
    materials = models.CharField(verbose_name='Материал изготовления',
                                 max_length=1000, help_text='Не более 1000 '
                                                            'символов')
    country_of_origin = models.CharField(verbose_name='Страна происхождения',
                                         max_length=60, help_text='Не более ' \
                                                                  '60 '
                                                                  'символов')

    def __str__(self):
        return f"{self.article} {self.name} {self.size} {self.brand}"
    # Метод __str__ определен, чтобы при выводе объектов модели в консоли
    # или на странице администратора Django, выводилась строка с артикулом и
    # названием товара.
