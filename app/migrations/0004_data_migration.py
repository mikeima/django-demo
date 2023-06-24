from django.db import migrations

import logging
logger = logging.getLogger('default')


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.MultipleObjectsReturned as e:
        logger.error(e)
        return None
    except model.DoesNotExist as e:
        key = None
        for value in kwargs.values():
            key = value
        logger.error(f'\t\t"{key}": {e}')
        return None


def copy_ozm_with_fk(apps, schema_editor):
    logger.info('\n\tCopying from Ozm to OzmWithForeignKey...')
    ozm_new = apps.get_model('app', 'OzmWithForeignKey')
    ozm = apps.get_model('app', 'Ozm')
    k_b = apps.get_model('app', 'K_B')
    grammage = apps.get_model('app', 'Grammage')
    producer = apps.get_model('app', 'Producer')
    material = apps.get_model('app', 'Material')
    for item in ozm.objects.all():
        ozm_new.objects.get_or_create(
            code=item.code,
            ozm=item.ozm,
            k_b=k_b.objects.get(code=item.k_b),
            grammage=get_or_none(grammage, code=item.grammage),
            producer=get_or_none(producer, code=item.producer),
            material_type=get_or_none(material, code=item.material_type)
        )


def copy_13_050_with_fk(apps, schema_editor):
    logger.info('\tCopying from T13_050 to T13_050WithForeignKey...')
    t13_050_new = apps.get_model('app', 'T13_050WithForeignKey')
    t13_050 = apps.get_model('app', 'T13_050')
    income_datetime = apps.get_model('app', 'IncomeDateTime')
    for item in t13_050.objects.all():
        t13_050_new.objects.get_or_create(
            code=item.code,
            f13_050=item.f13_050,
            income_datetime=get_or_none(income_datetime, code=item.income_datetime),
            pole1=item.pole1
        )


def copy_invoice_with_fk(apps, schema_editor):
    logger.info('\tCopying from Invoice to InvoiceWithForeignKey...')
    invoice_new = apps.get_model('app', 'InvoiceWithForeignKey')
    invoice = apps.get_model('app', 'Invoice')
    t13_050 = apps.get_model('app', 'T13_050WithForeignKey')
    for item in invoice.objects.all():
        invoice_new.objects.get_or_create(
            code=item.code,
            code13_050=get_or_none(t13_050, code=item.code13_050),
            pole1=item.pole1
        )


def copy_rolls_with_fk(apps, schema_editor):
    logger.info('\tCopying from Roll to RollWithForeignKey...')
    roll_new = apps.get_model('app', 'RollWithForeignKey')
    roll = apps.get_model('app', 'Roll')
    k_b = apps.get_model('app', 'K_B')
    grammage = apps.get_model('app', 'Grammage')
    roll_format = apps.get_model('app', 'Format')
    producer = apps.get_model('app', 'Producer')
    material = apps.get_model('app', 'Material')
    invoice = apps.get_model('app', 'InvoiceWithForeignKey')
    for item in roll.objects.all():
        roll_new.objects.get_or_create(
            roll_number=item.roll_number,
            roll_weight=item.roll_weight,
            k_b=get_or_none(k_b, code=item.k_b),
            grammage=get_or_none(grammage, code=item.grammage),
            roll_format=get_or_none(roll_format, code=item.roll_format),
            producer=get_or_none(producer, code=item.producer),
            material_type=get_or_none(material, code=item.material_type),
            zone=item.zone,
            original_number=item.original_number,
            defect=item.defect,
            vehicle=item.vehicle,
            invoice=get_or_none(invoice, code=item.invoice),
            input_datetime=item.input_datetime,
            cert_fsc=item.cert_fsc,
            upload_surname=item.upload_surname,
            pole1=item.pole1,
            pole2=item.pole2)


def copy_consumption_with_fk(apps, schema_editor):
    logger.info('\tCopying from Consumption to ConsumptionWithForeignKey...')
    consumption_new = apps.get_model('app', 'ConsumptionWithForeignKey')
    consumption = apps.get_model('app', 'Consumption')
    roll = apps.get_model('app', 'RollWithForeignKey')
    consumption_datetime = apps.get_model('app', 'ConsumptionDateTime')
    for item in consumption.objects.all():
        consumption_new.objects.get_or_create(
            code=item.code,
            roll_number=get_or_none(roll, roll_number=item.roll_number),
            code_datetime=get_or_none(consumption_datetime, code=item.code_datetime),
            pole1=item.pole1,
            pole2=item.pole2,
            pole3=item.pole3,
            pole4=item.pole4,
            pole5=item.pole5,
            material_type=item.material_type,
            zone=item.zone,
            defect=item.defect,
            ozm=item.ozm,
            cert_fsc=item.cert_fsc,
            pole6=item.pole6,
            pole7=item.pole7)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_create_tables_with_foreign_keys'),
    ]

    operations = [
        migrations.RunPython(copy_ozm_with_fk),
        migrations.RunPython(copy_13_050_with_fk),
        migrations.RunPython(copy_invoice_with_fk),
        migrations.RunPython(copy_rolls_with_fk),
        migrations.RunPython(copy_consumption_with_fk),
    ]
