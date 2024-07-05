# Generated by Django 5.0.6 on 2024-07-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnippet', '0010_remove_binaryprediction_attack_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(blank=True, default=0, null=True)),
                ('rate', models.FloatField(blank=True, default=0.0, null=True)),
                ('sttl', models.IntegerField(blank=True, default=0, null=True)),
                ('dload', models.FloatField(blank=True, default=0.0, null=True)),
                ('swin', models.IntegerField(blank=True, default=0, null=True)),
                ('stcpb', models.BigIntegerField(blank=True, default=0, null=True)),
                ('dtcpb', models.BigIntegerField(blank=True, default=0, null=True)),
                ('dwin', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_srv_src', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_state_ttl', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_src_dport_ltm', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_dst_sport_ltm', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_dst_src_ltm', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_srv_dst', models.IntegerField(blank=True, default=0, null=True)),
                ('dttl', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_dst_ltm', models.IntegerField(blank=True, default=0, null=True)),
                ('ct_src_ltm', models.IntegerField(blank=True, default=0, null=True)),
                ('prediction_gn_binary', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_gn_multiclass', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_gb_binary', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_gb_multiclass', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_lr_binary', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_lr_multiclass', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_lr_l1_binary', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_lr_l1_multiclass', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_lr_l2_binary', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_lr_l2_multiclass', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_gb_gscv_binary', models.FloatField(blank=True, default=0.0, null=True)),
                ('prediction_gb_gscv_multiclass', models.FloatField(blank=True, default=0.0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BinaryPrediction',
        ),
    ]