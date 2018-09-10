#!/usr/bin/env bash
SECRET_KEY = os.environ.get

SQLALCHEMY_DATABASE_URI =postgresql+psycopg2://feisal:1234@localhost/pitch


export MAIL_USERNAME=addictivefazman@gmail.com
export MAIL_PASSWORD=fazmandinho


python3.6 manage.py server