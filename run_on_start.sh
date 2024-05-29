#!/bin/bash

# Cambiar al directorio del proyecto
cd /home/sistemas/RNAE/

# Activar el entorno virtual
source entorno/bin/activate
python3 manage.py collectstatic -yes
# Ejecutar el servidor Gunicorn
gunicorn -c /home/sistemas/RNAE/conf/gunicorn_config.py rnae.wsgi

