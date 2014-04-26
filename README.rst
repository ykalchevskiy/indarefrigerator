InDaRefrigerator
================


Heroku
------

.. code-block:: bash

    $ heroku config:set FLASK_APP_CONFIG=indarefrigerator.config.ProductionConfig
    $ heroku config:set FLASK_SECRET_KEY=secret


Development
-----------

Use virtualenv/activate or virtualenvwrapper/postactivate:

.. code-block:: bash

    $ export FLASK_APP_CONFIG=indarefrigerator.config.DevelopmentConfig
    $ export FLASK_SECRET_KEY=secret


TODO
----

* flask-login, flask-bcrypt, flask-principal
* flask-restless
* flask-wtf
* flask-babel
* flask-assets

* backbone
