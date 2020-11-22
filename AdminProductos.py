import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

ventana_login = Tk()
ventana_login.title ("Seguridad - Acceso")
ventana_login.geometry ("300x230")
ventana_login.resizable(0, 0)
color='SpringGreen2'   
ventana_login['bg']=color

usuario_label = Label(ventana_login, text = "Usuario:")
usuario_label.grid(row=1, column=0, pady=5)
usuario_label.config(fg="#1D1F21", font=("Arial", 10, "bold"))
usuario_entry = Entry(ventana_login)
usuario_entry.grid(row=2, column=0, padx=85)

contraseña_label = Label(ventana_login, text = "Contraseña:")
contraseña_label.grid(row=3, column=0, padx=85, pady=5)
contraseña_label.config(fg="#1D1F21", font=("Arial", 10, "bold"))
contraseña_entry = Entry(ventana_login, show = "*")
contraseña_entry.grid(row=4, column=0, padx=85)

def login():
    # Conneccion a la base de datos
    connection = sqlite3.connect('Productos.db')
    c = connection.cursor()

    usuario = usuario_entry.get()
    contr = contraseña_entry.get()
    
    c.execute('SELECT * FROM usuario WHERE Nombre = ? AND Contraseña = ?', (usuario, contr))

    if c.fetchall():
        c.close()
        ventana_login.destroy()

        class Articulos:
            
            def abrirBD(self):
                conexion=sqlite3.connect("Productos.db")
                return conexion

            def alta(self, datos):
                cone=self.abrirBD()
                cursor=cone.cursor()
                sql="INSERT INTO Producto(Cod_Producto, Nombre, Precio, Descripcion, Categoria) VALUES (?,?,?,?,?)"
                cursor.execute(sql, datos)
                cone.commit()
                cone.close()

            def modifica(self, datos):
                try:
                    cone=self.abrirBD()
                    cursor=cone.cursor()
                    sql="UPDATE Producto SET Nombre = ?, Precio = ?, Descripcion = ?, Categoria = ? WHERE Cod_Producto = ?"
                    cursor.execute(sql, datos)
                    cone.commit()
                    return cursor.rowcount
                except:
                    cone.close()

            def baja(self, datos):
                try:
                    cone=self.abrirBD()
                    cursor=cone.cursor()
                    sql="DELETE FROM Producto WHERE Cod_Producto = ?"
                    cursor.execute(sql, datos)
                    cone.commit()
                    return cursor.rowcount
                except:
                    cone.close()

            def consulta(self, datos):
                try:
                    cone=self.abrirBD()
                    cursor=cone.cursor()
                    sql="SELECT Nombre, Precio, Descripcion, Categoria FROM Producto WHERE Cod_Producto = ?"
                    cursor.execute(sql, datos)
                    return cursor.fetchall()
                finally:
                    cone.close()

     #---------------------------------------------------------------------------------------------------

     # Creación de la base de datos en SQLite3
        try:
            with sqlite3.connect("Productos.db") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS Producto (Cod_Producto INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Precio INTEGER NOT NULL, Descripcion TEXT, Categoria TEXT);")
                c.execute("CREATE TABLE IF NOT EXISTS Venta (ID_Venta INTEGER PRIMARY KEY, Total_Venta INTEGER NOT NULL, Cod_Producto INTEGER NOT NULL, Fecha_Venta DATE, FOREIGN KEY (Cod_Producto) REFERENCES Producto(Cod_Producto));")
        except Error as e:
            print(e)

     #---------------------------------------------------------------------------------------------------

        # Definir ventana
        ventana = Tk()
        articulo1 = Articulos()
        ventana.minsize(500, 500)
        ventana.title("Proyecto Tkinter | PIA")
        ventana.resizable(0, 0)

     #---------------------------------------------------------------------------------------------------

     # Aviso para salir de la aplicación
        def salir():
            resultado = MessageBox.askquestion("Salir", "¿Seguro que quieres cerrar sesión?")
            if resultado == "yes":
                ventana.destroy()

     #---------------------------------------------------------------------------------------------------

    # Pantallas creadas para navegar
        def home():
            home_label.config(
                fg="white",
                bg="black",
                font=("Arial", 30),
                padx=130,
                pady=20
            )
            home_label.grid(row=0, column=0)

         # Pocisionamiento y Estilo del formulario
            home_frame.grid(row=1)

            boton_add.grid(row=1, column=0, padx=15, pady=30, sticky=NW)
            boton_update.grid(row=1, column=1, padx=15, pady=30, sticky=NE)
            boton_delete.grid(row=2, column=0, padx=15, pady=30, sticky=SW)
            boton_select.grid(row=2, column=1, padx=15, pady=30, sticky=SE)
            home_separator.grid(row=3, column=0)
            home_separator2.grid(row=3, column=1)
            boton_ventas.grid(row=4, column=0, padx=15, pady=30, sticky=SW)
            boton_listar.grid(row=4, column=1, padx=15, pady=30, sticky=SE)
            barra_status.grid(row=5, column=0, ipadx=8, ipady=8)

            boton_add.config(bg="#00C851", fg="white", font=("Arial", 14, "bold"), bd=5,)
            boton_update.config(bg="#FFBB33", fg="white", font=("Arial", 14, "bold"), bd=5,)
            boton_delete.config(bg="#FF4444", fg="white", font=("Arial", 14, "bold"), bd=5,)
            boton_select.config(bg="#33B5E5", fg="white", font=("Arial", 14, "bold"), bd=5,)
            boton_ventas.config(bg="#7030A0", fg="white", font=("Arial", 14, "bold"), bd=5,)
            boton_listar.config(bg="#FFFF00", font=("Arial", 14, "bold"), bd=5,)
            home_separator.config(font=("Arial", 14))
            home_separator2.config(font=("Arial", 14))
            barra_status.config(bg="black", fg="white", font=("Arial", 10, "bold"), borderwidth=5)

         # Ocultar otras pantallas
            add_label.grid_remove()
            add_frame.grid_remove()
            update_label.grid_remove()
            update_frame.grid_remove()
            delete_label.grid_remove()
            delete_frame.grid_remove()
            select_label.grid_remove()
            select_frame.grid_remove()
            ventas_label.grid_remove()
            ventas_frame.grid_remove()
            regresar.grid_remove()
            return True

        def add():
            add_label.config(
                fg="white",
                bg="black",
                font=("Arial", 30),
                padx=100,
                pady=20
            )
            add_label.grid(row=0, column=0, columnspan=10)

         # Pocisionamiento y Estilo del formulario
            add_frame.grid(row=1)

            add_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            add_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            add_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            add_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            add_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            add_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            add_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            add_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            add_description_entry.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

            add_category.place(x=50, y=250)

            guardar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            guardar.config(padx=15, pady=5, bg="#00C851", fg="white", font=("Arial", 10, "bold"))
         
            regresar.grid(row=7, column=0, padx=5, pady=30, sticky=SW)
            regresar.config(padx=15, pady=5, bg="#E552D9", fg="white", font=("Arial", 10, "bold"))

         # Ocultar otras pantallas
            home_label.grid_remove()
            home_frame.grid_remove()
            update_label.grid_remove()
            update_frame.grid_remove()
            delete_label.grid_remove()
            delete_frame.grid_remove()
            select_label.grid_remove()
            select_frame.grid_remove()
            ventas_label.grid_remove()
            ventas_frame.grid_remove()
            return True

        def update():
            update_label.config(
                fg="white",
                bg="black",
                font=("Arial", 30),
                padx=150,
                pady=20
            )
            update_label.grid(row=0, column=0)

         # Pocisionamiento y Estilo del formulario
            update_frame.grid(row=1)

            update_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            update_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            update_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            update_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            update_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            update_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            update_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            update_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            update_description_entry.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

            update_category.place(x=50, y=250)

            actualizar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            actualizar.config(padx=15, pady=5, bg="#FFBB33", fg="white", font=("Arial", 10, "bold"))
         
            regresar.grid(row=7, column=0, padx=5, pady=30, sticky=SW)
            regresar.config(padx=15, pady=5, bg="#E552D9", fg="white", font=("Arial", 10, "bold"))

         # Ocultar otras pantallas
            home_label.grid_remove()
            home_frame.grid_remove()
            add_label.grid_remove()
            add_frame.grid_remove()
            delete_label.grid_remove()
            delete_frame.grid_remove()
            select_label.grid_remove()
            select_frame.grid_remove()
            ventas_label.grid_remove()
            ventas_frame.grid_remove()
            return True

        def delete():
            delete_label.config(
                fg="white",
                bg="black",
                font=("Arial", 30),
                padx=150,
                pady=20
            )
            delete_label.grid(row=0, column=0)

         # Pocisionamiento y Estilo del formulario
            delete_frame.grid(row=1)

            delete_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            delete_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            eliminar.grid(row=2, column=1, padx=5, pady=30, sticky=E)
            eliminar.config(padx=15, pady=5, bg="#FF4444", fg="white", font=("Arial", 10, "bold"))
         
            regresar.grid(row=7, column=0, padx=5, pady=30, sticky=SW)
            regresar.config(padx=15, pady=5, bg="#E552D9", fg="white", font=("Arial", 10, "bold"))

            # Ocultar otras pantallas
            home_label.grid_remove()
            home_frame.grid_remove()
            add_label.grid_remove()
            add_frame.grid_remove()
            update_label.grid_remove()
            update_frame.grid_remove()
            select_label.grid_remove()
            select_frame.grid_remove()
            select_frame.grid_remove()
            ventas_label.grid_remove()
            ventas_frame.grid_remove()
            return True

        def select():
            select_label.config(
                fg="white",
                bg="black",
                font=("Arial", 30),
                padx=150,
                pady=20
            )
            select_label.grid(row=0, column=0)

            # Pocisionamiento y Estilo del formulario
            select_frame.grid(row=1)

            select_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            select_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            select_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            select_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            select_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            select_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            select_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            select_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
         

            select_category.place(x=50, y=250)

            consultar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            consultar.config(padx=15, pady=5, bg="#33B5E5", fg="white", font=("Arial", 10, "bold"))
             
            regresar.grid(row=7, column=0, padx=5, pady=30, sticky=SW)
            regresar.config(padx=15, pady=5, bg="#E552D9", fg="white", font=("Arial", 10, "bold"))

            # Ocultar otras pantallas
            home_label.grid_remove()
            home_frame.grid_remove()
            add_label.grid_remove()
            add_frame.grid_remove()
            update_label.grid_remove()
            update_frame.grid_remove()
            delete_label.grid_remove()
            delete_frame.grid_remove()
            ventas_label.grid_remove()
            ventas_frame.grid_remove()
            return True

        def ventass():
            ventas_label.config(
                fg="white",
                bg="black",
                font=("Arial", 30),
                padx=150,
                pady=20
            )
            ventas_label.grid(row=0, column=0)
         
            # Pocisionamiento y Estilo del formulario
            ventas_frame.grid(row=1)
         
            ventas_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            ventas_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
         
            ventas_total_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            ventas_total_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
         
            ventas_product_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            ventas_product_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
         
            ventas_fecha_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
            ventas_fecha_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
         
            ventas.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            ventas.config(padx=15, pady=5, bg="#7030A0", fg="white", font=("Arial", 10, "bold"))
         
            regresar.grid(row=7, column=0, padx=5, pady=30, sticky=SW)
            regresar.config(padx=15, pady=5, bg="#E552D9", fg="white", font=("Arial", 10, "bold"))

            # Ocultar otras pantallas
            home_label.grid_remove()
            home_frame.grid_remove()
            add_label.grid_remove()
            add_frame.grid_remove()
            update_label.grid_remove()
            update_frame.grid_remove()
            delete_label.grid_remove()
            delete_frame.grid_remove()
            select_label.grid_remove()
            select_frame.grid_remove()
            return True

        def ListaProductos():
            ventana_lista = Tk()
            ventana_lista.title ("Lista de información")
            ventana_lista.geometry ("800x580")
            ventana_lista.resizable(0, 0)
         
         
            def fetch_data():
                con = sqlite3.connect("Productos.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM producto")
                rows = cur.fetchall()
                if len(rows)!=0:
                    Menu_table.delete(*Menu_table.get_children())
                    for row in rows:
                        Menu_table.insert('',END,values=row)
                    con.commit()
                con.close()

         
            Detail_Frame=Frame(ventana_lista,bd=4,relief=RIDGE, bg="cyan")
            Detail_Frame.place(x=60,y=30,width=710,height=480)

            #Mostramos una tabla donde se mostraran los registros
            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="crimson")
            Table_Frame.place(x=10,y=70,width=660,height=400)
            
            #Es un desplazador que nos ayudara a mostrar los registros que la tabla no visiualice
            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
            #Mostramos el nombre de los datos en la tabla de los registros
            Menu_table=ttk.Treeview(Table_Frame,columns=("codigo","nombre", "precio", "descripcion", "categoria"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=Menu_table.xview)
            scroll_y.config(command=Menu_table.yview)
            
            #Llamamos a los datos registrados y los mostramos en la tabla
            Menu_table.heading("codigo", text="Codigo")
            Menu_table.heading("nombre", text="Nombre")
            Menu_table.heading("precio", text="Precio")
            Menu_table.heading("descripcion", text="Descripcion")
            Menu_table.heading("categoria", text="Categoria")
    
            Menu_table['show']= 'headings'
             
            #Mostramos los encabezados en la tabla de registro
            Menu_table.column("codigo", width=90)
            Menu_table.column("nombre", width=90)
            Menu_table.column("precio", width=90)
            Menu_table.column("descripcion", width=90)
            Menu_table.column("categoria", width=90)

            Menu_table.pack(fill=BOTH,expand=1)

            fetch_data()
         
         
     #---------------------------------------------------------------------------------------------------

        # Funciones para el manejo de productos que mandan llamar una funcion del archivo articulos.py
        def add_product():
            try:
                datos = (id_data.get(), name_data.get(), price_data.get(), add_description_entry.get("1.0", "end-1c"), add_category.get())
                if id_data.get() == "" or name_data.get() == "" or price_data.get() == "" or add_description_entry.get("1.0", "end-1c") == "" or add_category.get() == "Categoria":
                    MessageBox.showwarning("Alerta", "Rellene el formulario completo.")
                else:
                    articulo1.alta(datos)
                    MessageBox.showinfo("Información", "Los datos fueron cargados")
                    id_data.set("")
                    name_data.set("")
                    price_data.set("")
                    add_description_entry.delete("1.0", END)
                    add_category.set("Categoria")

                    app_status.set("¡Has agregado un producto correctamente!")
                    
            except Error as e:
                print(e)

        def update_product():
            if usuario == "Admin":
                datos = (id_data.get(), name_data.get(), price_data.get(), update_description_entry.get("1.0", "end-1c"), update_category.get())
                if id_data.get() == "" or name_data.get() == "" or price_data.get() == "" or update_description_entry.get("1.0", "end-1c") == "" or update_category.get() == "Categoria":
                    MessageBox.showwarning("Alerta", "Rellene el formulario completo.")
                else:
                    datos = (name_data.get(), price_data.get(), update_description_entry.get("1.0", "end-1c"), category_data.get(), id_data.get())
                    cantidad = articulo1.modifica(datos)
                    if cantidad == 1:
                        app_status.set("¡Acabas de modificar el producto correctamente!")
                        MessageBox.showinfo("Información", "Se modificó el producto con dicho código")
                    else:
                        app_status.set("No existe ese producto en la base de datos.")
                        MessageBox.showinfo("Información", "No existe un producto con dicho código")
            else:
                app_status.set("No tienes permitido realizar esta acción.")
                MessageBox.showinfo("Información", "No tienes los permisos suficientes")


        def delete_product():
            if usuario == "Admin":
                datos = (id_data.get(), )
                if id_data.get() == "":
                    MessageBox.showwarning("Alerta", "Rellene el formulario completo.")
                else:
                    cantidad = articulo1.baja(datos)
                    if cantidad == 1:
                        app_status.set("¡Acabas de eliminar el producto correctamente!")
                        MessageBox.showinfo("Información", "Se eliminó el producto con dicho código")
                    else:
                        app_status.set("No existe ese producto en la base de datos.")
                        MessageBox.showinfo("Información", "No existe un producto con dicho código")
            else:
                app_status.set("No tienes permitido realizar esta acción.")
                MessageBox.showinfo("Información", "No tienes los permisos suficientes")

        def query_product():
            datos = (id_data.get(), )
            respuesta = articulo1.consulta(datos)
            if len(respuesta)>0:
                name_data.set(respuesta[0][0])
                price_data.set(respuesta[0][1])
                description_data.set(respuesta[0][2])
                category_data.set(respuesta[0][3])
                app_status.set("Mostrando datos del producto...")
            else:
                name_data.set("")
                price_data.set("")
                category_data.set("Categoria")
                app_status.set("No existe ese producto en la base de datos.")
                MessageBox.showinfo("Información", "No existe un producto con dicho código")

     #---------------------------------------------------------------------------------------------------

        # Variables importantes!
        id_data = StringVar()
        name_data = StringVar()
        price_data = StringVar()
        description_data = StringVar()
        category_data = StringVar()
        app_status = StringVar()

     #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (INICIO)
        home_frame = Frame(ventana)

        home_label = Label(ventana, text="Menú Principal")
        boton_add = Button(home_frame, text="¡Añadir Productos!", command=add)
        boton_update = Button(home_frame, text="¡Actualizar Productos!", command=update)
        boton_delete = Button(home_frame, text="¡Eliminar Productos!", command=delete)
        boton_select = Button(home_frame, text="¡Consultar Productos!", command=select)
        boton_ventas = Button(home_frame, text="¡Registrar Venta!", command=ventass)
        boton_listar = Button(home_frame, text="Listar Productos", command=ListaProductos)
        home_separator = Label(home_frame, text="-------------------------------------")
        home_separator2 = Label(home_frame, text="-------------------------------------")

        barra_status = Label(ventana, textvariable=app_status)
        app_status.set(f"Estado de la aplicación: -- Bienvenido {usuario} --")

     #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (AÑADIR)
        add_label = Label(ventana, text="Añadir productos")

        # Campos del formulario (AÑADIR)
        add_frame = Frame(ventana)

        add_id_label = Label(add_frame, text="Clave del producto: ")
        add_id_entry = Entry(add_frame, textvariable=id_data)

        add_name_label = Label(add_frame, text="Nombre: ")
        add_name_entry = Entry(add_frame, textvariable=name_data)

        add_price_label = Label(add_frame, text="Precio: ")
        add_price_entry = Entry(add_frame, textvariable=price_data)

        add_description_label = Label(add_frame, text="Descripción: ")
        add_description_entry = Text(add_frame)

        add_category = ttk.Combobox(add_frame)
        add_category.set("Categoria")
        add_category['values'] = ('Electronica', 'Comida', 'Limpieza', 'Ropa', 'Decoración')
        add_category.current()

        guardar = Button(add_frame, text="Guardar", command=add_product)

     #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (ACTUALIZAR)
        update_label = Label(ventana, text="Actualizar producto")

        # Campos del formulario (ACTUALIZAR)
        update_frame = Frame(ventana)

        update_id_label = Label(update_frame, text="Clave del producto: ")
        update_id_entry = Entry(update_frame, textvariable=id_data)

        update_name_label = Label(update_frame, text="Nombre: ")
        update_name_entry = Entry(update_frame, textvariable=name_data)

        update_price_label = Label(update_frame, text="Precio: ")
        update_price_entry = Entry(update_frame, textvariable=price_data)

        update_description_label = Label(update_frame, text="Descripción: ")
        update_description_entry = Text(update_frame)

        update_category = ttk.Combobox(update_frame, textvariable=category_data)
        update_category.set("Categoria")
        update_category['values'] = ('Electronica', 'Comida', 'Limpieza', 'Ropa', 'Decoración')
        update_category.current()

        actualizar = Button(update_frame, text="Actualizar", command=update_product)

     #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (ELIMINAR)
        delete_label = Label(ventana, text="Eliminar producto")

        # Campos del formulario (ELIMINAR)
        delete_frame = Frame(ventana)

        delete_id_label = Label(delete_frame, text="Clave del producto: ")
        delete_id_entry = Entry(delete_frame, textvariable=id_data)

        eliminar = Button(delete_frame, text="Eliminar", command=delete_product)

     #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (CONSULTAR)
        select_label = Label(ventana, text="Consultar productos")

        # Campos del formulario (CONSULTAR)
        select_frame = Frame(ventana)

        select_id_label = Label(select_frame, text="Clave del producto: ")
        select_id_entry = Entry(select_frame, textvariable=id_data)

        select_name_label = Label(select_frame, text="Nombre: ")
        select_name_entry = Entry(select_frame, textvariable=name_data)

        select_price_label = Label(select_frame, text="Precio: ")
        select_price_entry = Entry(select_frame, textvariable=price_data)

        select_description_label = Label(select_frame, text="Descripción: ")
        select_description_entry = Entry(select_frame, textvariable=description_data)

        select_category = ttk.Combobox(select_frame, textvariable=category_data)
        select_category.set("Categoria")
        select_category['values'] = ('Electronica', 'Comida', 'Limpieza', 'Ropa', 'Decoración')
        select_category.current()

        consultar = Button(select_frame, text="Consultar", command=query_product)

     #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (VENTAS)
        ventas_label = Label(ventana, text="Registrar Venta")
         
        # Campos del formulario (VENTAS)
        ventas_frame = Frame(ventana)
         
        ventas_id_label = Label(ventas_frame, text="Clave de la Venta: ")
        ventas_id_entry = Entry(ventas_frame)
         
        ventas_total_label = Label(ventas_frame, text="Total: ")
        ventas_total_entry = Entry(ventas_frame)
         
        ventas_product_label = Label(ventas_frame, text="Producto(Clave): ")
        ventas_product_entry = Entry(ventas_frame)
         
        ventas_fecha_label = Label(ventas_frame, text="Fecha (YYYY-MM-DD): ")
        ventas_fecha_entry = Entry(ventas_frame)
         
        ventas = Button(ventas_frame, text="Registrar Venta")
     
     #---------------------------------------------------------------------------------------------------
     
        # Boton regresar al menú
         
        regresar = Button(ventana, text="Regresar", command=home)
     
     #---------------------------------------------------------------------------------------------------

        # Menú superior
        menu_superior = Menu(ventana)
        menu_superior.add_command(label="Inicio", command=home)
        menu_superior.add_command(label="Añadir", command=add)
        menu_superior.add_command(label="Actualizar", command=update)
        menu_superior.add_command(label="Eliminar", command=delete)
        menu_superior.add_command(label="Consultar", command=select)
        menu_superior.add_command(label="Ventas", command=ventass)
        menu_superior.add_command(label="Cerrar sesión", command=lambda: salir())

        # Cargar la pantalla Inicio
        home()

        # Cargar Menú
        ventana.config(menu=menu_superior)

        # Cargar ventana
        ventana.mainloop()

    else:
        MessageBox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")

def Registro():
    ventana_registro = Tk()
    ventana_registro.minsize(300, 260)
    ventana_registro.resizable(0, 0)
    ventana_registro.title("Registro de Usuario")
    ventana_registro['bg']="cyan"
    
    Label(ventana_registro,text="Clave de seguridad : ",bg=color,font=("Arial Black",10)).pack()     
    caja3=Entry(ventana_registro,show="*")                                                        
    caja3.pack()
    Label(ventana_registro,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()     
    caja4=Entry(ventana_registro)                                                        
    caja4.pack()
    Label(ventana_registro,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()  
    caja5=Entry(ventana_registro,show="*")                                                
    caja5.pack()    
    Label(ventana_registro,text="Verifique Contraseña : ",bg=color,font=("Arial Black",10)).pack()    
    caja6=Entry(ventana_registro,show="*")                                                            
    caja6.pack()
    def registro():
        # Conneccion a la base de datos
        connection = sqlite3.connect('Productos.db')
        c = connection.cursor()
        
        Seguridad=caja3.get()
        Usr_reg=caja4.get()    
        Contra_reg=caja5.get()  
        Contra_reg_2=caja6.get()
        
        if Usr_reg == "" or Contra_reg == "" or Contra_reg_2 == "":
            MessageBox.showwarning(title="Campos Vacios",message="Rellene el formulario completo.")
        else:
            if Seguridad == "123":
                if(Contra_reg==Contra_reg_2):       
                    c.execute("INSERT INTO usuario values(\'"+Usr_reg+"\',\'"+Contra_reg+"')")
                    connection.commit()         
                    MessageBox.showinfo(title="Registro Correcto",message="Hola, "+Usr_reg+" \nSu registro fue exitoso.")
                    ventana_registro.destroy()        
                else:
                    MessageBox.showwarning(title="Contraseña Incorrecta",message="Error \nLas contraseñas no coinciden.")
            else:
                MessageBox.showerror(title="Acceso Denegado",message="La clave de seguridad es incorrecta. \n No tiene permiso de agregar un usuario.")
            
            
    buttons = Button(ventana_registro,text="Registrar",command=registro,bg='gray',font=("Arial Rounded MT Bold",10)).pack(side="bottom")

Acceder = Button(ventana_login, text="Acceder", bg="gold2", font=("Arial", 10, "bold"), command = login)
Acceder.grid(row=5, column=0, pady=20)

Registrar = Button(ventana_login,text="Crear una cuenta",bg='gray', font=("Arial Rounded MT Bold",10), command = Registro)
Registrar.grid(row=6, column=0, pady=5)

ventana_login.mainloop()