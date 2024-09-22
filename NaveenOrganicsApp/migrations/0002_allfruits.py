# Generated by Django 5.0 on 2024-01-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NaveenOrganicsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllFruits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'all_fruits2',
                'unique_together': {('id', 'name')},
            },
        ),
    ]
