# Generated by Django 3.1.12 on 2025-01-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('category', models.CharField(choices=[('GC', 'Gaming Consoles'), ('GL', 'Gaming Laptops/PCs'), ('GMK', 'Gaming Mice'), ('GK', 'Gaming Keyboards'), ('GH', 'Gaming Headsets'), ('GM', 'Gaming Monitors'), ('GC', 'Gaming Chairs')], max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
