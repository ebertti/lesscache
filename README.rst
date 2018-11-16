LessCache
=========

Serverless cache backend for Django and Flask

Working with: AWS Dynamodb


.. image:: https://badges.gitter.im/Join%20Chat.svg
  :alt: Join the chat at https://gitter.im/ebertti/lesscache
  :target: https://gitter.im/ebertti/lesscache?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://img.shields.io/badge/django-1.11%202.0%202.1-brightgreen.svg
  :target: http://pypi.python.org/pypi/lesscache

.. image:: https://img.shields.io/pypi/v/lesscache.svg?style=flat
  :target: http://pypi.python.org/pypi/lesscache

.. image:: https://img.shields.io/pypi/pyversions/lesscache.svg?maxAge=2592000
  :target: http://pypi.python.org/pypi/lesscache

.. image:: https://img.shields.io/pypi/format/lesscache.svg?maxAge=2592000
  :target: http://pypi.python.org/pypi/lesscache

.. image:: https://img.shields.io/pypi/status/lesscache.svg?maxAge=2592000
  :target: http://pypi.python.org/pypi/lesscache

.. image:: https://img.shields.io/travis/ebertti/lesscache/master.svg?maxAge=2592000
  :target: https://travis-ci.org/ebertti/lesscache
  
.. image:: https://img.shields.io/requires/github/ebertti/lesscache.svg?maxAge=2592000
  :target: https://requires.io/github/ebertti/lesscache/requirements/

.. image:: https://img.shields.io/coveralls/ebertti/lesscache/master.svg?maxAge=2592000
  :target: https://coveralls.io/r/ebertti/lesscache?branch=master
  
.. image:: https://img.shields.io/codeclimate/github/ebertti/lesscache.svg
  :target: https://codeclimate.com/github/ebertti/lesscache

.. image:: https://landscape.io/github/ebertti/lesscache/master/landscape.png?style=flat
  :target: https://landscape.io/github/ebertti/lesscache/master


Installation
------------

**pip**

``pip install lesscache``
    
**pipenv**

``pipenv install lesscache``

Setup on Django
---------------

On Django Settings

.. code-block:: python

    instaled_apps = [
        ...
        'lesscache.compact.django'
    ]

    CACHES = {
        'default': {
            'BACKEND': 'lesscache.compact.django.cache.DjangoCacheDynamodb',
            'TIMEOUT': 120  # default 120 seconds == 2minutes
            'KEY_PREFIX': 'less'  # default less
            'VERSION': 1  # default 1
            'KEY_FUNCTION': 'path.to.function' # f'{prefix}:{key}:{version}'

            'OPTIONS': {
                'aws_access_key_id': None       # need only if you dont have login
                'aws_secret_access_key': None   # on aws-cli with your key
                'aws_region_name': None         # or not in aws lambda

                'read_capacity_units': 1
                'write_capacity_units': 1
                'encode': 'path.to.encode'  # default: 'lesscache.encode.PickleEncode
            }
        }
    }


Run manage command to create cache table on Dynamodb before using

``python manage.py create_dynamodb_cache``

Setup on Flask
--------------

**WIP**
