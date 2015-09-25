stuffs
======

### Raspi :

* commandes à lancer au démarrage
```
/etc/rc.local

ex : (su - pi -c "cd /home/pi/www && gunicorn hello_world:app -b :5000")&
```
* Motion
lancé à partir de la crontab de sudo
* accès à la config de la box du raspi en tapant dans le navigateur : http://localhost:8080

` ssh -L8080:192.168.1.1:80 pi@lamule73.adultdns.net `
