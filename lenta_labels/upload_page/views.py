from django.conf import settings
from django.http import StreamingHttpResponse
from django.shortcuts import render
from lenta_labels.settings import BASE_DIR
import os
from upload_page.utils import get_format
from upload_page.utils import get_format_label
from django.urls import reverse

# BASE_DIR = settings.BASE_DIR


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

        # Вызываем функции для обработки файлов
        get_format(file_path)
        get_format_label(file_path)


        # Возвращаем пользователю страницу с сообщением об успешной загрузке
        result_file_path_lousy = os.path.join(BASE_DIR, 'upload_documents',
                                              'lousy_label.xlsx')
        url_lousy = reverse('download_file',
                            args=[os.path.basename(result_file_path_lousy)])
        download_url_lousy = request.build_absolute_uri(url_lousy)

        result_file_path_mounted = os.path.join(BASE_DIR, 'upload_documents',
                                                'mounted_label.xlsx')
        url_mounted = reverse('download_file',
                              args=[
                                  os.path.basename(result_file_path_mounted)])
        download_url_mounted = request.build_absolute_uri(url_mounted)

        return render(request, 'results.html',
                      {'success': 'Файлы успешно загружены и обработаны',
                       'download_url_lousy': download_url_lousy,
                       'download_url_mounted': download_url_mounted})

    # Если метод запроса GET, то просто возвращаем страницу загрузки файла
    return render(request, 'upload_page.html')


# def download_file(request, file_name):
#     """Эта функция download_file представляет собой обработчик запроса, который
#      отправляет пользователю файл, расположенный на сервере по указанному пути
#      file_path.
#     Функция открывает файл в бинарном режиме ('rb') с помощью функции open,
#     создает объект StreamingHttpResponse с содержимым файла в качестве
#     параметра и устанавливает тип содержимого файла
#     'application/vnd.ms-excel'). Затем она устанавливает заголовок
#     Content-Disposition, который сообщает браузеру, что файл должен быть
#     скачан, а не отображен в браузере, и возвращает объект
#     StreamingHttpResponse.
#     Пользователь получает содержимое файла в виде скачиваемого файла с
#     именем file_name."""
#     file_path = os.path.join(BASE_DIR, 'upload_documents', file_name)
#     file = open(file_path, 'rb')
#     response = StreamingHttpResponse(file,
#                                      content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = f'attachment; filename="{file_name}"'
#     return response

def download_file(request, file_names):
    links = []
    for file_name in file_names:
        file_path = os.path.join(BASE_DIR, 'upload_documents', file_name)
        file = open(file_path, 'rb')
        response = StreamingHttpResponse(file,
                                         content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        links.append(response)
        return render(request, 'results.html', {'links': links})
