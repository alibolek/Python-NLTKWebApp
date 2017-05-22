#
# Runs web2py as a docker container over Debian, with Apache and mod_wsgi
#

FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    apache2 libapache2-mod-wsgi libapache2-mod-python \
	python-pip \
    ssl-cert \
    wget unzip
RUN pip install -U nltk
RUN wget http://www.web2py.com/examples/static/web2py_src.zip
RUN unzip -q web2py_src.zip

RUN cp -r web2py /var/www/web2py

# Configuring web2py run by mod_wsgi
RUN cp /var/www/web2py/handlers/wsgihandler.py /var/www/web2py

COPY web2py.conf /etc/apache2/sites-available/web2py.conf
RUN ln -s ../sites-available/web2py.conf /etc/apache2/sites-enabled/

RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod ssl
RUN a2dismod python

# Lower mpm-prefork minimum servers
RUN sed -i "s/StartServers          5/StartServers          1/g" /etc/apache2/apache2.conf
RUN sed -i "s/MinSpareServers       5/MinSpareServers       1/g" /etc/apache2/apache2.conf
RUN sed -i "s/MaxSpareServers      10/MaxSpareServers       1/g" /etc/apache2/apache2.conf

RUN chown -R www-data /var/www/web2py

WORKDIR /var/www/web2py

# Set web2py admin password
RUN sudo -u www-data python -c "from gluon.main import save_password; save_password('123',8443)"


CMD [ "python", "./my_script.py" ]


EXPOSE 80
EXPOSE 443

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
