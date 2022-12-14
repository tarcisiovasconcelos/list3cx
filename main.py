import PySimpleGUI as sg
import banco

#SQL DE CONSULTA PARA ENCONTRAR QUEM ESTÁ DEPRECIADO NO BANCO 
banco.cursor.execute(banco.sqlSelectALL)
row = banco.cursor.fetchall()
#Criei a lista de id de quem está no banco e no arquivo
listaBanco = [] 
for x in row:
    listaBanco.append([str(x[1]),str(x[2])])
print(listaBanco)

headings = ['Setor', 'Telefone']
data = listaBanco

layout = [
    [sg.Text("Digite Setor ou Telefone:")],
    [sg.Input(size=(40, 1), key='-INPUT-')],
    [sg.T('')],
    [sg.T('Contatos CESMAC')],
    [sg.Table(data, headings=headings, justification='left', key='-TABLE-', size=(30,20),expand_x=True,),],
]
window = sg.Window("Contatos CESMAC", layout, finalize=True,return_keyboard_events=True, size=(848,600))
table = window['-TABLE-']
entry = window['-INPUT-']
entry.bind('<Return>', 'RETURN-')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event != None:
        text = values['-INPUT-'].lower()
        erro = 0
        if text == '':
            table.update(data)
        if text != '': 
            new_data = []
            for row, row_data in enumerate(data):
                if text in row_data[0].lower() or text in row_data[1].lower():
                    new_data.append(row_data)
                
            print(new_data)
            if new_data != []:
                table.update(new_data)
            else:
                sg.popup('NOT FUNDO')



window.close()