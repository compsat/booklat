# Generated by Django 2.1.2 on 2018-11-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(blank=True, default='Anonymous', max_length=255, null=True)),
                ('series', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('narrated_by', models.CharField(blank=True, default='Anonymous', max_length=255, null=True)),
                ('length', models.CharField(blank=True, max_length=255, null=True)),
                ('release_date', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('embedded', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255, null=True)),
                ('account', models.CharField(max_length=255, null=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='Donate_Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=255, null=True)),
                ('account_details', models.CharField(max_length=255, null=True)),
                ('option_logo', models.ImageField(null=True, upload_to='')),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=255)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(default='Anonymous', max_length=255)),
                ('partner_link', models.URLField(max_length=255, null=True)),
                ('partner_logo', models.ImageField(null=True, upload_to='')),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(max_length=255, null=True)),
                ('account_link', models.URLField(max_length=255, null=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
        ),
    ]
