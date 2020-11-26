# Generated by Django 3.1.3 on 2020-11-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemacolumn',
            name='column_type',
            field=models.CharField(choices=[('full_name', 'Full name'), ('job', 'Job'), ('email', 'Email'), ('phone_number', 'Phone number'), ('address', 'Address'), ('date', 'Date'), ('text', 'Text')], default='full_name', max_length=12),
        ),
    ]