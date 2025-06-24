from unittest.mock import patch, MagicMock
from urllib import request, error

from pytest import raises

from sms import send, FreeMobileSMSNotificationException
from sms.sms import (
    FREEMOBILE_SMS_NOTIFICATION_DEFAULT_RETRIES,
    FREEMOBILE_SMS_NOTIFICATION_DEFAULT_CHUNKS,
)


def test_send():
    with patch.object(request, "urlopen", return_value=MagicMock(status=200)):
        send("USER_ID", "API_KEY", "Hello world")


def test_send_exceptions():
    for code in [400, 403, 500]:
        e = error.HTTPError(None, code, None, None, None)
        with (
            patch.object(request, "urlopen", side_effect=(e)),
            raises(FreeMobileSMSNotificationException),
        ):
            send("USER_ID", "API_KEY", "Hello world")


def test_send_retry():
    e = error.HTTPError(None, 402, None, None, None)
    with patch.object(request, "urlopen", side_effect=(e)) as mock_urlopen:
        send("USER_ID", "API_KEY", "Hello world")
        assert mock_urlopen.call_count == FREEMOBILE_SMS_NOTIFICATION_DEFAULT_RETRIES


def test_send_chunck():
    with patch.object(
        request, "urlopen", return_value=MagicMock(status=200)
    ) as mock_urlopen:
        send("USER_ID", "API_KEY", "Hello world")
        assert mock_urlopen.call_count == 1
    with patch.object(
        request, "urlopen", return_value=MagicMock(status=200)
    ) as mock_urlopen:
        send("USER_ID", "API_KEY", "*" * FREEMOBILE_SMS_NOTIFICATION_DEFAULT_CHUNKS * 2)
        assert mock_urlopen.call_count == 2
