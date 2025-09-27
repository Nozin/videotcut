from datetime import datetime
from tkinter import *
import os
import sys
from utils import convert_video, convert_video_for_bt, Folder
from tkinter import messagebox
from PIL import Image, ImageTk  # для работы с .jpg и другими форматами

root = Tk()
version = 0.1
root['bg'] = 'grey'
root.title(f'tvideocut v{version}')
#root.wm_attributes('-alpha', version)



def run_cutting(timestamp, input_video, convert_flag=False):
    if timestamp == '' or input_video == '':
        message = f'''Ошибка, не выбраны файлы'''
        messagebox.showerror(title='Ошибка', message=message)
        return
    result = []
    try:
        with open(timestamp, "r", encoding="utf-8") as f:
            file = f.read().split("\n")
            for line in file:
                line = line.split(" ")
                if len(line[-1]) <= 5:
                    start_time = datetime.strptime(line[-1], "%M:%S").time()
                elif  7 > len(line[-1]) > 5:
                    start_time = datetime.strptime(line[-1], "%H:%M:%S").time()
                else:
                    raise ValueError()
                name = ' '.join(line[:-1])
                result.append((name, str(start_time)))
    except FileNotFoundError as e:
        print('Ошибка файлов timestamp', e)
        message = f'''Ошибка файлов timestamp'''
        messagebox.showerror(title='Ошибка', message=message)
    print(result)
    if result:
        try:
            for  i in range(0, len(result)):
                input_video = input_video
                output_video = result[i][0]
                start = result[i][1]
                if i==len(result)-1:
                    end = None
                else:
                    end = result[i+1][1]
                print(output_video,start, end)
                if convert_flag:
                    if (convert_video(input_video, f'{output_video}.mp4', start, end)
                            and convert_video_for_bt(input_video, f'{output_video}.mp4', start, end)):
                        print("Готово!")
                    else:
                        print("Произошла ошибка")
                else:
                    if convert_video(input_video, f'{output_video}.mp4', start, end):
                        print("Готово!")
                    else:
                        print("Произошла ошибка")
        except Exception as e:
            message = f'''Ошибка'''
            messagebox.showerror(title='Ошибка', message=message)


def resource_path(relative_path):
    """Получает абсолютный путь к ресурсу, работает для разработки и PyInstaller."""
    try:
        base_path = sys._MEIPASS  # Путь к временной папке PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Путь для разработки
    return os.path.join(base_path, relative_path)



# Пример использования
if __name__ == "__main__":
    image = Image.open(resource_path("unnamed.png"))
    image = image.resize((640, 480), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    root.geometry('640x480')
    root.resizable(width=False, height=False)

    canvas = Canvas(root, height=640, width=480, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(1, 1, image=photo, anchor="nw")

    frame = Frame(root)
    frame.place(relx=0.5, rely=0.15, anchor='center')
    # title = Label(frame, text='Подсказка', bg='grey', font = 40)

    f = Folder()

    choose_filename = Button(frame, text='Выбрать тайминги', bg='yellow', command=f.get_tfile)
    choose_filename.pack()

    choose_folder_button = Button(frame, text='Выбрать файл для нарезки', bg='yellow', command=f.get_vfile)
    choose_folder_button.pack()

    cut1 = Button(frame, text='Нарезать', bg='yellow',
                      command=lambda: run_cutting(f.timestamp_file, f.video_file))
    cut1.pack()
    cut2 = Button(frame, text='Нарезать два раза с форматированием', bg='yellow',
                      command=lambda: run_cutting(f.timestamp_file, f.video_file, True))
    cut2.pack()

    root.mainloop()
