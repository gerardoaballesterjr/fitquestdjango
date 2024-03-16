from django.core.exceptions import ValidationError
import uuid, math, os

def user_profile_validator(image):
    if image.width != 100 and image.height != 100:
        raise ValidationError('Profile must be exactly 100x100 pixels is required.')

def image_upload(instance, filename):
    return f'fitquest/{uuid.uuid4().hex}{os.path.splitext(filename)[-1]}'

def uuid_generator() -> str:
    return uuid.uuid4().hex

def slug_generator(instance, slug=None) -> str:
    slug = slug if slug is not None else uuid_generator()
    if instance.__class__.objects.filter(slug=slug).exists():
        return slug_generator(instance, uuid_generator())
    return slug

def distance(locations):
    return sum(calculate(locations[i], locations[i + 1]) for i in range(len(locations) - 1))

def calculate(loc0, loc1) -> float:
    radians = list(map(math.radians, [loc0.latitude, loc0.longitude, loc1.latitude, loc1.longitude]))
    result = math.sin((radians[2] - radians[0]) / 2) ** 2 + math.cos(radians[0]) * math.cos(radians[2]) * math.sin((radians[3] - radians[1]) / 2) ** 2
    return 6371 * (2 * math.atan2(math.sqrt(result), math.sqrt(1 - result)))