import flet as ft
from PIL import Image
import os


def main(page: ft.Page):
    home = os.path.expanduser("~")
    desktop_path = os.path.join(home, "Desktop")
    new_folder = f"{desktop_path}\\fletCompressedImages\\"
    page.theme_mode = ft.ThemeMode.DARK

    def file_picker_result(e: ft.FilePickerResultEvent):
        page.title = 'Images Compressor'
        if e.files:
            for f in e.files:
                original_path = f.path
                image = Image.open(original_path)
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                new_name = f'compressed_{f.name}'
                new_path = os.path.join(new_folder, new_name)
                image.save(new_path, optimize=True, quality=60)
                page.add(ft.SelectionArea(content=ft.Text(
                    f"Imagen procesada y guardada en: {new_folder}")))

    file_picker = ft.FilePicker(on_result=file_picker_result)
    page.overlay.append(file_picker)

    def open_compressed():
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        page.launch_url(new_folder)

    page.add(
        ft.Row(controls=[ft.ElevatedButton(
            text="Elegir imagen",
            on_click=lambda _: file_picker.pick_files(
                allow_multiple=True, allowed_extensions=['jpg', 'jpeg', 'png'])
        ),
            ft.ElevatedButton(
            text="Ver comprimidos",
            on_click=lambda _: open_compressed()
        )])
    )


ft.app(target=main)
