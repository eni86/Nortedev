from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.views.decorators import staff_member_required


class PerfilDeUsuario(models.Model):
    idusuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Field name made lowercase.
    nombres = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    clave = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    web = models.URLField(blank=True)
    class Meta:
        managed = True
        db_table = 'Usuario'
    def __str__(self):
        return self.idusuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilDeUsuario.objects.create(usuario=instance)

@staff_member_required
@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfildeusuario.save()
