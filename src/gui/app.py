import tkinter as tk

from src.gui.pages.start_page import StartPage
from src.gui.pages.end_page import EndPage
from src.gui.pages.image.insert_form import ImageInsertionForm
from src.gui.pages.image.extract_from import ImageExtractForm
from src.gui.pages.image.extract_fromnoaes import ImageExtractFormnoAES
from src.gui.pages.image.recovery_form import ImageRecoveryForm


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ImageInsertionForm, ImageExtractForm, ImageExtractFormnoAES, ImageRecoveryForm):
            page_name = F.__name__

            frame = F(parent=self.container, controller=self)
            frame.configure(bg='white')
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_end_frame(self, title, stegano_type, file_dir, psnr, mse, compute_time, capacity):
        frame = EndPage(parent=self.container, controller=self,
                        title=title, stegano_type=stegano_type, file_dir=file_dir, psnr=psnr, mse=mse, compute_time=compute_time, capacity=capacity)
        frame.configure(bg='white')
        frame.grid(row=0, column=0, sticky="nsew")
