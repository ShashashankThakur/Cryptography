Generate a self-signed server certificate and private key using OpenSSL:
```
openssl req -x509 -newkey rsa:4096 -keyout server-key.pem -out server-cert.pem -days 365 -nodes
```

Run the server:
```
python chat_server.py
```

Run one or more clients:
```
python chat_client.py
```