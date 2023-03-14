# Line Chatbot using Python and Fast Api
This line bot using LineSDK [Line Python SDK](https://github.com/line/line-bot-sdk-python) to build the webhook api in Line API messaging

## Prerequisite

- Python 3.x
- Docker
- Line python SDK (python lib)

## Development

cd to line-bot-python repository
```
cd datateam/line-bot-python/
```

Before building you need to change to specific bot that you want to use, token can be found in [Line Messaging API](https://developers.line.biz/)

create .env file in `/pipeline` and copy token and key to `.env` file
```
cd datateam/line-bot-python/pipeline
```

- LINE_CHANNEL_ACCESS_TOKEN (see in Messaging API tab --> Channel access token)
- LINE_CHANNEL_SECRET (see in Basic settings tab --> Channel secret)
```
LINE_CHANNEL_ACCESS_TOKEN=[YOUR_LINE_CHANNEL_ACCESS_TOKEN]
LINE_CHANNEL_SECRET=[YOUR_LINE_CHANNEL_SECRET]
API_ENV=developer

** fill key without []
```

run in local machine

```
pip install -r requirements.txt
python main.py
```

#### Or

Build using Docker

```
docker build -t line-bot-pipe .

docker run -d -p 443:443 line-bot-pipe
```

## Test
Line requires https for verify webhook, using ngrok can help to test easily

```
ngrok config add-authtoken [YOUR AUTH TOKEN FOR NGROK]

ngrok http 443
```
## Edit replies message

`config.json` allow you to edit messages that the bot replies

## deployment

1.	Pull existing code to EC2 Production
2.	Build and deploy using Docker
3.	Verify API in Line Webhook of our Line Official Account


## LICENSE

MIT
