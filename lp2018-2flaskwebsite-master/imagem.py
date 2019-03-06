# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import datetime as dt

DATE_FORMAT = '%d/%m/%Y'

DAY = dt.timedelta(1)

def to_date(date):
    return dt.datetime.strptime(date, DATE_FORMAT)

def to_str(date):
    return dt.datetime.strftime(date, DATE_FORMAT)

courier = lambda size: ImageFont.truetype('fonts/cour.ttf', size)

def carteirinha(aluno, save=False):
    filename = 'images/CarteiraModel.jpg'
    filename2 = 'images/Foto_{}.jpg'.format(aluno['cpf'])

    imagem = Image.open(filename)
    imagem3x4 = Image.open(filename2)
    imagem3x4 = imagem3x4.resize((134, 166), Image.ANTIALIAS)

    imagem.paste(imagem3x4, (320,110))
    #imagem.show()

    #FONTE DA PRIMEIRA FOLHA DA CARTEIRINHA

    # IMPRIMINDO O NOME DO USUARIO
    ImageDraw.Draw(imagem).text((142, 56),  # Coordinates
    aluno['nome'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    #IMPRIMINDO UNIDADE
    ImageDraw.Draw(imagem).text((42, 163),  # Coordinates
    aluno['unidade'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO O CURSO
    ImageDraw.Draw(imagem).text((42, 203),  # Coordinates
    aluno['curso'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO A FILIACAO
    ImageDraw.Draw(imagem).text((512, 21),  # Coordinates
    aluno['nome_mae'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))
    ImageDraw.Draw(imagem).text((512, 36),  # Coordinates
    aluno['nome_pai'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO A NATURALIDADE
    ImageDraw.Draw(imagem).text((508, 75),  # Coordinates
    aluno['naturalidade'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO A NACIONALIDADE
    ImageDraw.Draw(imagem).text((688, 75),  # Coordinates
    aluno['nacionalidade'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO O NASCIMENTO
    ImageDraw.Draw(imagem).text((828, 75),  # Coordinates
    aluno['nascimento'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO O CPF
    ImageDraw.Draw(imagem).text((508, 110),  # Coordinates
    aluno['cpf'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO O RG
    ImageDraw.Draw(imagem).text((648, 110),  # Coordinates
    aluno['identidade'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO O ORGAO
    ImageDraw.Draw(imagem).text((737, 110),  # Coordinates
    aluno['orgao'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO A EXPEDICAO
    ImageDraw.Draw(imagem).text((827, 110),  # Coordinates
    aluno['expedicao'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO UF
    ImageDraw.Draw(imagem).text((907, 110),  # Coordinates
    aluno['uf'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO A EXPEDICAO
    ImageDraw.Draw(imagem).text((142, 93),  # Coordinates
    aluno['dre'],  # Text
    (0, 0, 0),  # Color
    font = courier(12))

    # IMPRIMINDO EXPEDICAO
    today = dt.date.today()
    ImageDraw.Draw(imagem).text((242, 93),  # Coordinates
    to_str(today),  # Text
    (0, 0, 0),  # Color
    font=courier(12))
    # IMPRIMINDO VALIDADE
    
    tomorrow = today + DAY
    ImageDraw.Draw(imagem).text((338, 93),  # Coordinates
    to_str(tomorrow),  # Text
    (0, 0, 0),  # Color
    font=courier(12))

    if save:
        imagem.save('temp/carteirinha_{}.png'.format(aluno['cpf']))
    else:
        imagem.show()
