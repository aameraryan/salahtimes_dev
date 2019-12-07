from django.core.exceptions import ValidationError


def phone_validator(value):
    if len(value) != 13 or value[:3] != "+91" or not value[3:].is_digit():
        raise ValidationError("Phone number not valid. eg. +910000000000")
    return True
