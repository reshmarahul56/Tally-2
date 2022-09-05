from django.contrib import admin

from tally2_app.models import Costcentr, Ledger, MainGroup, SubGroup, Under

# Register your models here.

admin.site.register(Under)
admin.site.register(MainGroup)
admin.site.register(SubGroup)
admin.site.register(Ledger)
admin.site.register(Costcentr)
