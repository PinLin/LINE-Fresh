# LINE-Fresh
A chatbot for LINE Tech Fresh 2019 pre-test

Chatbot ID: [@175novon](https://line.me/R/ti/p/@175novon)

![Chatbot QRCode](https://imgur.com/DlSoX2c.png)

## Demo

| ![](https://imgur.com/7AeBO2J.png) | ![](https://imgur.com/xqJXawe.png) |
| ---------------------------------- | ---------------------------------- |
| ![](https://imgur.com/RrrA6E7.png) | ![](https://imgur.com/MBFJFj6.png) |



## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PinLin/LINE-Fresh) 

> Remember to add   `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_CHANNEL_SECRET` to **Config Vars** in settings.

Or you can deploy manually by following these steps.

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
