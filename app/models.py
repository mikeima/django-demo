from django.db import models


class Format(models.Model):
    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'

    code = models.CharField(max_length=25,
                            verbose_name='Код Формат',
                            unique = True)
    format = models.CharField(max_length=25,
                              verbose_name='Формат',
                              null=True)
    short_format = models.CharField(max_length=25,
                                    verbose_name='Краткий формат',
                                    null=True)

    def __str__(self):
        return f'{self.format}'


class Material(models.Model):
    class Meta:
        verbose_name = 'Тип сырья'
        verbose_name_plural = 'Типы сырья'

    code = models.CharField(max_length=25,
                            verbose_name='Код Тип сырья',
                            unique=True)
    material_type = models.CharField(max_length=25,
                                     verbose_name='Тип сырья',
                                     null=True)

    def __str__(self):
        return f'{self.material_type}'


class Producer(models.Model):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    code = models.CharField(max_length=25,
                            verbose_name='Код Поставщик',
                            unique=True)
    producer = models.CharField(max_length=25,
                                verbose_name='Поставщик',
                                null=True)

    def __str__(self):
        return f'{self.producer}'


class K_B(models.Model):
    class Meta:
        verbose_name = 'К/Б'
        verbose_name_plural = 'К/Б'

    code = models.CharField(max_length=25,
                            verbose_name='Код К/Б',
                            unique=True)
    name = models.CharField(max_length=25,
                            verbose_name='Название',
                            null=True)
    short_name = models.CharField(max_length=25,
                                  verbose_name='Краткое обозначение',
                                  null=True)

    def __str__(self):
        return f'{self.name}'


class Grammage(models.Model):
    class Meta:
        verbose_name = 'Граммаж'
        verbose_name_plural = 'Граммаж'

    code = models.CharField(max_length=25,
                            verbose_name='Код Граммаж',
                            unique=True)
    grammage = models.CharField(max_length=25,
                                verbose_name='Граммаж',
                                null=True)

    def __str__(self):
        return f'{self.grammage}'


class Ozm(models.Model):
    class Meta:
        verbose_name = 'ОЗМ'
        verbose_name_plural = 'ОЗМ'

    code = models.IntegerField(verbose_name='Код ОЗМ',
                               unique=True)
    ozm = models.CharField(max_length=25,
                           verbose_name='ОЗМ',
                           null=True)
    k_b = models.CharField(max_length=255,
                           verbose_name='Код К/Б',
                           null=True)
    grammage = models.CharField(max_length=25,
                                verbose_name='Код Граммаж',
                                null=True)
    producer = models.CharField(max_length=25,
                                verbose_name='Код Поставщик',
                                null = True)
    material_type = models.CharField(max_length=255,
                                     verbose_name='Код Тип сырья',
                                     null=True)

    def __str__(self):
        return f'{self.ozm}'


class IncomeDateTime(models.Model):
    class Meta:
        verbose_name = 'Дата поступления'
        verbose_name_plural = 'Даты поступления'

    code = models.IntegerField(verbose_name='Код Дата поступления',
                               unique=True)
    income_datetime = models.DateTimeField(verbose_name='Дата поступления',
                                           null=True)
    shift_number = models.CharField(max_length=25,
                                    verbose_name='№ смены',
                                    null=True)

    def __str__(self):
        return f'{self.income_datetime}'


class T13_050(models.Model):
    class Meta:
        verbose_name = '13/050'
        verbose_name_plural = '13/050'

    code = models.IntegerField(verbose_name='Код 13/050',
                               unique=True)
    f13_050 = models.CharField(max_length=25,
                               verbose_name='13/050',
                               null=True)
    income_datetime = models.IntegerField(verbose_name='Код Дата поступления',
                                          null=True)
    pole1 = models.IntegerField(verbose_name='Поле 1',
                                null=True)

    def __str__(self):
        return f'{self.f13_050}'


class Invoice(models.Model):
    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'

    code = models.CharField(max_length=255,
                            verbose_name='Код Накладная',
                            unique=True)
    code13_050 = models.IntegerField(verbose_name='Код 13/050',
                                     null=True)
    pole1 = models.CharField(max_length=255,
                             verbose_name='Поле1',
                             null=True)

    def __str__(self):
        return f'{self.code}'


