# Generated by Django 4.2.7 on 2023-11-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_rest_api', '0002_address_private_address_tree_citation_private_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='line3',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Line 3'),
        ),
        migrations.AddField(
            model_name='address',
            name='line4',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Line 4'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
