Bachelor-Scorekeeper
====================

Install
-------

Suggested to setup virtualenv first

```
pip install -r requirements
```

Setup DB:
---------

* Ensure PG is running with `bachelor` database created

```
FLASK_APP=bachelor.py flask db upgrade
```
