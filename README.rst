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

Quickstart
----------

.. code-block:: bash

    $ pip install -r requrements/testing.txt
    $ ./manage.py db create
    $ ./manage.py create_superuser user@example.com password
    $ ./manage.py runserver

TODO
----

* flask-security
* flask-restless
* flask-wtf
* wtforms-alchemy
* flask-babel
* flask-assets

* backbone

Other
-----

* nosetests tests --with-coverage --cover-package=indarefrigerator
* coverage run manage.py tests && coverage report -m
* coverage html && google-chrome htmlcov/index.html
