# Generated by Django 4.0.3 on 2022-10-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_cart_status_alter_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='rr', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='rr', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(default=3434434),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]