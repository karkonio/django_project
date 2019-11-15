from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email():
    subject, from_email, to = 'Email confirmation', settings.EMAIL_HOST_USER, 'karina_yesbukenova@mail.ru'

    html_content = render_to_string(
        'registration/confirmation.html',
        {
            'first_name': 'korka'
        }
    )
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()