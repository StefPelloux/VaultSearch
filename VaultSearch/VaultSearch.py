import hvac
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon, QKeySequence
import MainWindows
import search



class Start(object):
    def __init__(self):
        self.ui = MainWindow(self)
        self.ui.show()




class MyQtApp(MainWindows.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.ui = MainWindows.Ui_MainWindow()
        self.ui.setupUi(self)
        self.showNormal()
        self.setWindowTitle("VaultSearch")
        AppIcon = QIcon("icon.png")
        self.setWindowIcon(AppIcon)
        self.openFile()
        self.shortcut = QtWidgets.QShortcut(QKeySequence("Ctrl+F"), self.ui.textEdit)
        self.shortcut.activated.connect(self.findtext)
        self._initSlotButtons()
        try:
            self.show()
        except Exception as E:
            print(E)

    def  openFile(self):
        self.filename = "c:\Temp\Vaulsearch.log"
        try:
            self.file = open(self.filename, "r")
            line = self.file.read()
            self.ui.lineurl.setText(line.split('\n', 1)[0])
            self.ui.linepath.setText(line.split('\n', 1)[1])
        except:
            line = ""


    def  saveFile(self):
        self.filename = "c:\Temp\Vaulsearh.log"
        self.file = open(self.filename, "w")
        line = self.ui.lineurl.text() + '\n' + self.ui.linepath.text()

        self.file.write(line)
        self.file.close()




    def syncronise(self):

        vault_url = self.ui.lineurl.text()
        token_git = self.ui.linetoken.text()
        rootpath = self.ui.linepath.text()

        self.saveFile()

        self.Listsecret = ""
        #print("Connexion to: ", vault_url)
        #client = hvac.Client()
        client = hvac.Client(url=vault_url)
        login_response = client.auth.github.login(token=token_git)
        ident = client.is_authenticated()
        if ident is False:
            print(ident)
            exit()

        self.list_secrets_res = list_secrets(client, rootpath)

        #for self.pathline in self.list_secrets_res[:]:
        #    self.Listsecret = self.Listsecret + str(self.pathline) + "\n"

        self.Listsecret = list_secret_value
        self.ui.textEdit.setText(self.Listsecret)

    def _initSlotButtons(self):
        self.ui.pushButton.clicked.connect(self.syncronise)

    def findtext(self):
         mysearch = Mysearch()
         if mysearch.exec_() == QtWidgets.QDialog.Accepted:
             if Mysearch.searchtext != "":
                 if not self.ui.textEdit.find(Mysearch.searchtext):
                     cursor = self.ui.textEdit.textCursor()
                     cursor.setPosition(0)
                     self.ui.textEdit.setTextCursor(cursor)
                     self.ui.textEdit.find(Mysearch.searchtext)



###########

class Mysearch(search.Ui_Search, QtWidgets.QDialog):
    def __init__(self):
        super(Mysearch, self).__init__()
        self.ui = search.Ui_Search()
        self.ui.setupUi(self)
        self.setWindowTitle("Search")
        self.showNormal()
        self._LogininitSlotButtons()

    def _LogininitSlotButtons(self):
        self.ui.buttonBox.accepted.connect(self.buttonBox)


    def buttonBox(self):
        Mysearch.searchtext = self.ui.searchtext.text()





##############

def read_list_secretpath(client, source_mount):
    return client.secrets.kv.v1.list_secrets(path=source_mount)['data']['keys']


def read_secret_entry(client, path_secret):
    return client.secrets.kv.v1.read_secret(path_secret)['data']


def list_secrets(client, source_mount):
    # Cree la liste contenant les paths de la premiere lecture du rootpath
    # ex: Donner le folder de debut. retourne les sous folders (VM,SAN..)
    list_entry = read_list_secretpath(client, source_mount)

    # pour chaque sous folder on creer une entree dans la root liste.
    for nbelem, newpathentry in enumerate(list_entry):
        list_entry[nbelem] = (source_mount + newpathentry)

    # une fois la struture cree on list ce qu'il ya dessous.
    final_list = build_newpath(client, list_entry)
    return


def build_newpath(client, list_secret_path):
    global list_secret_value
    list_secret_value = ""
    # lecture recursive de la structure.

    upd = 0
    for pathread in list_secret_path[:]:
        if pathread[-1] == '/':
            append_list = read_list_secretpath(client, pathread)
            for newpath in append_list:
                list_secret_path.append(pathread + newpath)
            list_secret_path.remove(pathread)
            upd = 1
    if upd == 1:
        build_newpath(client, list_secret_path)
    else:
        for secret in list_secret_path[:]:
            secret_value = str(read_secret_entry(client, secret))
            value_to_save = str(secret), str(secret_value)
            list_secret_value = str(list_secret_value) + str(value_to_save) + "\n"
    return list_secret_value



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    #app.setQuitOnLastWindowClosed(False)
    vaultapp = MyQtApp()
    vaultapp.show()
    app.exec_()










