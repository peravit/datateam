import os
import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, StickerSendMessage, \
                           TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction

from utils.loaders import load_json

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

config = load_json('configs.json')
# config['buttonsImageURL'] = 'https://www.liberator.co.th//images/icon-20.png'

def product_text(reply_tok, receive_text, source):
    if receive_text == 'product':
        buttons_template_message = TemplateSendMessage(
            alt_text='Product',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='Product',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(
                        label='Equity',
                        text='Equity'
                    ),
                    MessageAction(
                        label='TFEX',
                        text='TFEX'
                    ),
                    # URIAction(
                    #     label='uri',
                    #     uri='http://example.com/'
                    # )
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'equity':
        buttons_template_message = TemplateSendMessage(
            alt_text='Equity',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='Equity',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(
                        label='Cash balance',
                        text='Cash balance'
                    ),
                    MessageAction(
                        label='Cash account',
                        text='Cash account'
                    ),
                    URIAction(
                        label='ค่าธรรมเนียม',
                        uri=config['product']['equity_fee']
                    )
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)
    
    elif receive_text == 'cash account':
        line_bot_api.reply_message(reply_tok, TextSendMessage(config['product']['cash_account']))
    
    elif receive_text == 'cash balance':
        line_bot_api.reply_message(reply_tok, TextSendMessage(config['product']['cash_balance']))
    
    elif receive_text == 'tfex':
        buttons_template_message = TemplateSendMessage(
            alt_text='TFEX',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='TFEX',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(
                        label='Margin Call',
                        text='Margin Call'
                    ),
                    URIAction(
                        label='ค่าธรรมเนียม',
                        uri=config['product']['tfex_fee']
                    ),
                    URIAction(
                        label='หลักประกัน',
                        uri=config['product']['tfex_margin']
                    )
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)

    elif receive_text == 'margin call':
        line_bot_api.reply_message(reply_tok, TextSendMessage(config['product']['margin_call']))
    
    return True