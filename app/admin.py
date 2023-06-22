from django.contrib import admin

from app.models import (
    Format,
    Material,
    Producer,
    K_B,
    Grammage,
    OzmWithForeignKey as Ozm,
    IncomeDateTime,
    T13_050WithForeignKey as T13_050,
    InvoiceWithForeignKey as Invoice,
    RollWithForeignKey as Roll,
    ConsumptionDateTime,
    ConsumptionWithForeignKey as Consumption
)


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'format',
                    'short_format',
                    )
    list_per_page = 10


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'material_type',
                    )
    list_per_page = 10


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'producer',
                    )
    list_per_page = 10


@admin.register(K_B)
class K_BAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'name',
                    'short_name',
                    )
    list_per_page = 10


@admin.register(Grammage)
class GrammageAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'grammage',
                    )
    list_per_page = 10


@admin.register(Ozm)
class OzmAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'ozm',
                    'k_b',
                    'grammage',
                    'producer',
                    'material_type',
                    )
    list_per_page = 10


@admin.register(IncomeDateTime)
class IncomeDateTimeAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'income_datetime',
                    'shift_number',
                    )
    list_per_page = 10


@admin.register(T13_050)
class T13_050Admin(admin.ModelAdmin):
    list_display = ('code',
                    'f13_050',
                    'income_datetime',
                    'pole1',
                    )
    list_per_page = 10


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'code13_050',
                    'pole1',
                    )
    list_per_page = 10


@admin.register(Roll)
class RollAdmin(admin.ModelAdmin):
    list_display = ('roll_number',
                    'roll_weight',
                    'k_b',
                    'grammage',
                    'roll_format',
                    'producer',
                    'material_type',
                    'zone',
                    'original_number',
                    'defect',
                    'vehicle',
                    'invoice',
                    'input_datetime',
                    'cert_fsc',
                    'upload_surname',
                    )
    list_per_page = 10


@admin.register(ConsumptionDateTime)
class ConsumptionDateTimeAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'consumption_datetime',
                    'shift_number',
                    'time',
                    'material_type',
                    'sum_weight',
                    'defect',
                    'pole1',
                    )
    list_per_page = 10


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'roll_number',
                    'code_datetime',
                    'pole1',
                    'pole2',
                    'pole3',
                    'pole4',
                    'pole5',
                    'material_type',
                    'zone',
                    'defect',
                    'ozm',
                    'cert_fsc',
                    'pole6',
                    'pole7',
                    )
    list_per_page = 10
