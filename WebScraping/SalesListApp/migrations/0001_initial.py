# Generated by Django 4.1.2 on 2022-10-18 14:23

from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HepsiBurada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=500)),
                ('marka', models.CharField(max_length=500)),
                ('model_adi', models.CharField(max_length=500)),
                ('prices', models.IntegerField()),
                ('puani', models.CharField(max_length=500)),
                ('ekran_boyutu', models.CharField(max_length=500)),
                ('islemci', models.CharField(max_length=500)),
                ('islemci_tipi', models.CharField(max_length=500)),
                ('isletim_sistemi', models.CharField(max_length=500)),
                ('ssd_kapasitesi', models.CharField(max_length=500)),
                ('ram', models.CharField(max_length=500)),
            ],
        ),
    ]