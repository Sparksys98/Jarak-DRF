# Generated by Django 3.0.5 on 2020-04-27 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JarakAPI', '0002_auto_20200427_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('ABD', 'Abdali'), ('ARJ', 'Arjan'), ('TAB', 'Tabarbour'), ('WSR', 'Wadi_el_seir'), ('ABA', 'Aein_Al_Basha')], default='ABD', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
