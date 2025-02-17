# Generated by Django 3.1.12 on 2025-02-13 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questloadout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GC', 'Gaming Consoles'), ('GL', 'Gaming Laptops/PCs'), ('GMK', 'Gaming Mouse'), ('GK', 'Gaming Keyboards'), ('GH', 'Gaming Headsets'), ('GM', 'Gaming Monitors'), ('GCH', 'Gaming Chairs')], max_length=4),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
