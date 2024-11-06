import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from rembg import remove
from PIL import Image, ImageTk
import threading


class RemoveBackgroundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Remove Background App")
        self.root.geometry("500x600")

        # Inisialisasi elemen GUI
        self.label = tk.Label(self.root, text="Remove Background Tool", font=("Arial", 16))
        self.label.pack(pady=10)

        self.upload_button = tk.Button(self.root, text="Pilih Gambar", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.process_button = tk.Button(self.root, text="Hapus Latar Belakang", command=self.start_remove_bg,
                                        state=tk.DISABLED)
        self.process_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Simpan Hasil", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.progress_label = tk.Label(self.root, text="")
        self.progress_label.pack()

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.input_image = None
        self.output_image = None
        self.display_image_thumbnail = None

    def upload_image(self):
        # Dialog untuk memilih gambar
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.input_image = Image.open(file_path)
            # Tampilkan thumbnail pada GUI tanpa mengubah ukuran aslinya
            self.display_image_thumbnail = self.input_image.copy()
            self.display_image_thumbnail.thumbnail((300, 300))
            self.display_image(self.display_image_thumbnail)
            # Aktifkan tombol untuk memproses gambar
            self.process_button.config(state=tk.NORMAL)

    def display_image(self, image):
        # Tampilkan gambar pada GUI
        img_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def start_remove_bg(self):
        # Jalankan penghapusan latar belakang dalam thread terpisah
        threading.Thread(target=self.remove_bg).start()

    def remove_bg(self):
        if self.input_image:
            try:
                # Tampilkan progress bar
                self.progress_label.config(text="Proses penghapusan latar belakang sedang berjalan...")
                self.progress.pack(pady=10)
                self.progress["value"] = 0
                self.progress["maximum"] = 100

                # Simulasi progress update
                for i in range(1, 101):
                    self.progress["value"] = i
                    self.root.update_idletasks()
                    self.root.after(10)  # Menambahkan jeda untuk simulasi progress

                # Hapus latar belakang menggunakan rembg
                self.output_image = remove(self.input_image)

                # Tampilkan hasilnya di GUI (gunakan thumbnail untuk tampilan, simpan ukuran asli)
                self.display_image_thumbnail = self.output_image.copy()
                self.display_image_thumbnail.thumbnail((300, 300))
                self.display_image(self.display_image_thumbnail)

                # Aktifkan tombol simpan
                self.save_button.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
            finally:
                # Hentikan progress bar
                self.progress.pack_forget()
                self.progress_label.config(text="Proses selesai.")
        else:
            messagebox.showerror("Error", "Pilih gambar terlebih dahulu!")

    def save_image(self):
        if self.output_image:
            # Dialog untuk menyimpan gambar
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if file_path:
                self.output_image.save(file_path)
                messagebox.showinfo("Berhasil", "Gambar berhasil disimpan!")
        else:
            messagebox.showerror("Error", "Tidak ada gambar untuk disimpan!")


if __name__ == "__main__":
    root = tk.Tk()
    app = RemoveBackgroundApp(root)
    root.mainloop()
