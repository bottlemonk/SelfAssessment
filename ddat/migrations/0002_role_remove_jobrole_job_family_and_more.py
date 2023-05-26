# Generated by Django 4.2.1 on 2023-05-26 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('job_family', models.CharField(choices=[('Data', 'Data'), ('IT Operations', 'IT Operations'), ('Product and delivery', 'Product and delivery'), ('Quality assurance testing (QAT)', 'Quality assurance testing (QAT)'), ('Technical', 'Technical'), ('User-centred design', 'User-centred design')], max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobrole',
            name='job_family',
        ),
        migrations.RemoveField(
            model_name='person',
            name='job_role',
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=200, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Last name'),
        ),
        migrations.DeleteModel(
            name='JobFamily',
        ),
        migrations.DeleteModel(
            name='JobRole',
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ddat.role'),
        ),
    ]