# Generated by Django 4.2 on 2023-05-08 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('used', '0006_remove_vehicle_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vbrand', models.CharField(max_length=50)),
                ('vmodel', models.CharField(max_length=50)),
                ('vyear', models.PositiveIntegerField()),
                ('vmileage', models.PositiveIntegerField()),
                ('vprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vimage', models.ImageField(blank=True, default=None, upload_to='vehicle/uploads')),
                ('vimage1', models.ImageField(blank=True, default=None, upload_to='vehicle/uploads')),
                ('vimage2', models.ImageField(blank=True, default=None, upload_to='vehicle/uploads')),
                ('vimage3', models.ImageField(blank=True, default=None, upload_to='vehicle/uploads')),
                ('vuserid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='used.userreg')),
            ],
        ),
    ]
