# /**
#  * Copyright (C), 2023-2024, Sara Echeverria (bl33h)
#  * @uthor Sara Echeverria
#  * FileName: PCsSystem
#  * @version: II
#  * Creation: 24/04/2023
#  * Last modification: 25/04/2023
#  */

# Libraries import
from tkinter import *
import psycopg2
from tkinter import messagebox
from customtkinter import *
import customtkinter as ct

# Menu UI
class PCsSystem(Frame):
    def __init__(self, parent, master):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.win = CTkToplevel(parent)
        self.initUI()
    def initUI(self):
        self.win.title("PCs System")
        etiTitle = ct.CTkLabel(self.win, text="Welcome to PCs System!", font=("Arial", 20, "bold"))
        findPCbutton = ct.CTkButton(self.win, text="Search PC", command= lambda: FindPC(self.win), width=200)
        deletePCbutton = ct.CTkButton(self.win, text="Delete PC", command= lambda: DeletePC(self.win), width=200)
        adjustPriceButton = ct.CTkButton(self.win, text="Adjust PC price", command= lambda: AdjustPrice(self.win), width=200)
        checkPCbutton = ct.CTkButton(self.win, text="Check PC", command= lambda: CheckPC(self.win), width=200)
        
        
        etiTitle.pack(pady=5)
        findPCbutton.pack(pady=5)
        deletePCbutton.pack(pady=5)
        adjustPriceButton.pack(pady=5)
        checkPCbutton.pack(pady=5)
        
        self.win.geometry("500x500")

# Search PC 'transaction' function
class FindPC:
    def __init__(self, parent):
        self.parent = parent
        self.win = CTkToplevel(parent)
        self.win.title("Find PC")

        etiTitle = CTkLabel(self.win, text="Find PC", font=("Arial", 20, "bold"))
        velocity_lab = CTkLabel(self.win, text="Velocity")
        self.velocity_input = CTkEntry(self.win, width=200)
        ram_lab = CTkLabel(self.win, text="RAM")
        self.ram_input = CTkEntry(self.win, width=200)
        button_find = CTkButton(self.win, text="Find", command=self.find_pc, width=100)
        button_close = CTkButton(self.win, text="Close", command=self.close, width=100)

        etiTitle.pack(pady=5)
        velocity_lab.pack()
        self.velocity_input.pack(pady=5)
        ram_lab.pack()
        self.ram_input.pack(pady=5)
        button_find.pack(pady=5)
        button_close.pack(pady=5)
        self.win.geometry("600x200")

        # Database connection
        self.conn = psycopg2.connect(
            host="localhost",
            database="lab11",
            user="postgres",
            password="passworD"
        )

    def close(self):
        self.conn.close()
        self.win.destroy()

    def find_pc(self):
        velocidad = float(self.velocity_input.get())
        ram = int(self.ram_input.get())
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT modelo, precio FROM PC WHERE velocidad = {velocidad} AND ram = {ram};")
            pcs = cursor.fetchall()
            if pcs:
                message = "Matching PCs:\n\n"
                for pc in pcs:
                    message += f"Model number: {pc[0]}, price: {pc[1]}\n"
                messagebox.showinfo("Results", message)
            else:
                message = "No matching PCs found"
                messagebox.showinfo("Results", message)
        except Exception as e:
            messagebox.showerror("Error", f"Error finding PCs: {str(e)}")
        finally:
            cursor.close()

class DeletePC:
    def __init__(self, parent):
        self.parent = parent
        self.win = CTkToplevel(parent)
        self.win.title("Delete PC")

        etiTitle = CTkLabel(self.win, text="Delete PC", font=("Arial", 20, "bold"))
        modelo_lab = CTkLabel(self.win, text="Model Number")
        self.modelo_input = CTkEntry(self.win, width=200)

        button_delete = CTkButton(self.win, text="Delete", command=self.delete_pc, width=100)
        button_close = CTkButton(self.win, text="Close", command=self.close, width=100)

        etiTitle.pack(pady=5)
        modelo_lab.pack()
        self.modelo_input.pack(pady=5)
        button_delete.pack(pady=5)
        button_close.pack(pady=5)
        self.win.geometry("600x200")

        # Database connection
        self.conn = psycopg2.connect(
            host="localhost",
            database="lab11",
            user="postgres",
            password="passworD"
        )

    def close(self):
        self.conn.close()
        self.win.destroy()

    def delete_pc(self):
        modelo = self.modelo_input.get()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"DELETE FROM PC WHERE modelo = '{modelo}';")
            cursor.execute(f"DELETE FROM Producto WHERE modelo = '{modelo}';")
            if cursor.rowcount == 0:
                message = "There is no model with the given number."
            else:
                message = f"The PC with the model {modelo} has been eliminated."
            self.conn.commit()
            messagebox.showinfo("Results", message)
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error deleting PC: {str(e)}")
        finally:
            cursor.close()

