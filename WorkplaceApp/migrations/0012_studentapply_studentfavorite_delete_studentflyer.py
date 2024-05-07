# Generated by Django 4.1.5 on 2023-01-26 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0011_alter_flyerdata_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.flyerdata')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.studentdatatable')),
            ],
        ),
        migrations.CreateModel(
            name='studentfavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.flyerdata')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.studentdatatable')),
            ],
        ),
        migrations.DeleteModel(
            name='studentflyer',
        ),
    ]
