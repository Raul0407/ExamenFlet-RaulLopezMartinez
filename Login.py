import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6

    dlg = ft.AlertDialog(title=ft.Text("La contraseña es correcta"))
    dlg2 = ft.AlertDialog(title=ft.Text("La contraseña no es correcta"))
    def funcionBoton(x):
        if tfnombre.value == tfpassword.value:
            page.dialog = dlg
            dlg.open = True
        else:
            page.dialog = dlg2
            dlg2.open = True
        page.update()

    #Fin --- Ejercicio 6



    #Ejercicio 2

    img = ft.Image(src="Logo.png")

    #Fin --- Ejercicio 2



    #Ejercicio 3

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Fin --- Ejercicio 3



    page.window_height=500
    page.window_width= 250
    tfnombre = ft.TextField(label="Nombre")



    #Ejercicio 4

    tfpassword = ft.TextField(label="Contraseña", can_reveal_password=True, password=True)

    #Fin --- Ejercicio 4



    #Ejercicio 5

    btnEntrar = ft.ElevatedButton("Entrar", icon="park_rounded", icon_color="green400", on_click=funcionBoton)

    #Fin-- Ejercicio 5



    page.add(img,tfnombre,tfpassword,btnEntrar, dlg, dlg2)
    


ft.app(target=main,assets_dir="fotos")