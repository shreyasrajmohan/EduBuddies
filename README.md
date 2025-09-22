EduBuddy - packaged Django project

Setup:
1. Create PostgreSQL database and user:
   - DB name: EduData
   - User: EduUser
   - Password: eduuser
   (Grant privileges to the user for the DB.)

2. Install requirements:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py migrate

   Note: migrations included create the demo users and sample note.

4. Run server:
   python manage.py runserver

Demo credentials:
  - user: test / test
  - superuser: admin / admin123

Admin: http://127.0.0.1:8000/admin/
