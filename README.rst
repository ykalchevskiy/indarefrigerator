InDaRefrigerator
================


Heroku
------

heroku config:set FLASK_APP_CONFIG=indarefrigerator.config.ProductionConfig
heroku config:set FLASK_SECRET_KEY=secret


Development
-----------

Use virtualenv/activate or virtualenvwrapper/postactivate:

export FLASK_APP_CONFIG=indarefrigerator.config.DevelopmentConfig
export FLASK_SECRET_KEY=secret

TODO
----

flask-login + flask-bcrypt
flask-restless
flask-babel
flask-assets
flask-wtf
flask-script
flask-testing
backbone
