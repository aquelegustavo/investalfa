# Generated by Django 4.1 on 2022-08-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_remove_company_id_alter_company_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='max_quote',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='min_quote',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='last_quote',
            field=models.DecimalField(
                blank=True, decimal_places=2, default=None, max_digits=6, null=True),
        ),
    ]
