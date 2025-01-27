# Generated by Django 5.0.7 on 2024-07-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('voter_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=23)),
                ('last_name', models.CharField(max_length=23)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=23)),
                ('address', models.CharField(max_length=23)),
                ('city', models.CharField(max_length=23)),
                ('state', models.CharField(max_length=23)),
                ('pincode', models.IntegerField()),
                ('dob', models.DateField()),
                ('contact', models.BigIntegerField()),
            ],
        ),
    ]
