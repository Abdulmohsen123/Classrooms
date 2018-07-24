# Generated by Django 2.0.6 on 2018-07-24 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_classroom_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('exame_grade', models.CharField(max_length=120)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom')),
            ],
        ),
    ]
