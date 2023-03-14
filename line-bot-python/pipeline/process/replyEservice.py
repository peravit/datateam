import os
import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, StickerSendMessage, \
                           TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, \
                            ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage

from utils.loaders import load_json                           

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

config = load_json('configs.json')

def eservice_text(reply_tok, receive_text, source):
    if receive_text == 'e-service':
        buttons_template_message = TemplateSendMessage(
            alt_text='E-service',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='E-service',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(label='การถอนเงิน', text='การถอนเงิน'),
                    MessageAction(label='การฝากเงิน', text='การฝากเงิน'),
                    MessageAction(label='การโอนหุ้น', text='การโอนหุ้น'),
                    MessageAction(label='การเปลี่ยนแปลงข้อมูล', text='การเปลี่ยนแปลงข้อมูล'),
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'การถอนเงิน':
        buttons_template_message = TemplateSendMessage(
            alt_text='การถอนเงิน',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='การถอนเงิน',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(label='ขั้นตอนการถอนเงิน', text='ขั้นตอนการถอนเงิน'),
                    MessageAction(label='เงื่อนไขการถอนเงิน', text='เงื่อนไขการถอนเงิน'),
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'ขั้นตอนการถอนเงิน':
        mes = config['e_service']['withdraw']['withdraw_step']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'เงื่อนไขการถอนเงิน':
        mes = config['e_service']['withdraw']['withdraw_condition']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))
    
    elif receive_text == 'การโอนหุ้น':
        flex_message = FlexSendMessage(
            alt_text='การโอนหุ้น',
            contents={
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": config['buttonsImageURL'],
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            # "action": {
                            #   "type": "uri",
                            #   "uri": "http://linecorp.com/"
                            # }
                          },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "การโอนหุ้น",
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
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "การถอนใบหุ้น",
                                        "text": "การถอนใบหุ้น"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "การโอนหุ้นไปบริษัทหลักทรัพย์อื่น",
                                        "text": "การโอนหุ้นไปบริษัทหลักทรัพย์อื่น"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "โอนหุ้นระหว่างบัญชี",
                                        "text": "โอนหุ้นระหว่างบัญชี"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "ค่าใช้จ่ายการโอนหุ้น",
                                        "text": "ค่าใช้จ่ายการโอนหุ้น"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "เงื่อนไขการโอนหุ้น",
                                        "text": "เงื่อนไขการโอนหุ้น"
                                    }
                                }
                            ],
                            "flex": 0
                        }
                    }
        )
        line_bot_api.reply_message(reply_tok, flex_message)

    elif receive_text == 'การถอนใบหุ้น':
        mes = config['e_service']['transfer']['withdraw_stock_certificate']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'การโอนหุ้นไปบริษัทหลักทรัพย์อื่น':
        mes = config['e_service']['transfer']['transfer_to_broker']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'เงื่อนไขการโอนหุ้น':
        mes = config['e_service']['transfer']['transfer_condition']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'โอนหุ้นระหว่างบัญชี':
        mes = config['e_service']['transfer']['transfer_between_account']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'ค่าใช้จ่ายการโอนหุ้น':
        mes = config['e_service']['transfer']['transfer_fee']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))
    
    elif receive_text == 'การเปลี่ยนแปลงข้อมูล':
        flex_message = FlexSendMessage(
            alt_text='การเปลี่ยนแปลงข้อมูล',
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
                                    "text": "การเปลี่ยนแปลงข้อมูล",
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
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "Email",
                                        "uri": config['e_service']['change_personal_info']['email']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "ชื่อนามสกุล",
                                        "uri": config['e_service']['change_personal_info']['name']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "เบอร์โทร",
                                        "uri": config['e_service']['change_personal_info']['tel']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "password",
                                        "uri": config['e_service']['change_personal_info']['password']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "PIN",
                                        "uri": config['e_service']['change_personal_info']['pin']
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "ที่อยู่",
                                        "uri": config['e_service']['change_personal_info']['address']
                                    }
                                },
                            ],
                            "flex": 0
                        }
                    }
        )
        line_bot_api.reply_message(reply_tok, flex_message)

    elif receive_text == 'การฝากเงิน':
        buttons_template_message = TemplateSendMessage(
            alt_text='การฝากเงิน',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='การฝากเงิน',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(label='เงื่อนไขการฝากเงิน', text='เงื่อนไขการฝากเงิน'),
                    MessageAction(label='ขั้นตอนการฝากเงิน', text='ขั้นตอนการฝากเงิน'),
                    MessageAction(label='ฝากเงินผ่าน QR-code', text='ฝากเงินผ่าน QR-code'),
                    MessageAction(label='ฝากเงินผ่านช่องทาง ATS', text='ฝากเงินผ่านช่องทาง ATS'),
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'ขั้นตอนการฝากเงิน':
        buttons_template_message = TemplateSendMessage(
            alt_text='ขั้นตอนการฝากเงิน',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='ขั้นตอนการฝากเงิน',
                text=config['e_service']['deposit']['deposit_step'],
                actions=[
                    MessageAction(label='ฝากเงินผ่าน QR-code', text='ฝากเงินผ่าน QR-code'),
                    MessageAction(label='ฝากเงินผ่านช่องทาง ATS', text='ฝากเงินผ่านช่องทาง ATS'),
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'ฝากเงินผ่าน qr-code'.lower():
        mes = config['e_service']['deposit']['qr_code']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'เงื่อนไขการฝากเงิน':
        mes = config['e_service']['deposit']['deposit_condition']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    elif receive_text == 'ฝากเงินผ่านช่องทาง ats':
        mes = config['e_service']['deposit']['deposit_ats']
        line_bot_api.reply_message(reply_tok, TextSendMessage(mes))

    return True


    