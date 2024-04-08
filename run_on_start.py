#!/usr/bin/python
cd /home/sistemas/RNAE/
source entorno/bin/activate
gunicorn -c /home/sistemas/RNAE/conf/gunicorn_config.py rnae.wsgi
