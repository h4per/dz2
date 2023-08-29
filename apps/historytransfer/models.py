from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User, related_name='transfers_sent',
        on_delete=models.CASCADE,
        verbose_name='Отправитель'
    )
    to_user = models.ForeignKey(
        User, related_name='transfers_received', 
        on_delete=models.CASCADE,
        verbose_name='Получатель'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус операции'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    amount = models.DecimalField(
        default=0,
        max_digits=10, 
        decimal_places=2
    )

    def __str__(self):
        return self.from_user
    
    class Meta:
        verbose_name = "История перевода"
        verbose_name_plural = "История переводов"