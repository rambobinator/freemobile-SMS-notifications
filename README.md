# freemobile SMS notifications

Send SMS notifications to your own free mobile via any internet-connected device.

Visit their website for more informations:

https://mobile.free.fr/account/mes-options/notifications-sms

You can directly activate the option here: 

https://mobile.free.fr/account/mes-options?update=notifications-sms&activate=1

Copy your user_id and api_key in your environment like so:


`export FREEMOBILE_USER_ID=19666242 FREEMOBILE_API_KEY=G0n@bha2Get`

## uv:

If you already are an [uv](https://docs.astral.sh/uv/guides/install-python/) fan and don't want to install this package, simply type the following in your terminal:

`uvx freemobile "hello me :)"`

You should receive an ... sms there it is :)

## pip:

``` bash
pip install freemobile
freemobile "hello me again"
```

## Without environment variable:

`freemobile  --user-id 19666242 --api-key G0n@bha2Get "It's me again ..."`

## Send file content or standard input:

``` bash
echo "hello $USER \!" > msg.txt
freemobile --from-file msg.txt
```
or

`echo "hello $USER \!" | freemobile --from-file -`

## Limitations:

- ~~There seems to be a limit of 1000 characters per sending that I will fix in a future release (I never reach this limit in my personal usage ...).~~
- I haven't reached the rate limit quota yet, but I've implemented a retry mechanism that should work for most.
