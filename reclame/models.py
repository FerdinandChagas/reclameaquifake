from contextlib import nullcontext
from mailbox import NotEmptyError
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.

class Usuario(AbstractBaseUser):
    login = models.CharField(max_length=40, unique=True, default=None)
    password = models.CharField(max_length=40, default=None)
    USERNAME_FIELD = 'login'
    PASSWORD_FIELD = 'password'

    
    """def __init__(self,nome,email,senha):
        self.nome=nome
        self.email=email
        self.senha=senha
        self.reclamacoes=[] #Lista de reclamações do usuário
    """
        
    def toString(self):
        pass
    

class Empresa(Usuario,models.Model):
    media_notas=models.FloatField(default=0.0)
    ranking = models.IntegerField(default=0)
    
    """
    def __init__(self):
        self.media_notas=0.0
        self.ranking=0
    """    
    def toString(self):
        pass
    

class Reclamacao(models.Model):
    empresa = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    """    
    def __init__(self, empresa, usuario):
        self.empresa=empresa
        self.usuario=usuario
        self.conteudo=[] # Lista de mensagens
       
    """ 
    def toString(self):
        pass
    
class Mensagem(models.Model):
    data = models.DateTimeField('data')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reclamacao = models.IntegerField()
    conteudo = models.CharField(max_length=400, default='')
    
    
    """
    def __init__(self, data, usuario_id, reclamacao_id, conteudo):
        self.data=data
        self.usuario=usuario_id
        self.reclamacao=reclamacao_id
        self.conteudo=conteudo
    """
        
    def toString(self):
        pass
        