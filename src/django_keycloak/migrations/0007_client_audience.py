# Generated by Django 2.1.5 on 2019-03-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_keycloak', '0006_remove_client_service_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='audience',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
