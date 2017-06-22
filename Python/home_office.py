#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import random
from twx.botapi import TelegramBot, ReplyKeyboardMarkup

def main():
    last_update=0
    bot = TelegramBot('TOKEN')
    sender_id="ID do Destinatario"
    excuses = [
            'Os motoristas de onibus entraram de greve',
            'O cachorro faleceu',
            'Estou no trono desde cedo',
            'Não estou me sentindo bem',
            'O pneu do carro está do avesso'
            ]
    message=('Vou trabalhar de casa hoje. '+ random.choice(excuses) +".")
    bot.send_message(sender_id,message).wait()

if __name__ == '__main__':
        main()

