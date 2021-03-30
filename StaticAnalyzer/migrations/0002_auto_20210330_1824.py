# Generated by Django 3.1.7 on 2021-03-30 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0001_initial'),
        ('StaticAnalyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JavaSourceAnalyzer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANALYZER', models.CharField(default='', max_length=50)),
                ('SCAN_TYPE', models.CharField(default='', max_length=10)),
                ('FILE_NAME', models.CharField(default='', max_length=260)),
                ('MD5', models.CharField(default='', max_length=32)),
                ('ANALYSIS_RESULT', models.TextField(default=[])),
                ('TIMESTAMP', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='RecentScansDB',
        ),
        migrations.RenameField(
            model_name='staticanalyzerandroid',
            old_name='ANDROID_API',
            new_name='DYNAMIC_REPORT',
        ),
        migrations.RenameField(
            model_name='staticanalyzerandroid',
            old_name='ACTIVITIES',
            new_name='FLOW_REPORT',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='APKID',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='APP_TYPE',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='BINARY_ANALYSIS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='BROWSABLE_ACTIVITIES',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='CERTIFICATE_ANALYSIS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='CODE_ANALYSIS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='DOMAINS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='EMAILS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='EXPORTED_ACTIVITIES',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='EXPORTED_COUNT',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='FILES',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='FILE_ANALYSIS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='FIREBASE_URLS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='ICON_FOUND',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='ICON_HIDDEN',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='LIBRARIES',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='MAIN_ACTIVITY',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='MANIFEST_ANALYSIS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='MAX_SDK',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='MIN_SDK',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='NETWORK_SECURITY',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='NIAP_ANALYSIS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='PERMISSIONS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='PLAYSTORE_DETAILS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='PROVIDERS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='RECEIVERS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='SECRETS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='SERVICES',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='SHA1',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='SHA256',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='SIZE',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='STRINGS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='TARGET_SDK',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='TRACKERS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='URLS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='VERSION_CODE',
        ),
        migrations.AddField(
            model_name='staticanalyzerandroid',
            name='SCAN_TYPE',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='staticanalyzerandroid',
            name='STATIC_REPORT',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.PROTECT, to='Report.androidstaticreport'),
        ),
        migrations.AddField(
            model_name='staticanalyzerandroid',
            name='TIMESTAMP',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='staticanalyzerandroid',
            name='APP_NAME',
            field=models.CharField(default='', max_length=260),
        ),
        migrations.AlterField(
            model_name='staticanalyzerandroid',
            name='PACKAGE_NAME',
            field=models.CharField(default='', max_length=260),
        ),
        migrations.AlterField(
            model_name='staticanalyzerandroid',
            name='VERSION_NAME',
            field=models.CharField(default='', max_length=50),
        ),
    ]