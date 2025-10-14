import tkinter as tk
from tkinter import messagebox
import math


class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def setVolumen(self, v):
        self.volumen = v

    def setSuperficie(self, s):
        self.superficie = s

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcularSuperficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return (4/3) * math.pi * self.radio ** 3

    def calcularSuperficie(self):
        return 4 * math.pi * self.radio ** 2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return (self.base ** 2) * self.altura / 3

    def calcularSuperficie(self):
        return (self.base ** 2) + 2 * self.base * self.apotema


class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Esfera")
        self.configure(bg="#ffffff")
        self.crearComponentes()
        self.update()
        self.resizable(False, False)

    def crearComponentes(self):
        tk.Label(self, text="Esfera", bg="#ffffff", fg="#440099", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 5))

        tk.Label(self, text="Radio (cm):", bg="#ffffff", fg="#440099").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entradaRadio = tk.Entry(self, bg="#ffffff", fg="#440099", font=("Arial", 12), relief="solid", bd=2, justify="center")
        self.entradaRadio.grid(row=1, column=1, padx=10, pady=5)

        btnFrame = tk.Frame(self, bg="#ffffff")
        btnFrame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(btnFrame, text="Calcular", command=self.calcular,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btnFrame, text="Limpiar", command=self.limpiar,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btnFrame, text="Volver", command=self.volver,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)

        self.lblVolumen = tk.Label(self, text="Volumen (cm³): ", bg="#ffffff", fg="#440099")
        self.lblVolumen.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.lblSuperficie = tk.Label(self, text="Superficie (cm²): ", bg="#ffffff", fg="#440099")
        self.lblSuperficie.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def validarFloat(self, texto, nombre):
        try:
            val = float(texto)
            if val < 0:
                raise ValueError("negativo")
            return val
        except (ValueError, TypeError):
            raise ValueError(f"Entrada inválida para {nombre}. Debe ser un número no negativo.")

    def calcular(self):
        try:
            r = self.validarFloat(self.entradaRadio.get().strip(), "radio")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        figura = Esfera(r)
        self.lblVolumen.config(text=f"Volumen (cm³): {figura.volumen:.2f}")
        self.lblSuperficie.config(text=f"Superficie (cm²): {figura.superficie:.2f}")

    def limpiar(self):
        self.entradaRadio.delete(0, tk.END)
        self.lblVolumen.config(text="Volumen (cm³): ")
        self.lblSuperficie.config(text="Superficie (cm²): ")

    def volver(self):
        self.destroy()
        self.master.deiconify()
