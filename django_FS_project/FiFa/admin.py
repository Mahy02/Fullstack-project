from django.contrib import admin
from .models import Matches
from .models import Stadiums
from .models import Teams
from .models import Tickets
from .models import Referees

# Register your models here.
admin.site.register(Matches)
admin.site.register(Tickets)
admin.site.register(Teams)
admin.site.register(Referees)
admin.site.register(Stadiums)