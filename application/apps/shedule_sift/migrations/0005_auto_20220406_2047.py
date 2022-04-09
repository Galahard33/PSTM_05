# Generated by Django 3.2.12 on 2022-04-06 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shedule_sift', '0004_auto_20220406_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_month', models.CharField(max_length=100, verbose_name='День месяца')),
                ('month', models.SmallIntegerField(verbose_name='Номер месяца')),
                ('electrician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrical_relation', to='shedule_sift.electriciansmodel', verbose_name='Электрик')),
                ('electrician1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrical_relation1', to='shedule_sift.electriciansmodel', verbose_name='Электрик')),
                ('electrician2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrical_relation2', to='shedule_sift.electriciansmodel', verbose_name='Электрик')),
                ('electrician3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrical_relation3', to='shedule_sift.electriciansmodel', verbose_name='Электрик')),
                ('electrician4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrical_relation4', to='shedule_sift.electriciansmodel', verbose_name='Электрик')),
                ('kip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kip_relation', to='shedule_sift.kipsmodel', verbose_name='Киповец')),
                ('locksmith', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locksmith_relation', to='shedule_sift.locksmithsmodel', verbose_name='Слесарь')),
                ('locksmith1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locksmith_relation1', to='shedule_sift.locksmithsmodel', verbose_name='Слесарь')),
                ('locksmith2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locksmith_relation2', to='shedule_sift.locksmithsmodel', verbose_name='Слесарь')),
                ('locksmith3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locksmith_relation3', to='shedule_sift.locksmithsmodel', verbose_name='Слесарь')),
                ('locksmith4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locksmith_relation4', to='shedule_sift.locksmithsmodel', verbose_name='Слесарь')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_relation', to='shedule_sift.mastersmodel', verbose_name='Мастер')),
                ('paint_adjuster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paint_relation', to='shedule_sift.paintadjustersmodel', verbose_name='Красковар')),
            ],
            options={
                'db_table': 'month',
            },
        ),
        migrations.DeleteModel(
            name='Month1',
        ),
    ]