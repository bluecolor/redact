export LD_LIBRARY_PATH=/home/ceyhun/projects/lab/redact/lib/instantclient_12_2

celery -A app.tasks.discovery worker -Q discoveries,notifications
