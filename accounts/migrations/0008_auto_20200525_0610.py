# Generated by Django 3.0.4 on 2020-05-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200430_1722'),
        ('records', '0003_record_record_file'),
        ('accounts', '0007_auto_20200430_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='appointments',
            field=models.ManyToManyField(blank=True, related_name='app_doc', to='appointment.appointment'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='patient_records',
            field=models.ManyToManyField(blank=True, related_name='p1', to='records.record'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
