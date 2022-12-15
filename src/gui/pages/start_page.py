import tkinter as tk


class StartPage(tk.Frame):
    def donothing(self):
        filewin = tk.Toplevel(self.master)
        button = tk.Button(filewin, text="Do nothing button")
        button.pack()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        heading = tk.Label(
            self,
            bg="white",
            fg="black",
            text='Tugas Akhir',
            font='none 24 bold'
        )
        heading.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        text_elements = [
            "Memasukkan Pesan ke Gambar",
            "Mengekstraksi Pesan dari Gambar",
            "Confidentiality Pesan",
            "Recovery Pesan"
        ]

        command_elements = [
            lambda: controller.show_frame("ImageInsertionForm"),
            lambda: controller.show_frame("ImageExtractForm"),
            lambda: controller.show_frame("ImageExtractFormnoAES"),
            lambda: controller.show_frame("ImageRecoveryForm"),
        ]

        index = 0
        for text in text_elements:
            button = tk.Button(
                self,
                bg='white',
                fg='black',
                text=text,
                command=command_elements[index],
                width=50,
                height=2
            )
            button.place(relx=0.5, rely=0.1*(index+2), anchor=tk.CENTER)
            index += 1
