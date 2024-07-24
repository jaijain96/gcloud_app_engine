wait_for_mysql() {
  until python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('cloud_sql_proxy', 3307))" >/dev/null 2>&1
  do
    echo "Waiting for MySQL service to start..."
    sleep 5
  done
}

# wait_for_mysql # -> modify this for deployment where cloud sql proxy isn't
# needed

python manage.py makemigrations datalake
python manage.py migrate datalake

gunicorn -c configs/gunicorn_config.py datalake_from_scratch.wsgi:application
