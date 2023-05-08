# Generated by Django 3.0.4 on 2020-04-20 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listelement', '0002_element_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uptated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(max_length=200)),
                ('payer_id', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=6.1, max_digits=10)),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listelement.Element')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
