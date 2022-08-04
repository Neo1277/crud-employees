from .models import ThirdParties

def check_email(last_name, first_name, country_code, pk=None):

    query_emails = ThirdParties.objects.validate_if_email_exist(
        last_name=last_name,
        first_name=first_name
    )

    if pk:
        get_email = query_emails.filter(pk=pk).first()
        if get_email:
            return get_email['email']

    last_email = query_emails.last()
    generate_new_email = GenerateNewEmail()
    generate_new_email.set_lastname(last_name)
    generate_new_email.set_firstname(first_name)
    generate_new_email.set_country_code(country_code)

    return generate_new_email.generate_sequential_email(last_email)


class GenerateNewEmail(object):

    def __init__(self, domain = "cidenet.com"):
        self._domain = domain
        self._lastname = ""
        self._firstname = ""
        self._country_code = ""

    # getter method
    def get_domain(self):
        return self._lastname

    # setter method
    def set_domain(self, domain):
        self._domain = domain

    # getter method
    def get_lastname(self):
        return self._lastname

    # setter method
    def set_lastname(self, lastname):
        self._lastname = lastname

    # getter method
    def get_firstname(self):
        return self._firstname

    # setter method
    def set_firstname(self, firstname):
        self._firstname = firstname

    # getter method
    def get_country_code(self):
        return self._country_code

    # setter method
    def set_country_code(self, country_code):
        self._country_code = country_code

    def generate_sequential_email(self, email):

        self._country_code.lower()

        new_email = self._firstname.lower() + '.' + self._lastname.lower()

        if email:
            new_email += self.generate_email_id(email['email'])

        new_email += '@' + self._domain + '.' + self._country_code.lower()

        return new_email

    def generate_email_id(self, email):
        extract_email = email.split('@')
        extract_id= extract_email[0].split('.')

        if len(extract_id) > 2:
            new_id = '.' + str( int(extract_id[2]) + 1 )
        else:
            new_id = '.1'

        return new_id
