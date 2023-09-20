import os
from django.core.exceptions import ValidationError
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.MOV','.avi','.mp4','.webm','.mkv']  # Define your list of valid extensions

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Supported extensions are .MOV, .avi,.mkv, .webm, and .mp4.')
