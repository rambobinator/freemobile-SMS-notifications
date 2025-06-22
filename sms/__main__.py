from argparse import ArgumentParser, FileType
from os import getenv

from sms import send, FreeMobileSMSNotificationException

parser = ArgumentParser(
    prog="freemobile",
    description="""
    Send SMS notifications to your own mobile via any internet-connected device.
    FREEMOBILE_USER_ID and/or FREEMOBILE_API_KEY can also be specified in environment variable to be used as default values.
    """,
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("message", help="Message to send", nargs="?")
group.add_argument(
    "--from-file",
    help="Send FROM_FILE content, use - for standard input",
    type=FileType("r"),
)
parser.add_argument(
    "--user-id",
    help="freemobile user id, go to https://mobile.free.fr/account/mes-options/notifications-sms",
    default=getenv("FREEMOBILE_USER_ID"),
    type=int,
)
parser.add_argument(
    "--api-key",
    help="freemobile api key, go to https://mobile.free.fr/account/mes-options/notifications-sms",
    default=getenv("FREEMOBILE_API_KEY"),
)
args = parser.parse_args()
try:
    send(
        args.user_id,
        args.api_key,
        args.message if args.message is not None else args.from_file.read(),
    )
except FreeMobileSMSNotificationException as e:
    print(e)
