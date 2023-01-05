# Generated by Django 4.1.3 on 2023-01-04 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_students_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=30)),
                ('mob', models.IntegerField()),
                ('qualification', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('passoutyear', models.IntegerField()),
                ('sem', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Enquiry', 'Enquiry'), ('Joined', 'Joined'), ('Placed', 'Placed'), ('complete', 'Complete')], max_length=30)),
                ('address', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.student')),
                ('total_fee', models.IntegerField()),
                ('submitamount', models.CharField(max_length=100)),
                ('remaining', models.IntegerField()),
                ('submitdate', models.CharField(max_length=100)),
                ('nextpaydate', models.DateField()),
            ],
        ),
    ]
