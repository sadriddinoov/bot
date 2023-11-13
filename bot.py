from telegram import Update ,InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackContext,CallbackQueryHandler,ConversationHandler,MessageHandler,Filters)

TDTU_Ota_onalar,TDTU_Oqituvchilar,TDTU_Oquvchilar=('👨‍👩‍👦Ota-onalar','👨‍🏫O`qituvchilar','🧑🏻‍🎓O`quvchilar')

main_button =ReplyKeyboardMarkup([
    [TDTU_Ota_onalar,TDTU_Oqituvchilar],[TDTU_Oquvchilar]

 ], resiza_keyboard=True)
WORLD_TIL=1
WORLD_NEXT=2
def biz(update: Update, context: CallbackContext):

 keyboard = [
         [   
             InlineKeyboardButton("🇺🇿 Uzbek", callback_data='Uzbek'),
             InlineKeyboardButton("🇷🇺 Rus", callback_data='Rus')
        ],
        [InlineKeyboardButton("🇺🇸 English", callback_data='English')],
    ]

 update.message.reply_html((f'Assalomu Alaykum Hurmatli foydalanuvchi {update.effective_user.first_name} \n <b>  Xush kelibsiz TDTU_Kundalik_botiga  </b>'), reply_markup = InlineKeyboardMarkup(keyboard))
 return WORLD_TIL
def UZB_Ota_onalar(update,context):
    update.message.reply_text ('👨‍👩‍👦Ota-onalar tanlandi')
def UZB_Oqituvchilar(update,context):
    update.message.reply_text('👨‍🏫O`qituvchilar tanlandi')
def UZB_Oquvchilar(update,context):
    update.message.reply_text('🧑🏻‍🎓O`quvchilar tanlandi')
  
def siz_callback(update,context):
    query=update.callback_query
    query.message.delete()
    query.message.reply_html(text='<b> Siz bizning botimizda baholaringizni korishingiz mumkun 2️⃣0️⃣2️⃣2️⃣ ! </b> \n Quyidagilardan birini tanlang 👇', reply_markup=main_button)
    return WORLD_NEXT
updater = Updater('6181104239:AAEJplkG01kCKuDm_7E2nwp4sCEPvyCBc_o') 


con_hand=ConversationHandler(
    entry_points=[CommandHandler('start',biz)],
    states={
           WORLD_TIL:[CallbackQueryHandler(siz_callback)],
           WORLD_NEXT:[
           MessageHandler(Filters.regex('^('+TDTU_Ota_onalar+')$'),UZB_Ota_onalar),
           MessageHandler(Filters.regex('^('+TDTU_Oqituvchilar+')$'),UZB_Oqituvchilar),
           MessageHandler(Filters.regex('^('+TDTU_Oquvchilar+')$'),UZB_Oquvchilar),
         
           ],
    },
    fallbacks=[CommandHandler('start',biz)]

 )
updater.dispatcher.add_handler(con_hand)


updater.start_polling()
updater.idle()