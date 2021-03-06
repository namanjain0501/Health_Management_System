# Generated by Django 3.0.4 on 2020-05-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200525_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='num_reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization_proof',
            field=models.FileField(blank=True, upload_to='specialization_proofs'),
        ),
    ]
