# Generated by Django 4.1 on 2022-08-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_last_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
