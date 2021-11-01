from PyQt5 import uic,QtWidgets
import cryptocode

def criptografar():
    crip = pagina1.entrada.text()
    crip = cryptocode.encrypt(crip, 'wow')
    pagina1.entrada_2.setText(crip)
    
def descriptografar():
    descrip = pagina1.entrada.text()
    descrip = cryptocode.decrypt(descrip, "wow")
    pagina1.entrada_2.setText(descrip)

def limpeza():
    pagina1.entrada.setText("")
    pagina1.entrada_2.setText("")

app=QtWidgets.QApplication([])
pagina1=uic.loadUi("pagina1.ui")
pagina1.botao2.clicked.connect(criptografar)
pagina1.botao1.clicked.connect(descriptografar)
pagina1.botao3.clicked.connect(limpeza)

pagina1.show()
app.exec_()