# LINE-Fresh
A chatbot for LINE Tech Fresh 2019 pre-test

Chatbot ID: [@175novon](https://line.me/R/ti/p/@175novon)

![Chatbot QRCode](https://imgur.com/DlSoX2c.png)

## Deploy

1. Install dependencies.

   ```bash
   pip3 install -r requirements.txt
   ```

2. Store chatbot access token and secret to environment variables.

   ```bash
   export LINE_CHANNEL_ACCESS_TOKEN=<LINE_CHANNEL_ACCESS_TOKEN>
   export LINE_CHANNEL_SECRET=<LINE_CHANNEL_SECRET>
   ```

3. (optional) Set port of the web service.

   ```bash
   export PORT=<PORT>
   ```

4. Run it.

   ```bash
   gunicorn bot:app
   ```

> If you don't have a domain name, you can get a temporary one by using `ngrok`. Just run:
>
> ```bash
> ngrok http <PORT>
> ```
