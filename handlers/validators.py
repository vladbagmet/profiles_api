import trafaret as t


# https://help.twitter.com/en/managing-your-account/twitter-username-rules
TWITTER_HANDLE = t.Dict({t.Key("handle"): t.Regexp("^[A-Za-z0-9_]{1,15}$")})
