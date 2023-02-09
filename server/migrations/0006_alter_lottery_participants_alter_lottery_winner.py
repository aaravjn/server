# Generated by Django 4.1.3 on 2023-02-09 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0005_alter_lottery_participants_alter_lottery_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lottery',
            name='winner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='won_lotteries', to=settings.AUTH_USER_MODEL),
        ),
    ]