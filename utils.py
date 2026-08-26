from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('446A475376747867777A336B4D387363432F2F4B796E526A672B5A3570796876447A654142467A4B374B453D')
        params = {
            'sender': '2000660110',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
