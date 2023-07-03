# Generated by Django 4.2.2 on 2023-07-02 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_attendee_rename_title_conference_tittle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Participants', to='events.event')),
                ('sessions', models.ManyToManyField(to='events.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=100)),
                ('payment_date', models.DateField()),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('PAID', 'Paid'), ('PENDING', 'Pending'), ('FAILED', 'Failed')], max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.participant')),
            ],
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='attendee',
        ),
        migrations.DeleteModel(
            name='Attendee',
        ),
        migrations.AddField(
            model_name='reminder',
            name='Participant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='events.participant'),
            preserve_default=False,
        ),
    ]