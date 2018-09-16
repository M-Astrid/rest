sudo nginx -s reload
sudo gunicorn -b 0.0.0.0:8100  rest.wsgi:application