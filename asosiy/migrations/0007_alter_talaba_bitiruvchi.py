# Generated by Django 4.1.5 on 2023-01-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0006_alter_talaba_bitiruvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talaba',
            name='bitiruvchi',
            field=models.BooleanField(choices=[(True, True), (False, False)], default=False),
        ),
    ]