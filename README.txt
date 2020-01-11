

PYTHON ENVIRONMENT

  Python 3 is required.
  (may need to replace 'pip' below with 'pip3')

  pip install -r requirements.txt

DATABASE
Choose one

  POSTGRES
  pip install psycopg2
  createdb animal-project

  MYSQL
  pip install pymysql

APP SET UP

  python animals/manage.py migrate
  python animals/manage.py createsuperuser
  python animals/manage.py create_shapes

RUN LOCALLY FOR DEVELOPMENT
  python animals/manage.py runserver


UPDATE ON LIVE SITE
  source env/bin/activate
  git pull
  python animals/manage.py create_shapes
  python animals/manage.py migrate
  python animals/manage.py collectstatic
  touch tmp/restart.txt
