# Generated by Django 5.1.1 on 2024-10-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0002_rendezvous_date_rendezvous_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendezvous',
            name='date',
        ),
        migrations.RemoveField(
            model_name='rendezvous',
            name='email_client',
        ),
        migrations.RemoveField(
            model_name='rendezvous',
            name='nom_client',
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
            preserve_default=False,
        ),
    ]
