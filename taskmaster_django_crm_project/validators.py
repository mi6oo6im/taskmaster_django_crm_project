from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# template custom validator:
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _(f"{value} is not an even number"),
        )


def validate_first_capital(value):
    try:
        if value[0] != value[0].upper():
            raise ValidationError(
                _("First letter should be with capital case"),
            )
    except IndexError:
        raise ValidationError(
            _("Only letters are allowed."),
        )


def validate_all_alpha(value):
    if not value.isalpha():
        raise ValidationError(
            _("Only letters are allowed."),
        )

