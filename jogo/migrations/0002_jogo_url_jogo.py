from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='url_jogo',
            field=models.CharField(max_length=200, default=''),  # Corrigido para string vazia
            preserve_default=False,
        ),
    ]
