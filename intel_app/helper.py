import secrets
import json
import requests
from datetime import datetime
from decouple import config
from django.core.exceptions import ImproperlyConfigured

from intel_app.models import TopUpRequest

ishare_map = {
    2: 50,
    4: 52,
    7: 2000,
    10: 3000,
    12: 4000,
    15: 5000,
    18: 6000,
    22: 7000,
    25: 8000,
    30: 10000,
    45: 15000,
    60: 20000,
    75: 25000,
    90: 30000,
    120: 40000,
    145: 50000,
    285: 100000,
    560: 200000
}


def ref_generator():
    now_time = datetime.now().strftime('%H%M%S')
    secret = secrets.token_hex(2)

    return f"{now_time}{secret}".upper()


def top_up_ref_generator():
    """
    Generate a reference in the form TOPUP-HHMMXX where XX is a hex byte.
    If the generated ref already exists in TopUpRequest.reference, increment
    the hex byte by 1 (mod 256) and retry, up to 256 attempts.
    """
    time_str = datetime.now().strftime("%H%M")  # e.g. "1437"
    # pick a random starting byte 0–255
    secret_int = int(secrets.token_hex(1), 16)  # e.g. 0x3A → 58
    for _ in range(256):
        hex_part = f"{secret_int:02X}"  # e.g. "3A"
        ref = f"TOPUP-{time_str}{hex_part}"  # e.g. "TOPUP-14373A"
        # check your model for an existing record
        if not TopUpRequest.objects.filter(reference=ref).exists():
            return ref
        # collision → bump and try again
        secret_int = (secret_int + 1) % 256

    # if all 256 byte-values for this minute are exhausted, fail hard
    raise ImproperlyConfigured(
        "Unable to generate a unique top-up reference for this minute"
    )


def send_bundle(user, receiver, bundle_amount, reference):
    url = "https://console.bestpaygh.com/api/flexi/v1/new_transaction/"

    headers = {
        "api-key": config("API_KEY"),
        "api-secret": config("API_SECRET"),
        'Content-Type': 'application/json'
    }

    print("====================================")
    print(user.phone)
    print(user.first_name)
    print(user.last_name)
    print(user.email)
    print(receiver)
    print(reference)
    print(bundle_amount)
    print("=====================================")

    payload = json.dumps({
        "first_name": user.first_name,
        "last_name": user.last_name,
        "account_number": f"0{user.phone}",
        "receiver": receiver,
        "account_email": user.email,
        "reference": reference,
        "bundle_amount": bundle_amount
    })
    print("herrrrreeeeeeeee")
    response = requests.request("POST", url, headers=headers, data=payload)
    print("git here")
    print(response.json)
    return response


def value_for_moni_send_bundle(user, receiver, bundle_amount, reference):
    url = "https://www.value4moni.com/api/v1/inititate_transaction"

    headers = {
        'Content-Type': 'application/json',
    }

    # Create the payload for the POST request
    payload = {
        "API_Key": config("MONI_API_KEY"),
        "Receiver": str(receiver),
        "Volume": str(bundle_amount),
        "Reference": reference,
        "Package_Type": "AirtelTigo"
    }

    # Convert the payload into JSON format
    json_payload = json.dumps(payload)

    # Make the POST request to the API
    response = requests.post(url, headers=headers, data=json_payload)

    print(response.json())
    return response


def controller_send_bundle(receiver, bundle_amount, reference):
    url = "https://www.geosams.com/controller/api/send_bundle/"

    payload = json.dumps({
        "phone_number": str(receiver),
        "amount": int(bundle_amount),
        "reference": str(reference),
        "network": "AT"
    })
    headers = {
        'Authorization': config("CONTROLLER_TOKEN"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response


def verify_paystack_transaction(reference):
    url = f"https://api.paystack.co/transaction/verify/{reference}"

    headers = {
        "Authorization": "Bearer sk_test_d8585b8c1c61a364640e9acbb3bc8046f5fb9acd"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.json())

    return response

