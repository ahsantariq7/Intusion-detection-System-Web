# Generated by Django 5.0.2 on 2024-05-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnippet', '0008_remove_binaryprediction_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='binaryprediction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='attack_cat',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='ct_dst_sport_ltm',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='ct_dst_src_ltm',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='ct_src_dport_ltm',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='ct_srv_dst',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='ct_srv_src',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='ct_state_ttl',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='dload',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='dtcpb',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='dwin',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='prediction_gb',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='prediction_gb_gscv',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='prediction_gn',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='prediction_lr',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='prediction_lr_l1',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='prediction_lr_l2',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='rate',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='state',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='stcpb',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='sttl',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='binaryprediction',
            name='swin',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
