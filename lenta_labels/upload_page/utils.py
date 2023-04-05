# здесь будет Илюшина функция
import pandas as pd
import os
import io
from django.conf import settings

BASE_DIR = settings.BASE_DIR


# функция обработки шаблона во вшивную этикету одежды
def get_format(file_path):
    file_path = os.path.join(BASE_DIR, 'upload_documents', 'template.xlsx')
    x1 = pd.read_excel(file_path)
    df = x1
    df['1'] = ""
    df['2'] = "состав:"
    df['3'] = "place for care symbols"
    df['4'] = "Страна происхождения: "
    df4 = pd.DataFrame()
    df4 = df[
        ['1', '1', 'Бренд', '1', 'артикул', '1', 'Размер', '1', '2', 'Состав',
         '1', '1', 'EAN изделия', '1', '3', '1', 'Страна происхождения', '1',
         '1']].copy()
    df4['Страна происхождения'] = df['4'].astype(str) + df4[
        'Страна происхождения'].astype(str)
    df4 = df4_transposed = df4.T
    df4 = df4_transposed

    # Записываем результат в io.BytesIO
    output = io.BytesIO()
    df4.to_excel(output, index=False, header=False)
    output.seek(0)

    # Сохраняем файл в директорию upload_documents
    result_file_path = os.path.join(BASE_DIR, 'upload_documents',
                                    'lousy_label.xlsx')
    with open(result_file_path, 'wb') as f:
        f.write(output.getbuffer())


def get_format_label(file_path):
    file_path = os.path.join(BASE_DIR, 'upload_documents', 'template.xlsx')
    x1 = pd.read_excel(file_path)
    df2 = x1
    df2['1'] = ""
    df2['2'] = "Дата изготовления:"
    df2['3'] = "place for care symbols"
    df2['4'] = "Страна происхождения: "
    df2[
        'Срок службы ограничен физическим износом изделия.'] = 'Срок службы ограничен физическим износом изделия.'
    df2['артикул модель'] = 'Артикул/модель: '
    df2['Размер :'] = 'Размер: '
    df2['Состав :'] = 'Состав : '
    df2['4'] = "Страна-изготовитель:"
    df2[
        '5'] = 'Импортёр, уполномоченная организация на принятие претензий и поставщик в РФ: ООО «ЛЕНТА», Россия, 197374, г. Санкт-Петербург, ул. Савушкина, д. 112, литера Б. Мы ждем ваши отзывы по телефону горячей линии: 8-800-700-4-111 (на территории РФ звонок бесплатный) и по адресу: private.label@lenta.com.'
    df2['6'] = 'Срок службы ограничен физическим износом изделия.'
    df2['7'] = 'Изготовитель:'
    df2['8'] = 'Адрес производства:'
    df3 = pd.DataFrame()
    df3 = df2[
        ['1', 'Бренд', '1', 'Наименование', '1', 'артикул', 'Размер', 'Состав',
         '3',
         'ИЗГОТОВИТЕЛЬ, КОТОРЫЙ  УКАЗАН НА ЭТИКЕТКЕ\n/ Company name, Legal Adress',
         'АДРЕС РЕАЛЬНОГО ИЗГОТОВИТЕЛЯ, КОТОРЫЙ  УКАЗАН НА ЭТИКЕТКЕ\n/Adress real factory production  ',
         'Страна происхождения', '5', '1', '2', '6', '1', 'EAN изделия',
         '1']].copy()
    df3['артикул'] = df2['артикул модель'].astype(str) + df3['артикул'].astype(
        str)
    df3['Размер'] = df2['Размер :'].astype(str) + df3['Размер'].astype(str)
    df3['Состав'] = df2['Состав :'].astype(str) + df3['Состав'].astype(str)
    df3['Страна происхождения'] = df2['4'].astype(str) + df3[
        'Страна происхождения'].astype(str)
    df3[
        'ИЗГОТОВИТЕЛЬ, КОТОРЫЙ  УКАЗАН НА ЭТИКЕТКЕ\n/ Company name, Legal Adress'] = \
    df2['7'].astype(str) + df3[
        'ИЗГОТОВИТЕЛЬ, КОТОРЫЙ  УКАЗАН НА ЭТИКЕТКЕ\n/ Company name, Legal Adress'].astype(
        str)
    df3[
        'АДРЕС РЕАЛЬНОГО ИЗГОТОВИТЕЛЯ, КОТОРЫЙ  УКАЗАН НА ЭТИКЕТКЕ\n/Adress real factory production  '] = \
    df2['8'].astype(str) + df3[
        'АДРЕС РЕАЛЬНОГО ИЗГОТОВИТЕЛЯ, КОТОРЫЙ  УКАЗАН НА ЭТИКЕТКЕ\n/Adress real factory production  '].astype(
        str)
    df3 = df3_transposed = df3.T  # or df1.transpose()
    df3 = df3_transposed
    # Записываем результат в io.BytesIO
    output = io.BytesIO()
    df3.to_excel(output, index=False, header=False)
    output.seek(0)

    result_file_path = os.path.join(BASE_DIR, 'upload_documents',
                                    'label_on_item.xlsx')
    with open(result_file_path, 'wb') as f:
        f.write(output.getbuffer())




