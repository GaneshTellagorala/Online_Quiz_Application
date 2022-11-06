# Generated by Django 2.2.6 on 2019-11-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0009_final_quizresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.Course'),
        ),
        migrations.AddField(
            model_name='quizresult',
            name='date1',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='quizresult',
            name='marks',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='quizresult',
            name='result',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quizresult',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.Topic'),
        ),
        migrations.DeleteModel(
            name='Final',
        ),
    ]
