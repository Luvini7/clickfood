from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Campos adicionais
    cargo = models.CharField(max_length=100, null=True, blank=True)
    setor = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)

    # Resolve conflitos com related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Define um related_name único
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Define um related_name único
        blank=True
    )

    def __str__(self):
        return self.username