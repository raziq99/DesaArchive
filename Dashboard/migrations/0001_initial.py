# Generated by Django 5.1 on 2024-08-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('keterangan', 'Surat Keterangan'), ('masuk', 'Surat Masuk'), ('keluar', 'Surat Keluar'), ('asset', 'Asset')], max_length=20)),
                ('file', models.FileField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
