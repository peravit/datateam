import os
import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, StickerSendMessage, \
                           TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, \
                            ImageCarouselTemplate, ImageCarouselColumn

from utils.loaders import load_json                           

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

config = load_json('configs.json')

def contact_text(reply_tok, receive_text, source):
    if receive_text == 'ช่องทางติดต่อ':
        buttons_template_message = TemplateSendMessage(
            alt_text='ช่องทางติดต่อ',
            template=ButtonsTemplate(
                thumbnail_image_url=config['buttonsImageURL'],
                title='ช่องทางติดต่อ',
                text='กรุณาเลือกรายการ',
                actions=[
                    MessageAction(label='Social media', text='Social media'),
                    MessageAction(label='ติดต่อ Admin', text='ติดต่อ Admin'),
                    URIAction(label='เว็บไซต์บริษัท', uri=config['contact']['company_website'])
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, buttons_template_message)


    elif receive_text == 'social media':
        image_carousel_template_message = TemplateSendMessage(
            alt_text='Social media',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url=config['buttonsImageURL'],
                        action=URIAction(label='Line', uri=config['contact']['company_line'])
                    ),
                    ImageCarouselColumn(
                        image_url=config['buttonsImageURL'],
                        action=URIAction(label='Facebook', uri=config['contact']['company_facebook'])
                    )
                ]
            )
        )
        line_bot_api.reply_message(reply_tok, image_carousel_template_message)
    
    elif receive_text == 'ติดต่อ admin':
        line_bot_api.reply_message(reply_tok, TextSendMessage(config['contact']['contact_admin']))
        
    
    return True