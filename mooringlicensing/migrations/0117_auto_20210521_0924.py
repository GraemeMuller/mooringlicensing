# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-21 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0116_auto_20210518_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='customer_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('with_assessor', 'Under Review'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_documents', 'Awaiting Documents'), ('awaiting_sticker', 'Awaiting Sticker'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('awaiting_payment', 'Awaiting Payment')], default='draft', max_length=40, verbose_name='Customer Status'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='processing_status',
            field=models.CharField(choices=[('temp', 'Temporary'), ('draft', 'Draft'), ('with_assessor', 'With Assessor'), ('with_assessor_requirements', 'With Assessor (Requirements)'), ('with_approver', 'With Approver'), ('renewal', 'Renewal'), ('licence_amendment', 'Licence Amendment'), ('awaiting_applicant_respone', 'Awaiting Applicant Response'), ('awaiting_assessor_response', 'Awaiting Assessor Response'), ('awaiting_sticker', 'Awaiting Sticker'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_documents', 'Awaiting Documents'), ('awaiting_responses', 'Awaiting Responses'), ('ready_for_conditions', 'Ready for Conditions'), ('ready_to_issue', 'Ready to Issue'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('partially_approved', 'Partially Approved'), ('partially_declined', 'Partially Declined'), ('awaiting_payment', 'Awaiting Payment')], default='draft', max_length=30, verbose_name='Processing Status'),
        ),
    ]
