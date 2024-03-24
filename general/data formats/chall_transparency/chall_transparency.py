# we can just query https://crt.sh/?q=cryptohack.org

# but this is a little "scam" because we're using prior knowledge

# https://censys.io/certificates indexes the sha256 fingerprint of the subject key info field in the x509 certificate; aka the public key
# SHA256 fingerprint is simply the SHA256 hash of the DER representation of the public key, so a simple shell command through openssl should give us what we need
# > openssl pkey -outform der -pubin -in transparency.pem | sha256sum
# we can then take the output and query on censys site: https://censys.io/certificates?q=29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2

# no matter what method you use, youll see the link: thetransparencyflagishere.cryptohack.org

# flag: crypto{thx_redpwn_for_inspiration}