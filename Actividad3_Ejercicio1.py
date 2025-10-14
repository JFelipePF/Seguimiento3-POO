import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcularPromedio(self):
        return sum(self.lista_notas) / len(self.lista_notas) if self.lista_notas else 0.0

    def calcularDesviacion(self):
        n = len(self.lista_notas)
        if n == 0:
            return 0.0
        prom = self.calcularPromedio()
        suma = sum((x - prom) ** 2 for x in self.lista_notas)
        return math.sqrt(suma / n)

    def calcularMenor(self):
        return min(self.lista_notas) if self.lista_notas else 0.0

    def calcularMayor(self):
        return max(self.lista_notas) if self.lista_notas else 0.0


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas del Estudiante")
        self.geometry("600x300")
        self.configure(bg="#ffffff")
        self.notas = Notas()
        self._crear_componentes()

    def _crear_componentes(self):
        self.campos = []

        estilo_entry = {
            "bg": "#ffffff",
            "fg": "#440099",
            "font": ("Arial", 12),
            "relief": "solid",
            "bd": 2,
            "justify": "center"
        }

        # Frame horizontal para notas
        frame_notas = tk.Frame(self, bg="#ffffff")
        frame_notas.place(x=20, y=20)

        for i in range(5):
            sub_frame = tk.Frame(frame_notas, bg="#ffffff")
            sub_frame.pack(side="left", padx=10)

            lbl = tk.Label(sub_frame, text=f"Nota {i+1}", bg="#ffffff", fg="#440099", font=("Arial", 10, "bold"))
            lbl.pack()
            entrada = tk.Entry(sub_frame, **estilo_entry, width=8)
            entrada.pack()
            self.campos.append(entrada)

        # Botones
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular,
                                 bg="#440099", fg="white", font=("Arial", 10, "bold"))
        btn_calcular.place(x=150, y=100, width=100, height=30)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar,
                                bg="#440099", fg="white", font=("Arial", 10, "bold"))
        btn_limpiar.place(x=270, y=100, width=100, height=30)

        # Resultados
        self.lbl_promedio = tk.Label(self, text="Promedio = ", bg="#ffffff", fg="#440099", font=("Arial", 10))
        self.lbl_promedio.place(x=20, y=150, width=560, height=23)

        self.lbl_desviacion = tk.Label(self, text="Desviación estándar = ", bg="#ffffff", fg="#440099", font=("Arial", 10))
        self.lbl_desviacion.place(x=20, y=180, width=560, height=23)

        self.lbl_mayor = tk.Label(self, text="Valor mayor = ", bg="#ffffff", fg="#440099", font=("Arial", 10))
        self.lbl_mayor.place(x=20, y=210, width=560, height=23)

        self.lbl_menor = tk.Label(self, text="Valor menor = ", bg="#ffffff", fg="#440099", font=("Arial", 10))
        self.lbl_menor.place(x=20, y=240, width=560, height=23)

    def calcular(self):
        try:
            for i, campo in enumerate(self.campos):
                texto = campo.get().strip()
                if texto == "":
                    raise ValueError(f"Falta la nota {i+1}")
                valor = float(texto)
                self.notas.lista_notas[i] = valor
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
            return

        promedio = self.notas.calcularPromedio()
        desviacion = self.notas.calcularDesviacion()
        mayor = self.notas.calcularMayor()
        menor = self.notas.calcularMenor()

        self.lbl_promedio.config(text=f"Promedio = {promedio:.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
        self.lbl_mayor.config(text=f"Valor mayor = {mayor}")
        self.lbl_menor.config(text=f"Valor menor = {menor}")

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Valor mayor = ")
        self.lbl_menor.config(text="Valor menor = ")
        self.notas = Notas()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()