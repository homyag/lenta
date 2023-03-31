from django.shortcuts import render
from lenta_labels.settings import BASE_DIR
import os
from upload_page.utils import get_format


def upload_page(request):
    return render(request, 'upload_page.html')


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        # Проверка наличия файла
        if file is None:
            # Обработка ошибки, если файл не был загружен
            return render(request, 'upload_page.html', {'error': 'Файл не был '
                                                                 'загружен'})

        # Сохраняем файл в директорию upload_documents
        file_path = os.path.join(BASE_DIR, 'upload_documents', file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Вызываем функцию get_format для обработки файла
        get_format(file_path)

        # Возвращаем пользователю страницу с сообщением об успешной загрузке
        return render(request, 'results.html', {'success': 'Файл успешно '
                                                               'загружен и обработан'})

    # Если метод запроса GET, то просто возвращаем страницу загрузки файла
    return render(request, 'upload_page.html')
