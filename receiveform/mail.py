from django.template.loader import get_template
from django.conf import settings
import os

def generate_mail_content(context,template="tokenEmail.html"):
    email_path = os.path.join(settings.STATICFILES_DIRS[0],template)
    email_template = get_template(email_path)
