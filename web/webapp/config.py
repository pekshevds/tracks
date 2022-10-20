from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__name__))


WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "3ee7edd3364d4635a6055621220410"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'webapp.db')

SECRET_KEY = "ecovijelcmelxcvemwxweilhrwmiehlrxeiobrxce;povciwe"
REMEMBER_COOKIE_DURATION = timedelta(days=5)