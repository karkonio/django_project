from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings


def send_email(profile, activation_token):
    subject = 'Email confirmation'
    from_email = settings.EMAIL_HOST_USER
    to = profile.email

    html_content = render_to_string(
        'registration/confirmation.html',
        {
            'profile': profile,
            'token': activation_token
        }
    )
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
