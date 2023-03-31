from django.http import FileResponse, Http404, StreamingHttpResponse
from django.shortcuts import render
from lenta_labels.settings import BASE_DIR
import os
from upload_page.utils import get_format
from django.urls import reverse


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
        result_file_path = os.path.join(BASE_DIR, 'upload_documents',
                                        'result.xlsx')
        url = reverse('download_file',
                      args=[os.path.basename(result_file_path)])
        download_url = request.build_absolute_uri(url)
        return render(request, 'results.html',
                      {'success': 'Файл успешно загружен и обработан',
                       'download_url': download_url})

    # Если метод запроса GET, то просто возвращаем страницу загрузки файла
    return render(request, 'upload_page.html')


def download_file(request, file_name):
    """Эта функция download_file представляет собой обработчик запроса, который
     отправляет пользователю файл, расположенный на сервере по указанному пути
     file_path.
    Функция открывает файл в бинарном режиме ('rb') с помощью функции open,
    создает объект StreamingHttpResponse с содержимым файла в качестве
    параметра и устанавливает тип содержимого файла
    'application/vnd.ms-excel'). Затем она устанавливает заголовок
    Content-Disposition, который сообщает браузеру, что файл должен быть
    скачан, а не отображен в браузере, и возвращает объект
    StreamingHttpResponse.
    Пользователь получает содержимое файла в виде скачиваемого файла с
    именем file_name."""
    file_path = os.path.join(BASE_DIR, 'upload_documents', file_name)
    file = open(file_path, 'rb')
    response = StreamingHttpResponse(file,
                                     content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
