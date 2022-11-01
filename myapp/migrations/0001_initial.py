# Generated by Django 4.1.2 on 2022-10-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=150)),
                ('employment_type', models.CharField(choices=[('FULL_TIME', 'Full-time'), ('PART_TIME', 'Part-time'), ('REMOTE', 'Remote'), ('CONTRACT', 'Contract')], max_length=150)),
                ('experience_level', models.CharField(choices=[('ENTRY_LEVEL', 'Entry_level'), ('MID_LEVEL', 'Mid-level'), ('SENIOR_LEVEL', 'Senior-level')], max_length=150)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('status', models.CharField(choices=[('UNPUBLISHED', 'Unpublished'), ('PUBLISHED', 'Published')], default='PUBLISHED', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
