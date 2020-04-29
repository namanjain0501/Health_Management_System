# Generated by Django 3.0.4 on 2020-04-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200429_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='qualification_proof',
            new_name='specialization_proof',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='own_records',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='qualifications',
        ),
        migrations.AddField(
            model_name='doctor',
            name='locality',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]