class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Cilindro")
        self.configure(bg="#ffffff")
        self.crearComponentes()
        self.update()
        self.resizable(False, False)

    def crearComponentes(self):
        tk.Label(self, text="Cilindro", bg="#ffffff", fg="#440099", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 5))

        tk.Label(self, text="Radio (cm):", bg="#ffffff", fg="#440099").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entradaRadio = tk.Entry(self, bg="#ffffff", fg="#440099", font=("Arial", 12), relief="solid", bd=2, justify="center")
        self.entradaRadio.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Altura (cm):", bg="#ffffff", fg="#440099").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entradaAltura = tk.Entry(self, bg="#ffffff", fg="#440099", font=("Arial", 12), relief="solid", bd=2, justify="center")
        self.entradaAltura.grid(row=2, column=1, padx=10, pady=5)

        btnFrame = tk.Frame(self, bg="#ffffff")
        btnFrame.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(btnFrame, text="Calcular", command=self.calcular,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btnFrame, text="Limpiar", command=self.limpiar,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btnFrame, text="Volver", command=self.volver,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)

        self.lblVolumen = tk.Label(self, text="Volumen (cm³): ", bg="#ffffff", fg="#440099")
        self.lblVolumen.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.lblSuperficie = tk.Label(self, text="Superficie (cm²): ", bg="#ffffff", fg="#440099")
        self.lblSuperficie.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def validarFloat(self, texto, nombre):
        try:
            val = float(texto)
            if val < 0:
                raise ValueError("negativo")
            return val
        except (ValueError, TypeError):
            raise ValueError(f"Entrada inválida para {nombre}. Debe ser un número no negativo.")

    def calcular(self):
        try:
            r = self.validarFloat(self.entradaRadio.get().strip(), "radio")
            h = self.validarFloat(self.entradaAltura.get().strip(), "altura")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        figura = Cilindro(r, h)
        self.lblVolumen.config(text=f"Volumen (cm³): {figura.volumen:.2f}")
        self.lblSuperficie.config(text=f"Superficie (cm²): {figura.superficie:.2f}")

    def limpiar(self):
        self.entradaRadio.delete(0, tk.END)
        self.entradaAltura.delete(0, tk.END)
        self.lblVolumen.config(text="Volumen (cm³): ")
        self.lblSuperficie.config(text="Superficie (cm²): ")

    def volver(self):
        self.destroy()
        self.master.deiconify()

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Pirámide")
        self.configure(bg="#ffffff")
        self.crearComponentes()
        self.update()
        self.resizable(False, False)

    def crearComponentes(self):
        tk.Label(self, text="Pirámide", bg="#ffffff", fg="#440099", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 5))

        tk.Label(self, text="Base (cm):", bg="#ffffff", fg="#440099").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entradaBase = tk.Entry(self, bg="#ffffff", fg="#440099", font=("Arial", 12), relief="solid", bd=2, justify="center")
        self.entradaBase.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Altura (cm):", bg="#ffffff", fg="#440099").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entradaAltura = tk.Entry(self, bg="#ffffff", fg="#440099", font=("Arial", 12), relief="solid", bd=2, justify="center")
        self.entradaAltura.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Apotema (cm):", bg="#ffffff", fg="#440099").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entradaApotema = tk.Entry(self, bg="#ffffff", fg="#440099", font=("Arial", 12), relief="solid", bd=2, justify="center")
        self.entradaApotema.grid(row=3, column=1, padx=10, pady=5)

        btnFrame = tk.Frame(self, bg="#ffffff")
        btnFrame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(btnFrame, text="Calcular", command=self.calcular,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btnFrame, text="Limpiar", command=self.limpiar,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btnFrame, text="Volver", command=self.volver,
                  bg="#440099", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)

        self.lblVolumen = tk.Label(self, text="Volumen (cm³): ", bg="#ffffff", fg="#440099")
        self.lblVolumen.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.lblSuperficie = tk.Label(self, text="Superficie (cm²): ", bg="#ffffff", fg="#440099")
        self.lblSuperficie.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def validarFloat(self, texto, nombre):
        try:
            val = float(texto)
            if val < 0:
                raise ValueError("negativo")
            return val
        except (ValueError, TypeError):
            raise ValueError(f"Entrada inválida para {nombre}. Debe ser un número no negativo.")

    def calcular(self):
        try:
            b = self.validarFloat(self.entradaBase.get().strip(), "base")
            h = self.validarFloat(self.entradaAltura.get().strip(), "altura")
            a = self.validarFloat(self.entradaApotema.get().strip(), "apotema")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        figura = Piramide(b, h, a)
        self.lblVolumen.config(text=f"Volumen (cm³): {figura.volumen:.2f}")
        self.lblSuperficie.config(text=f"Superficie (cm²): {figura.superficie:.2f}")

    def limpiar(self):
        self.entradaBase.delete(0, tk.END)
        self.entradaAltura.delete(0, tk.END)
        self.entradaApotema.delete(0, tk.END)
        self.lblVolumen.config(text="Volumen (cm³): ")
        self.lblSuperficie.config(text="Superficie (cm²): ")

    def volver(self):
        self.destroy()
        self.master.deiconify()

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("300x200")
        self.configure(bg="#ffffff")
        self.crearComponentes()

    def crearComponentes(self):
        tk.Label(self, text="Seleccione una figura:", bg="#ffffff", fg="#440099", font=("Arial", 12, "bold")).pack(pady=20)

        tk.Button(self, text="Cilindro", command=self.abrirCilindro,
                  bg="#ff6a13", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

        tk.Button(self, text="Esfera", command=self.abrirEsfera,
                  bg="#ff6a13", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

        tk.Button(self, text="Pirámide", command=self.abrirPiramide,
                  bg="#ff6a13", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

    def abrirCilindro(self):
        self.withdraw()
        VentanaCilindro(self)

    def abrirEsfera(self):
        self.withdraw()
        VentanaEsfera(self)

    def abrirPiramide(self):
        self.withdraw()
        VentanaPiramide(self)

# Ejecutar la aplicación
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()