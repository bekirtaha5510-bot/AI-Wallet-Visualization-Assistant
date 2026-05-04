import os
import sys

python_dir = sys.base_prefix

os.environ["TCL_LIBRARY"] = os.path.join(python_dir, "tcl", "tcl8.6")
os.environ["TK_LIBRARY"] = os.path.join(python_dir, "tcl", "tk8.6")

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import requests


MODEL_NAME = "qwen2.5:0.5b"


class WalletApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Destekli Akıllı Cüzdan")
        self.root.geometry("900x650")

        self.expenses = {}

        title = tk.Label(
            root,
            text="AI Destekli Akıllı Cüzdan: Harcama Görselleştirme Asistanı",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        income_frame = tk.Frame(root)
        income_frame.pack(pady=5)

        tk.Label(income_frame, text="Aylık Gelir (TL):", font=("Arial", 11)).grid(row=0, column=0, padx=5)
        self.income_entry = tk.Entry(income_frame, width=20)
        self.income_entry.grid(row=0, column=1, padx=5)

        expense_frame = tk.Frame(root)
        expense_frame.pack(pady=10)

        tk.Label(expense_frame, text="Kategori:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
        self.category_entry = tk.Entry(expense_frame, width=20)
        self.category_entry.grid(row=0, column=1, padx=5)

        tk.Label(expense_frame, text="Tutar (TL):", font=("Arial", 11)).grid(row=0, column=2, padx=5)
        self.amount_entry = tk.Entry(expense_frame, width=20)
        self.amount_entry.grid(row=0, column=3, padx=5)

        add_button = tk.Button(
            expense_frame,
            text="Harcama Ekle",
            command=self.add_expense,
            width=15
        )
        add_button.grid(row=0, column=4, padx=5)

        self.expense_list = tk.Listbox(root, width=80, height=8)
        self.expense_list.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        analyze_button = tk.Button(
            button_frame,
            text="Bütçe Analizi Yap",
            command=self.analyze_budget,
            width=20
        )
        analyze_button.grid(row=0, column=0, padx=5)

        bar_button = tk.Button(
            button_frame,
            text="Bar Grafik Göster",
            command=self.show_bar_chart,
            width=20
        )
        bar_button.grid(row=0, column=1, padx=5)

        pie_button = tk.Button(
            button_frame,
            text="Pasta Grafik Göster",
            command=self.show_pie_chart,
            width=20
        )
        pie_button.grid(row=0, column=2, padx=5)

        ai_button = tk.Button(
            button_frame,
            text="AI Yorum Al",
            command=self.get_ai_comment,
            width=20
        )
        ai_button.grid(row=0, column=3, padx=5)

        self.result_text = tk.Text(root, width=100, height=18)
        self.result_text.pack(pady=10)

    def add_expense(self):
        category = self.category_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

        if not category or not amount_text:
            messagebox.showwarning("Uyarı", "Kategori ve tutar alanlarını doldurmalısın.")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Hata", "Tutar sayısal bir değer olmalıdır.")
            return

        if amount <= 0:
            messagebox.showerror("Hata", "Tutar 0'dan büyük olmalıdır.")
            return

        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

        self.expense_list.insert(tk.END, f"{category}: {amount:.2f} TL")

        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def get_income(self):
        income_text = self.income_entry.get().strip()

        if not income_text:
            messagebox.showwarning("Uyarı", "Aylık gelir alanını doldurmalısın.")
            return None

        try:
            income = float(income_text)
        except ValueError:
            messagebox.showerror("Hata", "Gelir sayısal bir değer olmalıdır.")
            return None

        if income <= 0:
            messagebox.showerror("Hata", "Gelir 0'dan büyük olmalıdır.")
            return None

        return income

    def analyze_budget(self):
        income = self.get_income()

        if income is None:
            return

        if not self.expenses:
            messagebox.showwarning("Uyarı", "En az bir harcama eklemelisin.")
            return

        total_expense = sum(self.expenses.values())
        remaining_budget = income - total_expense
        expense_ratio = (total_expense / income) * 100
        saving_ratio = (remaining_budget / income) * 100
        max_category = max(self.expenses, key=self.expenses.get)

        result = f"""
BÜTÇE ANALİZİ

Toplam Gelir: {income:.2f} TL
Toplam Gider: {total_expense:.2f} TL
Kalan Bütçe: {remaining_budget:.2f} TL

Gelire Göre Harcama Oranı: %{expense_ratio:.2f}
Tasarruf Oranı: %{saving_ratio:.2f}

En Yüksek Harcama Kategorisi: {max_category}
En Yüksek Harcama Tutarı: {self.expenses[max_category]:.2f} TL

VERİ GÖRSELLEŞTİRME YORUMU

- Bar grafik, harcama kategorilerini karşılaştırmak için kullanılır.
- Pasta grafik, her kategorinin toplam gider içindeki oranını göstermek için kullanılır.
- Bu proje kategorik veri, sayısal veri, karşılaştırma ve parça-bütün ilişkisi konularını içerir.
"""

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

    def show_bar_chart(self):
        if not self.expenses:
            messagebox.showwarning("Uyarı", "Grafik için önce harcama eklemelisin.")
            return

        categories = list(self.expenses.keys())
        amounts = list(self.expenses.values())

        plt.figure(figsize=(9, 5))
        plt.bar(categories, amounts)
        plt.title("Kategoriye Göre Harcamalar")
        plt.xlabel("Harcama Kategorileri")
        plt.ylabel("Tutar (TL)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    def show_pie_chart(self):
        if not self.expenses:
            messagebox.showwarning("Uyarı", "Grafik için önce harcama eklemelisin.")
            return

        categories = list(self.expenses.keys())
        amounts = list(self.expenses.values())

        plt.figure(figsize=(7, 7))
        plt.pie(amounts, labels=categories, autopct="%1.1f%%")
        plt.title("Harcamaların Toplam Gider İçindeki Payı")
        plt.tight_layout()
        plt.show()

    def get_ai_comment(self):
        income = self.get_income()

        if income is None:
            return

        if not self.expenses:
            messagebox.showwarning("Uyarı", "AI yorum için önce harcama eklemelisin.")
            return

        total_expense = sum(self.expenses.values())
        remaining_budget = income - total_expense
        expense_ratio = (total_expense / income) * 100
        saving_ratio = (remaining_budget / income) * 100
        max_category = max(self.expenses, key=self.expenses.get)
        max_amount = self.expenses[max_category]

        if remaining_budget > 0:
            budget_status = (
                "Kalan bütçeniz pozitif olduğu için ay sonunda bütçeniz eksiye düşmemektedir. "
                "Ancak kalan miktarın yeterli olup olmadığını anlamak için düzenli takip yapılmalıdır."
            )
        elif remaining_budget == 0:
            budget_status = (
                "Gelir ve gideriniz eşittir. Bu durumda ay sonunda tasarruf edilecek bir miktar kalmamaktadır."
            )
        else:
            budget_status = (
                "Giderleriniz gelirinizden fazladır. Bu durum bütçe açığı oluşturur ve harcamaların azaltılması gerekir."
            )

        if expense_ratio >= 90:
            risk_comment = (
                "Toplam gideriniz gelirinizin büyük bölümünü oluşturmaktadır. "
                "Bu nedenle bütçe riskiniz yüksek seviyededir."
            )
        elif expense_ratio >= 70:
            risk_comment = (
                "Toplam gideriniz gelirinizin önemli bir kısmını oluşturmaktadır. "
                "Harcamalarınızı kontrollü yönetmeniz gerekir."
            )
        else:
            risk_comment = (
                "Toplam gider oranınız daha dengeli görünmektedir. "
                "Bu durum tasarruf yapma ihtimalinizi artırır."
            )

        rule_based_comment = f"""
AI DESTEKLİ BÜTÇE YORUMU

1. Genel Durum
Geliriniz {income:.2f} TL, toplam gideriniz {total_expense:.2f} TL ve kalan bütçeniz {remaining_budget:.2f} TL'dir.

2. Harcama Oranı
Toplam gideriniz gelirinizin %{expense_ratio:.2f}'lik kısmını oluşturmaktadır.
Tasarruf oranınız %{saving_ratio:.2f} olarak hesaplanmıştır.

3. En Yüksek Harcama
En yüksek harcama kategoriniz "{max_category}" kategorisidir.
Bu kategori için {max_amount:.2f} TL harcama yapılmıştır.

4. Kalan Bütçe Yorumu
{budget_status}

5. Risk Yorumu
{risk_comment}

6. Tasarruf Önerileri
- En yüksek harcama kategoriniz olan "{max_category}" alanını gözden geçirin.
- Eğlence, dışarıda yemek, alışveriş gibi değişken harcamaları azaltmayı deneyin.
- Her ay gelirinizden küçük de olsa sabit bir tasarruf miktarı ayırmaya çalışın.

7. Veri Görselleştirme Açıklaması
- Bar grafik, harcama kategorilerini karşılaştırmak için kullanılır.
- Pasta grafik, her kategorinin toplam gider içindeki payını göstermek için kullanılır.
- Bu analizde kategorik veri, sayısal veri ve parça-bütün ilişkisi birlikte kullanılmıştır.
"""

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, rule_based_comment)


if __name__ == "__main__":
    root = tk.Tk()
    app = WalletApp(root)
    root.mainloop()