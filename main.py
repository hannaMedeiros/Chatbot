import telebot
from telebot import types
import sqlite3
from partidasAPI import buscar_partidas
import unicodedata

bot = telebot.TeleBot('8113761349:AAHzR5o-6MYueywTD-C0fJUgBKrX_mpLue0')

status = {}

@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    menu = types.InlineKeyboardMarkup( )
    botao_curiosidades = types.InlineKeyboardButton('❓ Curiosidades', callback_data= 'curiosidades')
    botao_partidas = types.InlineKeyboardButton('🎮 Partidas', callback_data = 'partidas')
    botão_redes = types.InlineKeyboardButton('Redes Sociais da Furia', callback_data = 'redes_sociais')

    menu.add(botao_curiosidades, botao_partidas, botão_redes)

    texto = "Olá! Sou o bot da FURIA. Escolha uma opção abaixo:"
    bot.send_message(msg.chat.id, texto, reply_markup=menu)

@bot.message_handler(commands=['menu'])
def menu(msg):
    start(msg)

@bot.message_handler(func=lambda msg: msg.text.lower() == "menu")
def exibir_menu(msg: telebot.types.Message):
    menu = types.InlineKeyboardMarkup( )
    botao_curiosidades = types.InlineKeyboardButton('❓ Curiosidades', callback_data= 'curiosidades')
    botao_partidas = types.InlineKeyboardButton('🎮 Partidas', callback_data = 'partidas')
    botão_redes = types.InlineKeyboardButton('Redes Sociais da Furia', callback_data = 'redes_sociais')

    menu.add(botao_curiosidades, botao_partidas, botão_redes)

    texto = "Olá! Sou o bot da FURIA. Escolha uma opção abaixo:"
    bot.send_message(msg.chat.id, texto, reply_markup=menu)

@bot.callback_query_handler(func=lambda call: call.data == 'redes_sociais')
def redes_sociais(call):

    menu_redes = types.InlineKeyboardMarkup()

    botao_insta = types.InlineKeyboardButton('Instagram', url = "https://www.instagram.com/furiagg/")
    botao_twitter = types.InlineKeyboardButton('Twitter/X', url="https://x.com/FURIA")
    botao_youtube = types.InlineKeyboardButton('YouTube', url="https://www.youtube.com/@FURIAggCS")
    botao_site = types.InlineKeyboardButton('Site Oficial', url="https://www.furia.gg/")
    botao_twitch = types.InlineKeyboardButton('Twitch', url="https://www.twitch.tv/furiatv")

    menu_redes.add(botao_insta)
    menu_redes.add(botao_twitter)
    menu_redes.add(botao_youtube)
    menu_redes.add(botao_site)
    menu_redes.add(botao_twitch)
    texto = "Aqui estão as redes sociais da FURIA:"
    bot.send_message(call.message.chat.id, texto, reply_markup=menu_redes)

@bot.callback_query_handler(func=lambda call: True)
def click_botao(call:types.CallbackQuery):
    chat_id = call.message.chat.id
    if call.data == 'curiosidades':
        status[call.message.chat.id] = 'curiosidades' 
        bot.send_message(chat_id, 'Você selecionou Curiosidades! Agora envie sua pergunta:')

    elif call.data == 'partidas':
        status[chat_id] = 'partidas'
        partidas = buscar_partidas()
        if partidas:
            bot.send_message(chat_id, partidas, parse_mode='Markdown')
        else:
            bot.send_message(chat_id, "Não foi possível buscar partidas no momento.")
        
        del status[chat_id]
           

@bot.message_handler(func=lambda msg: True)
def responder(msg: types.Message):
    chat_id = msg.chat.id
    if status.get(chat_id) == 'curiosidades':
        resposta = buscar_resposta(msg.text)

        if resposta == 'Desculpe, não sei a resposta sobre isso 😕.':
            bot.send_message(chat_id, "Desculpe, não sei a resposta sobre isso 😕.Tente perguntar de outra forma.")
            return
        else:
                bot.send_message(chat_id, resposta)
            

def remover_acentos(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt)
                   if unicodedata.category(c) != 'Mn')


def buscar_resposta(pergunta):
    conn = sqlite3.connect('cs_chatbot.db')
    cursor = conn.cursor()

    ignorar = ['o', 'a', 'de', 'em', 'é', 'no', 'na', 'os', 'as', 'um', 'uma', 'e', 'ou', 'qual', 'como', 'por', 'que']
    palavras_usuario = [p for p in pergunta.lower().split() if p not in ignorar]

    cursor.execute("SELECT pergunta, resposta FROM faq_cs")
    resultados = cursor.fetchall()

    melhores_respostas = []

    for pergunta_db, resposta in resultados:
        palavras_db = [remover_acentos(p.lower()) for p in pergunta_db.split()]
        pontuacao = sum(1 for p in palavras_usuario if p in palavras_db)

        if pontuacao > 0:
            melhores_respostas.append((pontuacao, resposta))


    conn.close()

    if melhores_respostas:
        melhores_respostas.sort(reverse=True, key=lambda x: x[0])
        return melhores_respostas[0][1]
    
    else:
        return 'Desculpe, não sei a resposta sobre isso 😕. Tente perguntar de outra forma.'




bot.infinity_polling()

