# здесь будет Илюшина функция
import pandas as pd
import os
import io
from django.conf import settings

BASE_DIR = settings.BASE_DIR


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
                                    'result.xlsx')
    with open(result_file_path, 'wb') as f:
        f.write(output.getbuffer())
