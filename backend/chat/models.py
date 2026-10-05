import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(_("Müştəri Adı"), max_length=60, default="Qonaq")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Çat")
        verbose_name_plural = _("Çatlar")
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.customer_name} - {self.id}"

class Message(models.Model):
    SENDER_CHOICES = (
        ('customer', 'Customer'),
        ('operator', 'Operator'),
        ('bot', 'Bot'),
    )
    
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(_("Mesaj"))
    sender_type = models.CharField(max_length=20, choices=SENDER_CHOICES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Mesaj")
        verbose_name_plural = _("Mesajlar")
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['chat', 'is_read']),
        ]

    def __str__(self):
        return f"{self.get_sender_type_display()} - {self.text[:30]}"
