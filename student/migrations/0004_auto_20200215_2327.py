# Generated by Django 3.0.2 on 2020-02-15 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentdetailsinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetailsinfo',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sts', to='student.StudentInfo'),
        ),
    ]
