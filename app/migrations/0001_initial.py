# Generated by Django 4.2.1 on 2023-06-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код Расход')),
                ('roll_number', models.CharField(max_length=25, null=True, verbose_name='Код № Рулона')),
                ('code_datetime', models.IntegerField(verbose_name='Код Дата расхода')),
                ('pole1', models.IntegerField(null=True, verbose_name='Поле1')),
                ('pole2', models.IntegerField(null=True, verbose_name='Поле2')),
                ('pole3', models.CharField(max_length=255, null=True, verbose_name='Поле3')),
                ('pole4', models.CharField(max_length=255, null=True, verbose_name='Поле4')),
                ('pole5', models.IntegerField(null=True, verbose_name='Поле5')),
                ('material_type', models.CharField(max_length=255, null=True, verbose_name='Тип сырья')),
                ('zone', models.CharField(max_length=255, null=True, verbose_name='Зона')),
                ('defect', models.CharField(max_length=255, null=True, verbose_name='Брак')),
                ('ozm', models.FloatField(null=True, verbose_name='ОЗМ')),
                ('cert_fsc', models.CharField(max_length=255, null=True, verbose_name='Сертификат FSC')),
                ('pole6', models.IntegerField(null=True, verbose_name='Поле6')),
                ('pole7', models.CharField(max_length=255, null=True, verbose_name='Поле7')),
            ],
            options={
                'verbose_name': 'Расход',
                'verbose_name_plural': 'Расход',
            },
        ),
        migrations.CreateModel(
            name='ConsumptionDateTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код Дата расхода')),
                ('consumption_datetime', models.DateTimeField(null=True, verbose_name='Дата расхода')),
                ('shift_number', models.CharField(max_length=25, null=True, verbose_name='№ смены')),
                ('time', models.DateTimeField(null=True, verbose_name='Время')),
                ('material_type', models.CharField(max_length=255, null=True, verbose_name='Тип сырья')),
                ('sum_weight', models.IntegerField(null=True, verbose_name='Sum-Вес нетто/брутто')),
                ('defect', models.CharField(max_length=255, null=True, verbose_name='Брак')),
                ('pole1', models.IntegerField(null=True, verbose_name='Поле 1')),
            ],
            options={
                'verbose_name': 'Дата расхода',
                'verbose_name_plural': 'Даты расхода',
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, verbose_name='Код Формат')),
                ('format', models.CharField(max_length=25, null=True, verbose_name='Формат')),
                ('short_format', models.CharField(max_length=25, null=True, verbose_name='Краткий формат')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
            },
        ),
        migrations.CreateModel(
            name='Grammage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, verbose_name='Код Граммаж')),
                ('grammage', models.CharField(max_length=25, null=True, verbose_name='Граммаж')),
            ],
            options={
                'verbose_name': 'Граммаж',
                'verbose_name_plural': 'Граммаж',
            },
        ),
        migrations.CreateModel(
            name='IncomeDateTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код Дата поступления')),
                ('income_datetime', models.DateTimeField(null=True, verbose_name='Дата поступления')),
                ('shift_number', models.CharField(max_length=25, null=True, verbose_name='№ смены')),
            ],
            options={
                'verbose_name': 'Дата поступления',
                'verbose_name_plural': 'Даты поступления',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='Код Накладная')),
                ('code13_050', models.IntegerField(null=True, verbose_name='Код 13/050')),
                ('pole1', models.CharField(max_length=255, null=True, verbose_name='Поле1')),
            ],
            options={
                'verbose_name': 'Накладная',
                'verbose_name_plural': 'Накладные',
            },
        ),
        migrations.CreateModel(
            name='K_B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, verbose_name='Код К/Б')),
                ('name', models.CharField(max_length=25, null=True, verbose_name='Название')),
                ('short_name', models.CharField(max_length=25, null=True, verbose_name='Краткое обозначение')),
            ],
            options={
                'verbose_name': 'К/Б',
                'verbose_name_plural': 'К/Б',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, verbose_name='Код Тип сырья')),
                ('material_type', models.CharField(max_length=25, null=True, verbose_name='Тип сырья')),
            ],
            options={
                'verbose_name': 'Тип сырья',
                'verbose_name_plural': 'Типы сырья',
            },
        ),
        migrations.CreateModel(
            name='Ozm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код ОЗМ')),
                ('ozm', models.CharField(max_length=25, null=True, verbose_name='ОЗМ')),
                ('k_b', models.CharField(max_length=255, null=True, verbose_name='Код К/Б')),
                ('grammage', models.CharField(max_length=25, null=True, verbose_name='Код Граммаж')),
                ('producer', models.CharField(max_length=25, null=True, verbose_name='Код Поставщик')),
                ('material_type', models.CharField(max_length=255, null=True, verbose_name='Код Тип сырья')),
            ],
            options={
                'verbose_name': 'ОЗМ',
                'verbose_name_plural': 'ОЗМ',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, verbose_name='Код Поставщик')),
                ('producer', models.CharField(max_length=25, null=True, verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=25, verbose_name='Код № Рулона')),
                ('roll_weight', models.IntegerField(null=True, verbose_name='Вес нетто/брутто')),
                ('k_b', models.CharField(max_length=25, null=True, verbose_name='Код К/Б')),
                ('grammage', models.CharField(max_length=25, null=True, verbose_name='Код Граммаж')),
                ('roll_format', models.CharField(max_length=25, null=True, verbose_name='Код Формат')),
                ('producer', models.CharField(max_length=25, null=True, verbose_name='Код Поставщик')),
                ('material_type', models.CharField(max_length=25, null=True, verbose_name='Код Тип сырья')),
                ('zone', models.CharField(max_length=25, null=True, verbose_name='Зона')),
                ('original_number', models.CharField(max_length=255, null=True, verbose_name='Исходный номер')),
                ('defect', models.CharField(max_length=25, null=True, verbose_name='Брак')),
                ('vehicle', models.CharField(max_length=255, null=True, verbose_name='Тр_средство')),
                ('invoice', models.CharField(max_length=255, null=True, verbose_name='Код Накладная')),
                ('input_datetime', models.DateTimeField(null=True, verbose_name='Дата/время ввода')),
                ('cert_fsc', models.CharField(max_length=255, null=True, verbose_name='Сертификат FSC')),
                ('upload_surname', models.CharField(max_length=255, null=True, verbose_name='Выгрузка Фамилия')),
                ('pole1', models.IntegerField(null=True, verbose_name='Поле1')),
                ('pole2', models.IntegerField(null=True, verbose_name='Поле2')),
            ],
            options={
                'verbose_name': 'Рулон',
                'verbose_name_plural': 'Рулоны',
            },
        ),
        migrations.CreateModel(
            name='T13_050',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код 13/050')),
                ('f13_050', models.CharField(max_length=25, null=True, verbose_name='13/050')),
                ('income_datetime', models.IntegerField(null=True, verbose_name='Код Дата поступления')),
                ('pole1', models.IntegerField(null=True, verbose_name='Поле 1')),
            ],
            options={
                'verbose_name': '13/050',
                'verbose_name_plural': '13/050',
            },
        ),
    ]
