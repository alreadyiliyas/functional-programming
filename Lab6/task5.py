# Напишите программу, которая любой введенный казахский текст из кириллицы переводит в латиницу.
# Халқымызбен жұмыла тойлайтын қазақтың қанына сінген төл мерекеміз әз Наурызда келд
text = input("Enter text: ")
latinica = ''
size = len(text)
i = 0
while i < size:
    if text[i] == 'А':
        latinica = latinica + 'А'
    if text[i] == 'а':
        latinica = latinica + 'а'
    if text[i] == 'Ә':
        latinica = latinica + 'Á'
    if text[i] == 'ә':
        latinica = latinica + 'á'
    if text[i] == 'Б':
        latinica = latinica + 'В'
    if text[i] == 'б':
        latinica = latinica + 'b'
    if text[i] == 'Д':
        latinica = latinica + 'D'
    if text[i] == 'д':
        latinica = latinica + 'd'
    if text[i] == 'Е':
        latinica = latinica + 'Е'
    if text[i] == 'е':
        latinica = latinica + 'е'
    if text[i] == 'Ф':
        latinica = latinica + 'F'
    if text[i] == 'ф':
        latinica = latinica + 'f'
    if text[i] == 'Г':
        latinica = latinica + 'g'
    if text[i] == 'г':
        latinica = latinica + 'g'
    if text[i] == 'Ғ':
        latinica = latinica + 'Ǵ'
    if text[i] == 'ғ':
        latinica = latinica + 'ǵ'
    if text[i] == 'Х':
        latinica = latinica + 'H'
    if text[i] == 'х':
        latinica = latinica + 'h'
    if text[i] == 'И':
        latinica = latinica + 'I'
    if text[i] == 'и':
        latinica = latinica + 'ı'
    if text[i] == 'Й':
        latinica = latinica + 'I'
    if text[i] == 'й':
        latinica = latinica + 'ı'
    if text[i] == 'І':
        latinica = latinica + 'І'
    if text[i] == 'і':
        latinica = latinica + 'і'
    if text[i] == 'Ж':
        latinica = latinica + 'J'
    if text[i] == 'ж':
        latinica = latinica + 'j'
    if text[i] == 'Л':
        latinica = latinica + 'L'
    if text[i] == 'л':
        latinica = latinica + 'l'
    if text[i] == 'М':
        latinica = latinica + 'М'
    if text[i] == 'м':
        latinica = latinica + 'm'
    if text[i] == 'Н':
        latinica = latinica + 'N'
    if text[i] == 'н':
        latinica = latinica +  'n'
    if text[i] == 'Ң':
        latinica = latinica +  'Ñ'
    if text[i] == 'ң':
        latinica = latinica +  'ñ'
    if text[i] == 'Ө':
        latinica = latinica +  'Ö'
    if text[i] == 'ө':
        latinica = latinica +  'ö'
    if text[i] == 'П':
        latinica = latinica +  'P'
    if text[i] == 'п':
        latinica = latinica +  'p'
    if text[i] == 'Қ':
        latinica = latinica +  'Q'
    if text[i] == 'қ':
        latinica = latinica + 'q'
    if text[i] == 'Р':
        latinica = latinica + 'R'
    if text[i] == 'К':
        latinica = latinica + 'К'
    if text[i] == 'к':
        latinica = latinica + 'к'
    if text[i] == 'р':
        latinica = latinica + 'r'
    if text[i] == 'С':
        latinica = latinica + 'S'
    if text[i] == 'с':
        latinica = latinica + 's'
    if text[i] == 'О':
        latinica = latinica + 'О'
    if text[i] == 'о':
        latinica = latinica + 'о'
    if text[i] == 'Ш':
        latinica = latinica + "SH"
    if text[i] == 'ш':
        latinica = latinica + "sh"
    if text[i] == 'т':
        latinica = latinica + 't'
    if text[i] == 'У':
        latinica = latinica + 'Ý'
    if text[i] == 'у':
        latinica = latinica + 'ý'
    if text[i] == 'Ұ':
        latinica = latinica + 'U'
    if text[i] == 'ұ':
        latinica = latinica + 'u'
    if text[i] == 'Ү':
        latinica = latinica + 'Ú'
    if text[i] == 'ү':
        latinica = latinica + 'ú'
    if text[i] == 'В':
        latinica = latinica + 'V'
    if text[i] == 'в':
        latinica = latinica + 'v'
    if text[i] == 'Ы':
        latinica = latinica + 'Y'
    if text[i] == 'ы':
        latinica = latinica + 'y'
    if text[i] == 'З':
        latinica = latinica + 'Z'
    if text[i] == 'з':
        latinica = latinica + 'z'
    if text[i] == ' ':
        latinica = latinica + ' '

    i += 1


print(latinica)
