from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    """
    Validate whether the password is alphanumeric.
    """

    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError("This password must contain a letter.",
                                  code='password_no_letter')

    def get_help_text(self):
        return 'Your password must contain at least one upper or lower case letter.'
