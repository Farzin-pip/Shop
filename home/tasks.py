from bucket import bucket
from celery import shared_task
from utils import send_otp_code


# TODO: can be async?
def all_bucket_objects_task():
    result = bucket.get_objects()
    return result


@shared_task
def delete_object_task(key):
    bucket.delete_object(Key=key)


@shared_task
def download_object_task(key):
    bucket.download_object(key=key)


@shared_task
def upload_object_task(path, key):
    bucket.upload_object(path, key)


@shared_task
def send_otp_task(phone_number ,code):
    send_otp_code(phone_number ,code)
