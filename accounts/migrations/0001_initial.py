# Generated by Django 3.0.4 on 2020-04-29 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('records', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('blood_group', models.CharField(blank=True, choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=4)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('address', models.TextField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('records', models.ManyToManyField(to='records.record')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('adhaar_num', models.CharField(blank=True, max_length=20)),
                ('blood_group', models.CharField(blank=True, choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=4)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('home_address', models.CharField(blank=True, max_length=150)),
                ('work_address', models.CharField(blank=True, max_length=150)),
                ('qualifications', models.CharField(blank=True, max_length=100)),
                ('qualification_proof', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('own_records', models.ManyToManyField(db_constraint=False, related_name='d1', to='records.record')),
                ('patient_records', models.ManyToManyField(related_name='p1', to='records.record')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
