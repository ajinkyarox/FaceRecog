# Generated by Django 3.0 on 2019-12-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
            ],
        ),
    ]
