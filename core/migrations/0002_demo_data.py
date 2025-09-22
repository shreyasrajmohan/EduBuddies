from django.db import migrations

def create_demo_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    LibraryNote = apps.get_model('core', 'LibraryNote')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    if not User.objects.filter(username='test').exists():
        User.objects.create_user('test', 'test@example.com', 'test')
    test_user = User.objects.get(username='test')
    if not LibraryNote.objects.filter(title='Sample Note').exists():
        LibraryNote.objects.create(user=test_user, title='Sample Note', url='https://example.com/note1')

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demo_data),
    ]
