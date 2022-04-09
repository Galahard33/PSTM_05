from django.contrib import admin

from .. import models

# Register your models here.
# To get django model: models.<ModelName>.DjangoModel


@admin.register(models.PaintAdjustersModel.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MastersModel.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ElectriciansModel.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.KipsModel.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LocksmithsModel.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Month.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    save_as=True


@admin.register(models.NameMonth.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass