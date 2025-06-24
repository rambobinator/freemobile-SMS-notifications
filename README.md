# freemobile SMS notifications

Send SMS notifications to your own free mobile via any internet-connected device.

Go to there website for more informations: https://mobile.free.fr/account/mes-options/notifications-sms

You can directly activate the option here: https://mobile.free.fr/account/mes-options?update=notifications-sms&activate=1

Copy your user_id and api_key in your environnement like so:


`export FREEMOBILE_USER_ID=******* FREEMOBILE_API_KEY=********`

## uv

If you already are an [uv](https://docs.astral.sh/uv/guides/install-python/) user and don't want to install this package, simply type the following in your terminal:

`uvx --from git+https://github.com/rambobinator/freemobile-SMS-notifications freemobile "hello me \!"`

You should receive an ... sms there it is :)
