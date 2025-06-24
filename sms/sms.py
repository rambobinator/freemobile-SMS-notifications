#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"

from time import sleep
from urllib import error, parse, request

# API url and errors are from https://mobile.free.fr/account/mes-options/notifications-sms
FREEMOBILE_SMS_NOTIFICATION_URL = "https://smsapi.free-mobile.fr/sendmsg"
FREEMOBILE_SMS_NOTIFICATION_RESPONSES = {
    200: "Le SMS a été envoyé sur votre mobile.",
    400: "Un des paramètres obligatoires est manquant.",
    402: "Trop de SMS ont été envoyés en trop peu de temps.",
    403: "Le service n'est pas activé sur l'espace abonné, ou login / clé incorrect.",
    500: "Erreur côté serveur. Veuillez réessayer ultérieurement.",
}
FREEMOBILE_SMS_NOTIFICATION_DEFAULT_TIMEOUT = 10
FREEMOBILE_SMS_NOTIFICATION_DEFAULT_RETRIES = 3
FREEMOBILE_SMS_NOTIFICATION_DEFAULT_CHUNKS = 999


class FreeMobileSMSNotificationException(Exception):
    pass


def send(
    user_id: int,
    api_key: str,
    message: str,
    timeout: int = FREEMOBILE_SMS_NOTIFICATION_DEFAULT_TIMEOUT,
    retries: int = FREEMOBILE_SMS_NOTIFICATION_DEFAULT_RETRIES,
    chunks: int = FREEMOBILE_SMS_NOTIFICATION_DEFAULT_CHUNKS,
) -> None:
    i = 0
    while tmp := message[i : chunks + i]:
        query = parse.urlencode({"user": user_id, "pass": api_key, "msg": tmp})
        for retry in range(retries):
            try:
                with request.urlopen(
                    f"{FREEMOBILE_SMS_NOTIFICATION_URL}?{query}", timeout=timeout
                ):
                    break
            except error.HTTPError as e:
                match e.code:
                    case 400 | 403 | 500:
                        raise FreeMobileSMSNotificationException(
                            FREEMOBILE_SMS_NOTIFICATION_RESPONSES[e.code]
                        )
                    case 402:
                        sleep(retry**2)
                        continue
        i += chunks


__all__ = ["send", "FreeMobileSMSNotificationException"]
