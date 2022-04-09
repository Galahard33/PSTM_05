from orm_converter.tortoise_to_django import ConvertedModel
from tortoise import Tortoise, fields
from tortoise.models import Model


class LocksmithsModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255, description='ФИО')
    phone = fields.CharField(max_length=40, description='Телефон', default='-')
    shift: fields.ReverseRelation["Month"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "locksmith"


class ElectriciansModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255, description='ФИО')
    phone = fields.CharField(max_length=40, description='Телефон', default='-')
    shift: fields.ReverseRelation["Month"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "electrician"


class KipsModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255, description='ФИО')
    phone = fields.CharField(max_length=40, description='Телефон', default='-')
    shift: fields.ReverseRelation["Month"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "kip"


class PaintAdjustersModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255, description='ФИО')
    phone = fields.CharField(max_length=40, description='Телефон', default='-')
    shift: fields.ReverseRelation["Month"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "paint_adjuster"


class MastersModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255, description='ФИО')
    phone = fields.CharField(max_length=40, description='Телефон', default='-')
    shift: fields.ReverseRelation["Month"]

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "masters"


class Month(Model, ConvertedModel):
    day_month = fields.SmallIntField(description='День месяца')
    month = fields.SmallIntField (description='Номер месяца')
    shift = fields.SmallIntField(description='Смена')
    locksmith: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                   related_name="locksmith_relation",
                                                                                   null=True,description='Слесарь')
    locksmith1: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation1",
                                                                                    null=True, description="Слесарь")
    locksmith2: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation2",
                                                                                    null=True, description='Слесарь')
    locksmith3: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation3",
                                                                                    null=True, description='Слесарь')
    locksmith4: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation4",
                                                                                    null=True, description='Слесарь')
    locksmith5: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation5",
                                                                                    null=True, description='Слесарь')
    locksmith6: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation6",
                                                                                    null=True, description='Слесарь')
    locksmith7: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation7",
                                                                                    null=True, description='Слесарь')
    locksmith8: fields.ForeignKeyRelation[LocksmithsModel] = fields.ForeignKeyField("shedule_sift.LocksmithsModel",
                                                                                    related_name="locksmith_relation8",
                                                                                    null=True, description='Слесарь')
    electrician: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField("shedule_sift.ElectriciansModel",
                                                                                       related_name='electrical_relation',
                                                                                       null=True, description='Электрик')
    electrician1: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation1',
        null=True, description='Электрик')
    electrician2: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation2',
        null=True, description='Электрик')
    electrician3: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation3',
        null=True, description='Электрик')
    electrician4: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation4',
        null=True, description='Электрик')
    electrician5: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation5',
        null=True, description='Электрик')
    electrician6: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation6',
        null=True, description='Электрик')
    electrician7: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation7',
        null=True, description='Электрик')
    electrician8: fields.ForeignKeyRelation[ElectriciansModel] = fields.ForeignKeyField(
        "shedule_sift.ElectriciansModel",
        related_name='electrical_relation8',
        null=True, description='Электрик')
    kip: fields.ForeignKeyRelation[KipsModel] = fields.ForeignKeyField("shedule_sift.KipsModel",
                                                                       related_name='kip_relation', null=True, description='Киповец')
    paint_adjuster: fields.ForeignKeyRelation[PaintAdjustersModel] = fields.ForeignKeyField(
        "shedule_sift.PaintAdjustersModel", related_name='paint_relation', null=True, description='Красковар')
    master: fields.ForeignKeyRelation[MastersModel] = fields.ForeignKeyField('shedule_sift.MastersModel',
                                                                             related_name='master_relation', description='Мастер')

    def __str__(self) -> str:
        return f"{self.day_month} '   ' {self.month} '' {self.shift}"

    class Meta:
        table = "month"


class NameMonth(Model, ConvertedModel):
    name = fields.CharField(max_length=150, description='Название месяца')
    numbr = fields.SmallIntField(description='Номер месяца')

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "NameMonth"


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.shedule_sift.models"],
        app_label="shedule_sift",
        _init_relations=False,
    )
