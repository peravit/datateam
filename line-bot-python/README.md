# Line Chatbot using Python and Fast Api
This line bot using LineSDK [Line Python SDK](https://github.com/line/line-bot-sdk-python) to build the webhook api in Line API messaging

## Prerequisite

- Python 3.x
- Docker
- Line python SDK (python lib)

## deployment
cd to line-bot-python repository
```
cd datateam/line-bot-python/
```
1.	Pull existing code to EC2 Production
2.	Build and deploy using Docker 
```
docker-compose up -d --no-deps --build
```
3.	Verify API in Line Webhook of our Line Official Account
