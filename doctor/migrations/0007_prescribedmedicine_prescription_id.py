# Generated by Django 5.0.1 on 2024-03-30 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_remove_bill_doctor_id_remove_bill_patient_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescribedmedicine',
            name='prescription_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription'),
        ),
    ]
