# Generated by Django 5.1.1 on 2024-10-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100)),
                ('date_rdv', models.DateTimeField()),
                ('email_client', models.EmailField(max_length=254)),
            ],
        ),
    ]
