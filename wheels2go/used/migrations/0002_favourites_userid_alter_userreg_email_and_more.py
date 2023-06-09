# Generated by Django 4.2 on 2023-05-04 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('used', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourites',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='used.userreg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userreg',
            name='email',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='phonenumber',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='username',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