class Roll(models.Model):
    class Meta:
        verbose_name = 'Рулон'
        verbose_name_plural = 'Рулоны'

    roll_number = models.CharField(max_length=25,
                                   verbose_name='Код № Рулона',
                                   unique=True)
    roll_weight = models.IntegerField(verbose_name='Вес нетто/брутто',
                                      null=True)
    k_b = models.CharField(max_length=25,
                           verbose_name='Код К/Б',
                           null=True)
    grammage = models.CharField(max_length=25,
                                verbose_name='Код Граммаж',
                                null=True)
    roll_format = models.CharField(max_length=25,
                                   verbose_name='Код Формат',
                                   null=True)
    producer = models.CharField(max_length=25,
                                verbose_name='Код Поставщик',
                                null=True)
    material_type = models.CharField(max_length=25,
                                     verbose_name='Код Тип сырья',
                                     null=True)
    zone = models.CharField(max_length=25,
                            verbose_name='Зона',
                            null=True)
    original_number = models.CharField(max_length=255,
                                       verbose_name='Исходный номер',
                                       null=True)
    defect = models.CharField(max_length=25,
                              verbose_name='Брак',
                              null=True)
    vehicle = models.CharField(max_length=255,
                               verbose_name='Тр_средство',
                               null=True)
    invoice = models.CharField(max_length=255,
                               verbose_name='Код Накладная',
                               null=True)
    input_datetime = models.DateTimeField(verbose_name='Дата/время ввода',
                                          null=True)
    cert_fsc = models.CharField(max_length=255,
                                verbose_name='Сертификат FSC',
                                null=True)
    upload_surname = models.CharField(max_length=255,
                                      verbose_name='Выгрузка Фамилия',
                                      null=True)
    pole1 = models.IntegerField(verbose_name='Поле1',
                                null=True)
    pole2 = models.IntegerField(verbose_name='Поле2',
                                null=True)

    def __str__(self):
        return f'{self.roll_number}'


class ConsumptionDateTime(models.Model):
    class Meta:
        verbose_name = 'Дата расхода'
        verbose_name_plural = 'Даты расхода'

    code = models.IntegerField(verbose_name='Код Дата расхода',
                               unique=True)
    consumption_datetime = models.DateTimeField(verbose_name='Дата расхода',
                                                null=True)
    shift_number = models.CharField(max_length=25,
                                    verbose_name='№ смены',
                                    null=True)
    time = models.DateTimeField(verbose_name='Время',
                                null=True)
    material_type = models.CharField(max_length=255,
                                     verbose_name='Тип сырья',
                                     null=True)
    sum_weight = models.IntegerField(verbose_name='Sum-Вес нетто/брутто',
                                     null=True)
    defect = models.CharField(max_length=255,
                              verbose_name='Брак',
                              null=True)
    pole1 = models.IntegerField(verbose_name='Поле 1',
                                null=True)

    def __str__(self):
        return f'{self.consumption_datetime}'


class Consumption(models.Model):
    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расход'

    code = models.IntegerField(verbose_name='Код Расход',
                               unique=True)
    roll_number = models.CharField(max_length=25,
                                   verbose_name='Код № Рулона',
                                   null=True)
    code_datetime = models.IntegerField(verbose_name='Код Дата расхода')
    pole1 = models.IntegerField(verbose_name='Поле1',
                                null=True)
    pole2 = models.IntegerField(verbose_name='Поле2',
                                null=True)
    pole3 = models.CharField(max_length=255,
                             verbose_name='Поле3',
                             null=True)
    pole4 = models.CharField(max_length=255,
                             verbose_name='Поле4',
                             null=True)
    pole5 = models.IntegerField(verbose_name='Поле5',
                                null=True)
    material_type = models.CharField(max_length=255,
                                     verbose_name='Тип сырья',
                                     null=True)
    zone = models.CharField(max_length=255,
                            verbose_name='Зона',
                            null=True)
    defect = models.CharField(max_length=255,
                              verbose_name='Брак',
                              null=True)
    ozm = models.FloatField(verbose_name='ОЗМ',
                            null=True)
    cert_fsc = models.CharField(max_length=255,
                                verbose_name='Сертификат FSC',
                                null=True)
    pole6 = models.IntegerField(verbose_name='Поле6',
                                null=True)
    pole7 = models.CharField(max_length=255,
                             verbose_name='Поле7',
                             null=True)

    def __str__(self):
        return f'{self.code}'
