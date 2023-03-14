import os
import json
import copy

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, StickerSendMessage, \
                           TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, \
                            ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage

from utils.loaders import load_json                           

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

config = load_json('configs.json')

mes_temp = {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
                "type": "message",
                "label": "",
                "text": "",
                      }
           }

uri_temp = {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
                "type": "uri",
                "label": "",
                "uri": "",
                      }
           }

def faq_text(reply_tok, receive_text, source):
    if receive_text == 'faq':
        footer_contents = []
        for mes_type in config['faq'].values():
            
            if mes_type['type'] == 'text':
                faq_i = copy.deepcopy(mes_temp)
                # faq_i = mes_temp.copy()
                faq_i['action']['label'] = mes_type['question']
                faq_i['action']['text'] = mes_type['question']

            elif mes_type['type'] == 'link':
                faq_i = copy.deepcopy(uri_temp)
                # faq_i = uri_temp.copy()
                faq_i['action']['label'] = mes_type['question']
                faq_i['action']['uri'] = mes_type['answer']

            footer_contents.append(faq_i)

        flex_message = FlexSendMessage(
            alt_text='FAQ',
            contents={
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": config['buttonsImageURL'],
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
                          },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "FAQ",
                                    "weight": "bold",
                                    "size": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "กรุณาเลือกรายการ",
                                                    "wrap": True,
                                                    "color": "#666666",
                                                    "size": "sm",
                                                    "flex": 5
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": footer_contents,
                            "flex": 0
                        }
                    }
        )
        line_bot_api.reply_message(reply_tok, flex_message)
    
    else:
        for repl in config['faq'].values():
            if receive_text == repl['question'].lower():
                mes = repl['answer']
                line_bot_api.reply_message(reply_tok, TextSendMessage(mes))
                break

    return True