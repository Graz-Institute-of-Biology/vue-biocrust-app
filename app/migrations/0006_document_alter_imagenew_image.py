# Generated by Django 4.1 on 2023-07-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_predresults_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='uploads/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='imagenew',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
