import tkinter as tk
import tkinter.filedialog as fd
import src.helper.gui as hg

from src.image.recovery import Recovery

class ImageRecoveryForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.initialize()

        hg.insert_header(self, 'Pengecekan Recovery Pesan')
        self.render_file_frame()
        self.render_fileextracted_frame()
        self.render_execute_frame()

    def initialize(self):
        self.TITLE_ROW = 0
        self.FILE_ROW = 1
        self.FILEEXTRACTED_ROW = 2
        self.EXECUTE_ROW = 3

        self.image_dir = tk.StringVar()
        self.image_dir.set('')

        self.message_dir = tk.StringVar()
        self.message_dir.set('')

    def render_file_frame(self):
        file_frame = hg.create_frame(self, self.FILE_ROW + 1)

        hg.create_label(file_frame, 'Gambar', 0, 0)
        hg.create_label(file_frame, self.image_dir, 0, 1, fix_text=False)
        hg.create_button(file_frame, 'Pilih',
                         lambda: self.load_image_file(), 1, 0)

    def render_fileextracted_frame(self):
        fileextracted_frame = hg.create_frame(self, self.FILEEXTRACTED_ROW + 1)

        hg.create_label(fileextracted_frame, 'Gambar', 0, 0)
        hg.create_label(fileextracted_frame, self.message_dir, 0, 1, fix_text=False)
        hg.create_button(fileextracted_frame, 'Pilih',
                         lambda: self.load_imageextracted_file(), 1, 0)

    def render_execute_frame(self):
        execute_frame = hg.create_frame(self, self.EXECUTE_ROW + 1)

        hg.create_button(execute_frame, 'Execute',
                         lambda: self.execute(), 0, 0)

        hg.create_button(execute_frame, 'Back',
                         lambda: self.controller.show_frame("StartPage"), 0, 1)

    def load_image_file(self):
        self.image_dir.set(fd.askopenfilename())

    def load_imageextracted_file(self):
        self.message_dir.set(fd.askopenfilename())

    def execute(self):
        print('> Image dir:', self.image_dir.get())
        print('> Image Extracted dir:', self.message_dir.get())

        image = self.image_dir.get()
        image_result = self.message_dir.get()

        Recovery(image, image_result)
        title='Pengecekan Selesai'
        self.controller.show_end_frame(title, "Image", 0, 0, 0, 0, 0)