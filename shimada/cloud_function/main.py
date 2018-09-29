# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import os
import sys
import requests
import wsgiref.simple_server
from argparse import ArgumentParser

from builtins import bytes
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate,
    PostbackAction, MessageAction, URIAction, ImageCarouselTemplate, ImageCarouselColumn
)
from linebot.utils import PY3

NGROK_ADDRESS = os.getenv('NGROK_ADDRESS', None)

def linebot(request):
    signature = request.headers['X-Line-Signature']
    
    # get channel_secret and channel_access_token from your environment variable
    channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
    if channel_secret is None:
        print('Specify LINE_CHANNEL_SECRET as environment variable.')
        sys.exit(1)
    if channel_access_token is None:
        print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
        sys.exit(1)

    line_bot_api = LineBotApi(channel_access_token)
    parser = WebhookParser(channel_secret)

    # get request body as text
    body = request.get_data(as_text=True)

    events = parser.parse(body, signature)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        
        line_bot_api.reply_message(
            event.reply_token,
            set_reply_message(event.message.text)            
        )

def set_reply_message(user_message):
    """
    送られたメッセージによって返答を変えるために利用
    """
    if user_message == '嫁いまなにしてる':
        return create_buttons_template()
    elif user_message == "スタンプ":
        return create_stamp_message()
    else :
        return create_image_message(filename=user_message)

def create_buttons_template():
    """嫁いまなにしてる"""
    ## ラズパイへ
    url = '{address}/linebot'.format(address=NGROK_ADDRESS)
    # url = '{address}/linebot'.format(address=NGROK_ADDRESS)
    headers = {"content-type": "application/json"}
    r = requests.get(url, headers=headers)
    data = r.json()
    # print(data[0])
    # print(data[1])
    return TemplateSendMessage(
        alt_text='嫁いまなにしてる',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://storage.googleapis.com/smartse-team3/shipnaku_3.jpg',
            thumbnail_image_url='https://storage.googleapis.com/smartse-team3/{filename}'.format(filename=data[1]),
            # thumbnail_image_url='{address}/get_image'.format(address=NGROK_ADDRESS),
            title='嫁いまなにしてる',
            text=data[0],
            actions=[
                MessageAction(
                    label='rc_graph',
                    text='rc_graph'
                ),
                MessageAction(
                    label='line_graph',
                    text='line_graph'
                ),
                MessageAction(
                    label='heartbeat',
                    text='heartbeat'
                )
            ]
        )
    )

def create_stamp_message():
    """スタンプ"""
    return StickerSendMessage(sticker_id=1, package_id=1)

def create_image_message(filename):
    """画像"""
    return ImageSendMessage(
        original_content_url='{address}/get_image/{filename}.jpg'.format(address=NGROK_ADDRESS, filename=filename),
        preview_image_url='{address}/get_image/{filename}.jpg'.format(address=NGROK_ADDRESS, filename=filename)
        # original_content_url='https://storage.googleapis.com/smartse-team3/{filename}.jpg'.format(filename=filename),
        # preview_image_url='https://storage.googleapis.com/smartse-team3/{filename}.jpg'.format(filename=filename),
    )
