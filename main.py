import os

def remove_text_from_names(folder_path, text_to_remove):
    try:
        # Рекурсивно обрабатываем все файлы и подпапки в указанной директории
        for root, dirs, files in os.walk(folder_path):
            for name in files + dirs:
                old_path = os.path.join(root, name)

                # Создаем новое имя, убирая указанный текст
                new_name = name.replace(text_to_remove, '')

                # Создаем новый путь с новым именем
                new_path = os.path.join(root, new_name)

                # Переименовываем файл или папку
                os.rename(old_path, new_path)
                print(f"Переименовано: {old_path} -> {new_path}")

        print("Процесс завершен.")

    except Exception as e:
        print(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    # Замените 'ПУТЬ_К_ПАПКЕ' на путь к вашей целевой папке
    folder_path = input("Введите путь к папке: ")

    # Замените 'ТЕКСТ_ДЛЯ_УДАЛЕНИЯ' на текст, который вы хотите удалить из имен
    text_to_remove = input("Введите текст для удаления: ")

    remove_text_from_names(folder_path, text_to_remove)