# Adjust PC price based on a model 'transaction' function, a $100 discount
class AdjustPrice:
    def __init__(self, parent):
        self.parent = parent
        self.win = CTkToplevel()
        self.win.title("Adjust PC price")

        etiTitle = CTkLabel(self.win, text="Adjust PC price ($100 discount)", font=("Arial", 20, "bold"))
        mod_lab = CTkLabel(self.win, text="Model Number")
        self.mod_input = CTkEntry(self.win, width=200)

        etiTitle = CTkLabel(self.win, text="Adjust PC price", font=("Arial", 20, "bold"))
        mod_lab = CTkLabel(self.win, text="Model Number")
        self.mod_input = CTkEntry(self.win, width=200)
        button_delete = CTkButton(self.win, text="Adjust PC price", command=self.adjust_price, width=100)
        button_close = CTkButton(self.win, text="Close", command=self.close, width=100)

        etiTitle.pack(pady=5)
        mod_lab.pack()
        self.mod_input.pack(pady=5)
        button_delete.pack(pady=5)
        button_close.pack(pady=5)
        self.win.geometry("600x200")

        # Database connection
        self.conn = psycopg2.connect(
            host="localhost",
            database="lab11",
            user="postgres",
            password="passworD"
        )

    def close(self):
        self.conn.close()
        self.win.destroy()

    def adjust_price(self):
        modelo = self.mod_input.get()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"UPDATE PC SET precio = precio - 100 WHERE modelo = '{modelo}'")
            if cursor.rowcount == 0:
                message = "There is no model with the given number."
            else:
                message = f"The price of PC with the model {modelo} has been adjusted."
            self.conn.commit()
            messagebox.showinfo("Results", message)
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error deleting PC: {str(e)}")
        finally:
            cursor.close()

# Check PC 'transaction' function
class CheckPC:
    def __init__(self, parent):
        self.parent = parent
        self.win = CTkToplevel(parent)
        self.win.title("Check PC")

        etiTitle = CTkLabel(self.win, text="Check if PC exists in the system", font=("Arial", 20, "bold"))
        mak_lab = CTkLabel(self.win, text="Maker")
        self.mak_input = CTkEntry(self.win, width=200)
        mod_lab = CTkLabel(self.win, text="Model")
        self.mod_input = CTkEntry(self.win, width=200)
        vel_lab = CTkLabel(self.win, text="Velocity")
        self.vel_input = CTkEntry(self.win, width=200)
        ram_lab = CTkLabel(self.win, text="RAM")
        self.ram_input = CTkEntry(self.win, width=200)
        disc_lab = CTkLabel(self.win, text="Disc size")
        self.disc_input = CTkEntry(self.win, width=200)
        pri_lab = CTkLabel(self.win, text="Price")
        self.pri_input = CTkEntry(self.win, width=200)
        button_find = CTkButton(self.win, text="Check", command=self.check_pc, width=100)
        button_close = CTkButton(self.win, text="Close", command=self.close, width=100)

        etiTitle.pack(pady=5)
        mak_lab.pack()
        self.mak_input.pack(pady=5)
        mod_lab.pack()
        self.mod_input.pack(pady=5)
        vel_lab.pack()
        self.vel_input.pack(pady=5)
        ram_lab.pack()
        self.ram_input.pack(pady=5)
        disc_lab.pack()
        self.disc_input.pack(pady=5)
        pri_lab.pack()
        self.pri_input.pack(pady=5)
        button_find.pack(pady=5)
        button_close.pack(pady=5)
        self.win.geometry("600x200")

        # Database connection
        self.conn = psycopg2.connect(
            host="localhost",
            database="lab11",
            user="postgres",
            password="passworD"
        )
    
    def close(self):
        self.conn.close()
        self.win.destroy()

    def check_pc(self):
        fabricante = self.mak_input.get()
        modelo = self.mod_input.get()
        velocidad = float(self.vel_input.get())
        ram = int(self.ram_input.get())
        disco = int(self.disc_input.get())
        precio = float(self.pri_input.get())
        cursor = self.conn.cursor()
            
        try:
            cursor.execute(f"SELECT modelo, ram, velocidad, disco, precio FROM PC WHERE velocidad = {velocidad} AND ram = {ram};")
            pcs = cursor.fetchall()
            if pcs:
                message = "Error!\n\n"
                for pc in pcs:
                    message += f"There is already a record with the given data. With a model number: {pc[0]} and a price of: {pc[3]} dollars\n"
                messagebox.showinfo("Results", message)
            else:
                cursor.execute(f"SELECT modelo FROM Producto WHERE modelo = '{modelo}';")
                result = cursor.fetchone()
                if result:
                    messagebox.showerror("Error", "Model already exists.")
                else:
                    cursor.execute(f"SELECT fabricante FROM Producto WHERE fabricante = '{fabricante}';")
                    result = cursor.fetchone()
                    if not result:
                        cursor.execute(f"INSERT INTO Producto (fabricante, modelo, tipo) VALUES ('{fabricante}', '{modelo}', 'PC');")
                        cursor.execute(f"INSERT INTO PC (modelo, velocidad, ram, disco, precio) VALUES ('{modelo}', {velocidad}, {ram}, {disco}, {precio});")
                        self.conn.commit()
                        messagebox.showinfo("Results", "New PC added to database.")
        except Exception as e:
            messagebox.showerror("Error", f"Error finding or adding PC: {str(e)}")
        finally:
            cursor.close()

root = Tk()
app = PCsSystem(parent=None, master=root)
app.mainloop()