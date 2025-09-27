import subprocess
import os
from tkinter import filedialog, messagebox

class Folder():
    def __init__(self):
        self.current_folder = ''
        self.timestamp_file = ''
        self.video_file = ''

    def get_tfile(self):
        try:
            #self.timestamp_file = filedialog.askopenfile().name.split('/')[-1]
            self.timestamp_file = filedialog.askopenfile(filetypes=[("Текстовые файлы", "*.txt")]).name
            print(self.timestamp_file)
            message = f'''Выбран фaйл с таймингами👇\n"{self.timestamp_file}"'''
            messagebox.showinfo(title='Инфо', message=message)
        except Exception as e:
            message = f'''Ошибка при выборе файла таймингов'''
            messagebox.showerror(title='Ошибка', message=message)

    def get_vfile(self):
        try:
        #self.video_file = filedialog.askopenfile().name.split('/')[-1]
            self.video_file = filedialog.askopenfile(filetypes=[("Текстовые файлы", "*.mp4")]).name
            print(self.video_file)
            message = f'''Выбран видео файл 👇\n"{self.video_file}"'''
            messagebox.showinfo(title='Инфо', message=message)
        except Exception as e:
            message = f'''Ошибка при выборе видео файла'''
            messagebox.showerror(title='Ошибка', message=message)


def convert_video(input_file, output_file, start, end):
    #print(input_file, output_file, start, end)
    """
    Конвертирует видео файл с помощью ffmpeg
    """
    try:
        # Проверяем существование входного файла
        if not os.path.exists(input_file):
            print(f"Ошибка: файл {input_file} не существует")
            return False

        #ffmpeg -i input.mp4 -ss 00:01:30 -to 00:02:45 -c copy output.mp4
        #print(input_file)
        print(input_file)
        output_dir = input_file.split('.')[0]
        os.makedirs(output_dir, exist_ok=True)  # создаст папку, если её нет

        output_file = os.path.join(output_dir, output_file)
        if end == None:
            # Команда ffmpeg
            command = [
                'ffmpeg',
                "-y",
                '-i', input_file,
                '-ss', start,
                '-c', 'copy',
                output_file
            ]
        else:
            # Команда ffmpeg
            command = [
                'ffmpeg',
                "-y",
                '-i', input_file,
                '-ss', start,
                '-to', end,
                '-c', 'copy',
                output_file
            ]

        print(f"Запуск команды: {' '.join(command)}")

        # Запускаем процесс
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")

        if result.returncode == 0:
            print(f"Конвертация завершена успешно: {output_file}")
            return True
        else:
            print(f"Ошибка при конвертации:")
            print(result.stderr)
            return False

    except FileNotFoundError:
        print("Ошибка: ffmpeg не найден. Убедитесь, что ffmpeg установлен и добавлен в PATH")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return False

def convert_video_for_bt(input_file, output_file, start, end):
    # print(input_file, output_file, start, end)
    """
    Конвертирует видео файл с помощью ffmpeg
    """
    try:
        # Проверяем существование входного файла
        if not os.path.exists(input_file):
            print(f"Ошибка: файл {input_file} не существует")
            return False

        # ffmpeg -i input.mp4 -ss 00:01:30 -to 00:02:45 -c:v mpeg4 -q:v 3 -c:a aac -b:a 128k -movflags +faststart -vf "format=yuv420p" output.mp4 -y
        # print(input_file)
        print(input_file)
        output_dir = f'{input_file.split('.')[0]} a345bt'
        os.makedirs(output_dir, exist_ok=True)  # создаст папку, если её нет

        output_file = os.path.join(output_dir, output_file)
        if end == None:
            # Команда ffmpeg
            command = [
                'ffmpeg',
                "-y",
                '-i', input_file,
                '-ss', start,
                '-c:v', 'h264',
                '-q:v', '3',
                '-c:a', 'aac',
                '-b:a', '128k',
                '-movflags', '+faststart',
                '-vf', 'format=yuv420p',
                output_file
            ]
        else:
            # Команда ffmpeg
            command = [
                'ffmpeg',
                "-y",
                '-i', input_file,
                '-ss', start,
                '-to', end,
                '-c:v', 'h264',
                '-q:v', '3',
                '-c:a', 'aac',
                '-b:a', '128k',
                '-movflags', '+faststart',
                '-vf', 'format=yuv420p',
                output_file
            ]

        print(f"Запуск команды: {' '.join(command)}")

        # Запускаем процесс
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")

        if result.returncode == 0:
            print(f"Конвертация завершена успешно: {output_file}")
            return True
        else:
            print(f"Ошибка при конвертации:")
            print(result.stderr)
            return False

    except FileNotFoundError:
        print("Ошибка: ffmpeg не найден. Убедитесь, что ffmpeg установлен и добавлен в PATH")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return False


