from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from contents.models import Thread, Comment


@receiver(post_save, sender=Thread)
def thread_create_notification(sender, instance, created, **kwargs):

    if created:
        subject = "コメント投稿"
        message = "コメントが投稿されました。"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Comment)
def comment_create_notification(sender, instance, created, **kwargs):

    if created:
        subject = "コメント投稿"
        message = "コメントが投稿されました。"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, recipient_list)
