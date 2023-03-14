import os
import ast
from typing import List, Optional
import json
import errors

from fastapi import APIRouter, HTTPException, Header, Request
from fastapi.responses import JSONResponse

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage
from pydantic import BaseModel

from utils.logger import create_logger

from process.replyContact import contact_text
from process.replyEservice import eservice_text
from process.replyFaq import faq_text
from process.replyOpenAccount import openacc_text
from process.replyProduct import product_text

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)

errors_lgr = create_logger("errors")

class Line(BaseModel):
    destination: str
    events: List[Optional[None]]



@router.post("/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    print('?????????????????????????')
    print(body.decode("utf-8"))
    print('?????????????????????????')
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    # except InvalidSignatureError:
    #     raise HTTPException(status_code=400, detail="chatbot handle body error.")
    # return 'OK'
    except Exception as e:
        errors_lgr.exception(e)
        error_message = str(e)
        print("error:", error_message, flush=True)
        try:
            res = ast.literal_eval(error_message)
        except:
            res = errors.unknown_error

        status_code = res.pop("status_code") if "status_code" in res else 500
        return JSONResponse(res, status_code)


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(event)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    
    json_event = event.as_json_dict()
    # json_event = jsonbody["events"][0]
    reply_tok = json_event['replyToken']
    receive_text = json_event['message']['text'].lower()
    source = json_event['source']
    contact_text(reply_tok, receive_text, source)
    eservice_text(reply_tok, receive_text, source)
    faq_text(reply_tok, receive_text, source)
    openacc_text(reply_tok, receive_text, source)
    product_text(reply_tok, receive_text, source)


# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     # receive_text = event['message']['text']
    
#     print("!!!!!!!!!!!!!!!!!!!!!!")
#     # line_message = json.loads(event.message)
#     print("!!!!!!!!!!!!!!!!!!!!!!")
#     print(event)
#     print("!!!!!!!!!!!!!!!!!!!!!!")
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text)
#     )


# @handler.add(MessageEvent, message=StickerMessage)
# def sticker_text(event):
#     # Judge condition
#     line_bot_api.reply_message(
#         event.reply_token,
#         StickerSendMessage(package_id='6136', sticker_id='10551379')
#     )