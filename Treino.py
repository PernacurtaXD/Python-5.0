import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


janela = ctk.CTk()
janela.geometry('600x500')
janela.title('Sistema de Consumo de Gasolina')
janela.iconbitmap('customkinter/gas.ico')
janela.resizable(False,False)

ctk.CTkLabel(janela,
             text = 'Consumo de Gasolina',
             front = ('cascadia mono', 40),
             text_color= ('snow').pack(pady = 27))


ctk.CTkLabel(janela,
             text = ('Distância percorrida:'),
             front = ('cascadia mono', 21),
             text_color= 'snow').pack(pady = 10)

distancia_km = ctk.CTkEntry(janela,
                            font = ('cascadia mono', 18),
                            placeholder_text= 'Digite a distância percorrida',
                            width= 340,
                            height= 30)

distancia_km.pack(pady = 10)

ctk.CTkLabel(janela,
             text= 'Consumo de combustível por km/l:',
             font= ('cascadia mono', 21),
             text_color= 'snow').pack(pady = 10)

consumo_kml = ctk.CTkEntry(janela,
                           font = ('cascadia mono', 21),
                           placeholder_text = 'Digite o consumo em km/l:',
                           width= 340,
                           height= 30)

consumo_kml.pack(pady = 10)

ctk.CTkLabel(janela,
             text= 'Preço do combustível:',
             font= ('cascadia mono', 21),
             text_color= 'snow').pack(pady = 10)

consumo_kml = ctk.CTkEntry(janela,
                           font = ('cascadia mono', 21),
                           placeholder_text = 'Digite o preço do combustível:',
                           width= 340,
                           height= 30)
             
consumo_kml.pack(pady = 5)


def calcular_consumo():
    distancia_km = float(distancia_km.get())
    consumo_kml = float(consumo_kml.get())
    precol = float(precol.get())
    consumototal = (distancia_km / consumo_kml) * precol
    resultado_label.configure(text = f'O custo total da viagem é de R${consumo_total:.2f}')

botao_calcular = ctk.CTkButton(janela,
                               text = 'Calcular',
                               font = ('cascadia mono', 18),
                               command= calcular_consumo
                               ) 

botao_calcular.pack(pady = 10)

resultado_label = ctk.CTkButton(janela,
                                text = 'Calcular',
                                font= ('cascadia mono', 16),
                                text_color= "snow" 
                                )

resultado_label.pack(pady = 10)

janela.mainloop()