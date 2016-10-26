from django.contrib import admin
from baseball_api_app.models import Master, Batting, Fielding, Pitching

admin.site.register([Master, Batting, Fielding, Pitching])
