import os
import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, StickerSendMessage, \
                           TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, \
                            ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage, ImageSendMessage

from utils.loaders import load_json                           

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

config = load_json('configs.json')

def openacc_text(reply_tok, receive_text, source):
    if receive_text == 'เปิดบัญชี':
        buttons_template_message = TemplateSendMessage(
            alt_text='เปิดบัญชี',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='เปิดบัญชี',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(label='วิธีการเปิดบัญชี', text='วิธีการเปิดบัญชี'),
                    MessageAction(label='คุณสมบัติผู้เปิดบัญชี', text='คุณสมบัติผู้เปิดบัญชี'),
                    MessageAction(label='ค่าใช้จ่ายในการเปิดบัญชี', text='ค่าใช้จ่ายในการเปิดบัญชี'),
                    MessageAction(label='FAQ', text='FAQ'),
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'ค่าใช้จ่ายในการเปิดบัญชี':
        mes = config['open_account']['open_fee']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'คุณสมบัติผู้เปิดบัญชี':
        mes = config['open_account']['qualification']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'วิธีการเปิดบัญชี':
        buttons_template_message = TemplateSendMessage(
            alt_text='วิธีการเปิดบัญชี',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='วิธีการเปิดบัญชี',
                text='กรุณาเลือกรายการ',
                actions=[
                    URIAction(label='ขั้นตอนการเปิดบัญชี', uri=config['open_account']['open_step']),
                    MessageAction(label='การยืนยันตัวตนเปิดบัญชี', text='การยืนยันตัวตนเปิดบัญชี'),
                    MessageAction(label='การสมัคร ATS', text='การสมัคร ATS'),

                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    # elif receive_text == 'การยืนยันตัวตนเปิดบัญชี':
    #     flex_message = FlexSendMessage(
    #         alt_text='การยืนยันตัวตนเปิดบัญชี',
    #         contents={
    #                     "type": "bubble",
    #                     "hero": {
    #                         "type": "image",
    #                         "url": config['buttonsImageURL'],
    #                         "size": "full",
    #                         "aspectRatio": "20:13",
    #                         "aspectMode": "cover"
    #                       },
    #                     "body": {
    #                         "type": "box",
    #                         "layout": "vertical",
    #                         "contents": [
    #                             {
    #                                 "type": "text",
    #                                 "text": "การยืนยันตัวตนเปิดบัญชี",
    #                                 "weight": "bold",
    #                                 "size": "xl"
    #                             },
    #                             {
    #                                 "type": "box",
    #                                 "layout": "vertical",
    #                                 "margin": "lg",
    #                                 "spacing": "sm",
    #                                 "contents": [
    #                                     {
    #                                         "type": "box",
    #                                         "layout": "baseline",
    #                                         "spacing": "sm",
    #                                         "contents": [
    #                                             {
    #                                                 "type": "text",
    #                                                 "text": config['open_account']['ndid']['ndid_detail'],
    #                                                 "wrap": True,
    #                                                 "color": "#666666",
    #                                                 "size": "sm",
    #                                                 "flex": 5
    #                                             }
    #                                         ]
    #                                     }
    #                                 ]
    #                             }
    #                         ]
    #                     },
    #                     "footer": {
    #                         "type": "box",
    #                         "layout": "vertical",
    #                         "spacing": "sm",
    #                         "contents": [
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "NDID คืออะไร",
    #                                     "uri": config['open_account']['ndid']['what_is_ndid']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "BAY",
    #                                     "uri": config['open_account']['ndid']['bay']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "BBL",
    #                                     "uri": config['open_account']['ndid']['bbl']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "CIMB",
    #                                     "uri": config['open_account']['ndid']['cimb']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "GSB",
    #                                     "uri": config['open_account']['ndid']['gsb']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "KBANK",
    #                                     "uri": config['open_account']['ndid']['kbank']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "KKP",
    #                                     "uri": config['open_account']['ndid']['kkp']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "SCB",
    #                                     "uri": config['open_account']['ndid']['scb']
    #                                 }
    #                             },
    #                             {
    #                                 "type": "button",
    #                                 "style": "link",
    #                                 "height": "sm",
    #                                 "action": {
    #                                     "type": "uri",
    #                                     "label": "TTB",
    #                                     "uri": config['open_account']['ndid']['ttb']
    #                                 }
    #                             }
    #                         ],
    #                         "flex": 0
    #                     }
    #                 }
    #     )
    #     line_bot_api.reply_message(reply_tok, flex_message)

    elif receive_text == 'การยืนยันตัวตนเปิดบัญชี':
        flex_message = FlexSendMessage(
            alt_text='การยืนยันตัวตนเปิดบัญชี',
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
                                    "text": "การยืนยันตัวตนเปิดบัญชี",
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
                                                    "text": config['open_account']['open_verification']['verification_detail'],
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
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "การยืนยันตัวตนผ่านธนาคาร",
                                        "uri": config['open_account']['open_verification']['bank_ver']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "การยืนยันตัวตนผ่าน 7-11",
                                        "text": "การยืนยันตัวตนผ่าน 7-11"
                                    }
                                }
                            ],
                            "flex": 0
                        }
                    }
        )
        line_bot_api.reply_message(reply_tok, flex_message)

    elif receive_text == 'การยืนยันตัวตนผ่าน 7-11':
        image_message = ImageSendMessage(
        original_content_url=config['open_account']['open_verification']['7_11_ver'],
        preview_image_url=config['open_account']['open_verification']['7_11_ver']
        )
        line_bot_api.reply_message(reply_tok, image_message)
    
    elif receive_text == 'การสมัคร ats':
        flex_message = FlexSendMessage(
            alt_text='การสมัคร ATS',
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
                                    "text": "การสมัคร ATS",
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
                                                    "text": config['open_account']['ats']['ats_detail'],
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
                            "contents": [

                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "BAY",
                                        "uri": config['open_account']['ats']['bay']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "BBL",
                                        "uri": config['open_account']['ats']['bbl']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "KTB",
                                        "uri": config['open_account']['ats']['ktb']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "SCB",
                                        "uri": config['open_account']['ats']['scb']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "TTB",
                                        "uri": config['open_account']['ats']['ttb']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "UOB",
                                        "uri": config['open_account']['ats']['uob']
                                    }
                                },
                            ],
                            "flex": 0
                        }
                    }
        )
        line_bot_api.reply_message(reply_tok, flex_message)
    
    return True