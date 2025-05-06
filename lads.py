import tkinter as tk
from tkinter import messagebox

# pertanyaan buat ngenentuin love lang
questions = [
    {
        "text": "Kalau lagi stres, kamu paling senang kalau…",
        "options": [
            ("Dukungan dan semangat", "Words of Affirmation"),
            ("Bantuan menyelesaikan masalah", "Acts of Service"),
            ("Hadiah kecil", "Receiving Gifts"),
            ("Dateng langsung buat nemenin", "Quality Time"),
            ("Dipeluk", "Physical Touch")
        ]
    },
    {
        "text": "Saat ulang tahun, kamu paling pengen…",
        "options": [
            ("Dikasih kartu ucapan", "Words of Affirmation"),
            ("Dibuatin pesta", "Acts of Service"),
            ("Dikasih kado", "Receiving Gifts"),
            ("Ngabisin waktu bareng-bareng", "Quality Time"),
            ("Cuddle", "Physical Touch")
        ]
    },
    {
        "text": "Hal kecil yang bikin kamu tersenyum…",
        "options": [
            ("Ucapan pujian", "Words of Affirmation"),
            ("Dijemput tanpa diminta", "Acts of Service"),
            ("Dapet snack favorit secara spontan", "Receiving Gifts"),
            ("Makan siang bareng walau sibuk", "Quality Time"),
            ("Dirangkul bahunya", "Physical Touch")
        ]
    },
    {
        "text": "Apa yang bikin kamu merasa spesial?",
        "options": [
            ("Diyakinin kalau berharga", "Words of Affirmation"),
            ("Ngelakuin sesuatu tanpa diminta", "Acts of Service"),
            ("Diberi kenang-kenangan", "Receiving Gifts"),
            ("Didengerin tanpa distraksi", "Quality Time"),
            ("Digenggam tangannya saat bicara", "Physical Touch")
        ]
    },
    {
        "text": "Kalau kamu capek, kamu pengen...",
        "options": [
            ("Dikuatkan dengan kata-kata", "Words of Affirmation"),
            ("Dibantu mengurus pekerjaan", "Acts of Service"),
            ("Dibawain minuman atau camilan", "Receiving Gifts"),
            ("Ditemani istirahat", "Quality Time"),
            ("Dipeluk erat", "Physical Touch")
        ]
    },
    {
        "text": "Saat sedih, kamu lebih suka...",
        "options": [
            ("Ditenangkan lewat kata-kata", "Words of Affirmation"),
            ("Dibantu membereskan hal yang bikin sedih", "Acts of Service"),
            ("Dikasih barang yang menghibur", "Receiving Gifts"),
            ("Ditemani tanpa harus banyak bicara", "Quality Time"),
            ("Dirangkul/dipeluk", "Physical Touch")
        ]
    },
    {
        "text": "Cara kamu menunjukkan cinta ke orang lain adalah…",
        "options": [
            ("Bilang langsung 'aku sayang kamu'", "Words of Affirmation"),
            ("Membantu mereka", "Acts of Service"),
            ("Ngasih hadiah", "Receiving Gifts"),
            ("Ngajak jalan/jalan bareng", "Quality Time"),
            ("Sentuhan fisik (peluk, gandeng)", "Physical Touch")
        ]
    },
    {
        "text": "Pasangan kamu melakukan apa yang bikin kamu merasa paling dicintai?",
        "options": [
            ("Ngasih pujian atau kata manis", "Words of Affirmation"),
            ("Bantu kamu tanpa diminta", "Acts of Service"),
            ("Ngasih barang-barang favorit", "Receiving Gifts"),
            ("Luangin waktu walau sibuk", "Quality Time"),
            ("Ngasih pelukan hangat", "Physical Touch")
        ]
    },
    {
        "text": "Kalau LDR, kamu paling butuh...",
        "options": [
            ("Pesan kata cinta tiap hari", "Words of Affirmation"),
            ("Dia tetap bantu kamu dari jauh", "Acts of Service"),
            ("Kirim-kiriman paket/kado", "Receiving Gifts"),
            ("Video call rutin", "Quality Time"),
            ("Ketemu langsung sesekali", "Physical Touch")
        ]
    },
    {
        "text": "Apa yang kamu anggap sebagai bentuk kasih sayang paling tulus?",
        "options": [
            ("Kata-kata jujur dari hati", "Words of Affirmation"),
            ("Perbuatan nyata", "Acts of Service"),
            ("Memberi dari hati", "Receiving Gifts"),
            ("Kehadiran penuh perhatian", "Quality Time"),
            ("Gestur fisik penuh kehangatan", "Physical Touch")
        ]
    }
]

# score tracking buat love lang
scores = {
    "Words of Affirmation": 0,
    "Acts of Service": 0,
    "Receiving Gifts": 0,
    "Quality Time": 0,
    "Physical Touch": 0
}

# mapping love lang ke lads charas
li_mapping = {
    "Words of Affirmation": "Xavier - Si romantis yang ekspresif dan perhatian",
    "Acts of Service": "Zayne - Si misterius yang penuh kejutan",
    "Receiving Gifts": "Rafayel - Si pengayom yang selalu ada dalam tindakan",
    "Quality Time": "Sylus - Si tenang yang hadir sepenuh hati",
    "Physical Touch": "Caleb - Si protektif yang hangat dan menggenggam"
}

# GUI logic
class LoveLangApp:
    def __init__(self, master):
        self.master = master
        self.q_index = 0
        self.var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Sistem Pakar Penentuan LI Game Love and DeepSpace")
        self.master.geometry("600x400")
        self.master.config(bg="#f5f5f5")
        
        # header
        self.header_label = tk.Label(self.master, text="Siapa LI-mu di Lads", font=("Roboto", 16, "bold"), bg="#f5f5f5")
        self.header_label.pack(pady=20)

        # pertantaan
        self.question_label = tk.Label(self.master, text="", wraplength=500, font=("Roboto", 12), bg="#f5f5f5")
        self.question_label.pack(pady=10)

        # opsi (radio button)
        self.radio_buttons = []
        for _ in range(5):
            rb = tk.Radiobutton(self.master, variable=self.var, value="", wraplength=500, anchor="w", justify="left", font=("Roboto", 10))
            rb.pack(fill="x", padx=20, anchor="w", pady=5)
            self.radio_buttons.append(rb)

        #  button next
        self.next_btn = tk.Button(self.master, text="Next", command=self.next_question, font=("Roboto", 12), bg="#4CAF50", fg="white", relief="flat", bd=0,padx=10,pady=1)
        self.next_btn.pack(pady=20)

        self.show_question()

    def show_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=f"{self.q_index + 1}. {q['text']}")
        self.var.set(None)
        for i, (text, value) in enumerate(q["options"]):
            self.radio_buttons[i].config(text=text, value=value)

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Pilih Jawaban", "Silakan pilih salah satu jawaban!")
            return
        scores[selected] += 1
        self.q_index += 1
        if self.q_index >= len(questions):
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        top_lang = max(scores, key=scores.get)
        character = li_mapping[top_lang]
        messagebox.showinfo("Hasil", f"Love language dominanmu adalah: {top_lang}\n\nKarakter Love and DeepSpace yang cocok:\n{character}")
        self.master.destroy()

# Run the GUI app
root = tk.Tk()
app = LoveLangApp(root)
root.mainloop()
    
