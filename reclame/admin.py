from django.contrib import admin
from .models import Empresa, Mensagem, Reclamacao, Usuario

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Mensagem)
admin.site.register(Reclamacao)
admin.site.register(Usuario)

