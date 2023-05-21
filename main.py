import play# import

text1 = play.new_text(words='г - гладити, з - зіграти, с - спати', font_size=30, x=0,
                      y=play.screen.top-20)
text2 = play.new_text(words='к - кормити, п - прибрати, пробіл - піти', font_size=30, x=0,
                           y=play.screen.top-45)
player = play.new_image(image='1.png', x=0, y=0, size=150)

speech = play.new_text(words=None, x=0, y=play.screen.bottom+20)
speech.words = "Привіт, давай дружити!"
eat = True

@play.when_program_starts# коли програма запускається
def start():
    pass


@play.repeat_forever
async def do():
    global eat
    if play.key_is_pressed('г') or play.key_is_pressed('Г'):
        player.image = '7.png'
        player.size = 80
        speech.words = "Мммм..., як приємно)"
        await play.timer(2)
        player.size = 150
        player.image = "2.png"
        speech.words = 'Хочу щееееее!'
    if play.key_is_pressed('к') and eat == True:
        player.image = '6.png'
        speech.words = "Боже як це смачно..."
        await play.timer(2)
        player.image = "2.png"
        speech.words = 'Я смачно попоїв'
        eat = False
    if play.key_is_pressed('к') and eat == False:
        player.image = '4.png'
        speech.words = "Оце я наївся"
        await play.timer(2)
        player.image = "3.png"
        speech.words = 'та прибери вже за мною'
    if play.key_is_pressed('п'):
        player.image = '4.png'
        speech.words = "Ох, нарешті дякую"
        await play.timer(2)
        player.image = "3.png"
        speech.words = 'Фух'
        eat = True
play.start_program()