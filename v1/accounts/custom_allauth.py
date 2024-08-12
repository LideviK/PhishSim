from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class AccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        params = request.GET
        base_url = params.get('base_url', settings.FRONTEND_BASE_URL)
        # base_url = params.get('base_url', settings.INTERNAL_DOMAIN)
        if base_url.endswith('/'):
            fmt_str = '{}verify_email/{}'
        else:
            fmt_str = '{}/verify_email/{}'

        return fmt_str.format(base_url, emailconfirmation.key)

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        print("--> supering ...");
        return super(AccountAdapter, self).send_confirmation_mail(request, emailconfirmation, signup)

    def get_email_confirmation_redirect_url(self, request):
        path = 'rest-auth/registration/complete/'
        print("--> returning the anon redirect url...");
        return settings.EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL

    def respond_email_verification_sent(self, request, user):
        """
        We don't need this redirect.
        """
        pass