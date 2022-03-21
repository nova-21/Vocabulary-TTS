# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from gtts import gTTS
import os
import threading
import time
import vlc
from mutagen.mp3 import MP3
import pandas as pd
import sys
from PyQt5 import QtGui

from main_ui import Ui_MainWindow




class languages_gui(QMainWindow,Ui_MainWindow):
        fila=0
        p = vlc.MediaPlayer("texto.mp3")
        stopThread=0

        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.loadCsv('words.csv')
            self.playAll.clicked.connect(self.corr2)
            self.playThis.clicked.connect(self.corr3)
            self.pushButton.clicked.connect(self.stopPlaying)

        def removeFiles(self):
            os.remove("texto.mp3")

        def stopper(self):
            global stop


        def stopPlaying(self):
            self.stopThread=1

        def corr2(self):
            th=threading.Thread(target=self.correr)
            try:
                th.start()
            except (KeyboardInterrupt, SystemExit):
                th.join()
                sys.exit()

        def corr3(self):
            th=threading.Thread(target=self.runSingle)
            try:
                th.start()
            except (KeyboardInterrupt, SystemExit):
                th.join()
                sys.exit()

        def loadCsv(self, fileName):
            with open(fileName, "r") as fileInput:
                for row in csv.reader(fileInput):
                    rowPosition = self.tabla.rowCount()
                    self.tabla.insertRow(rowPosition)
                    contador=0
                    for field in row:
                        self.tabla.setItem(rowPosition,contador, QTableWidgetItem(field))
                        contador=contador+1

        def runSingle(self):
            self.tabla.clearSelection()
            rowIndex=self.tabla.currentRow()
            print(rowIndex)
            if rowIndex < 0:
                return
            with open('words.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                df = pd.read_csv('words.csv',header=None)
                for i in [0, 1, 2, 3, 4]:
                    if self.stopThread == 1:
                        self.stopThread=0
                        self.removeFiles()
                        return
                    self.tabla.item(rowIndex, i).setBackground(QtGui.QColor(Qt.yellow))
                    self.tabla.viewport().update()
                    text = df.iat[rowIndex,i]

                    if i == 0:
                        language = 'en'
                    elif i == 1:
                        language = 'es'
                    elif i == 2:
                        language = 'pt'
                    elif i == 3:
                        language = 'it'
                    else:
                        language = 'fr'
                    speech = gTTS(text=text, lang=language, slow=True)
                    speech.save("texto.mp3")
                    audio = MP3("texto.mp3")
                    duration = audio.info.length
                    self.p.play()
                    time.sleep(duration)
                    self.p.stop()
                    self.tabla.item(rowIndex, i).setBackground(QtGui.QColor(255, 255, 255))
                    self.tabla.viewport().update()
            self.removeFiles()

        def closeEvent(self, event):
            self.removeFiles()
            self.stylusProximityControlOff()
            self.deleteLater()

        def correr(self):
            self.fila=0
            with open('words.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    for i in [0,1,2,3,4]:
                        if self.stopThread == 1:
                            self.stopThread = 0
                            self.removeFiles()
                            return
                        self.tabla.item(self.fila,i).setBackground(QtGui.QColor(Qt.yellow))
                        self.tabla.viewport().update()
                        text = row[i]
                        if i == 0:
                            language = 'en'
                        elif i == 1:
                            language = 'es'
                        elif i == 2:
                            language = 'pt'
                        elif i == 3:
                            language = 'it'
                        else:
                            language = 'fr'
                        speech = gTTS(text=text, lang=language, slow=True)
                        speech.save("texto.mp3")
                        audio = MP3("texto.mp3")
                        duration = audio.info.length
                        self.p.play()
                        time.sleep(duration)
                        self.p.stop()
                        self.tabla.item(self.fila, i).setBackground(QtGui.QColor(255, 255, 255))
                        self.tabla.viewport().update()
                    self.fila=self.fila+1
                    time.sleep(1)
            self.removeFiles()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI=languages_gui()
    GUI.show()
    sys.exit(app.exec_())







