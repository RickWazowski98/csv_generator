# Generated by Django 3.1.3 on 2020-11-26 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_auto_20201125_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='date_of_creation',
            new_name='date_of_modified',
        ),
        migrations.AlterField(
            model_name='schema',
            name='column_separator',
            field=models.CharField(choices=[(',', 'Comma(,)'), (';', 'Semicolon(;)')], default=',', max_length=2),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string_character',
            field=models.CharField(choices=[('"', 'Double-quote(")'), ("'", "Single-quote(')")], default='"', max_length=2),
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_of_creation', models.DateField(auto_now_add=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schema', to='generator.schema')),
                ('schema_columns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='generator.schemacolumn')),
            ],
        ),
    ]
