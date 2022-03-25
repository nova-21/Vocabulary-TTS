# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import gtts.lang
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from gtts import gTTS
import os
import threading
import time
from mutagen.mp3 import MP3
import pandas as pd
import sys
from PyQt5 import QtGui
from pygame import mixer
from main_ui import Ui_MainWindow
import ctypes  # An included library with Python install.


class languages_gui(QMainWindow,Ui_MainWindow):
        fila=0
        stopThread=0
        lang=gtts.lang.tts_langs()
        listLocal=0
        key_list = list(lang.keys())
        val_list = list(lang.values())
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.loadCsv('words.csv')

            self.playAll.clicked.connect(self.managerAll)
            self.playThis.clicked.connect(self.managerOne)
            self.pushButton.clicked.connect(self.stopPlaying)
            self.getMp3.clicked.connect(self.managerGenerate)



        def removeFiles(self):
            os.remove("texto.mp3")

        def stopper(self):
            global stop


        def stopPlaying(self):
            self.stopThread=1

        def managerAll(self):
            th=threading.Thread(target=self.correr)
            try:
                th.start()
            except (KeyboardInterrupt, SystemExit):
                th.join()
                sys.exit()

        def managerOne(self):
            th=threading.Thread(target=self.runSingle)
            try:
                th.start()
            except (KeyboardInterrupt, SystemExit):
                th.join()
                sys.exit()

        def managerGenerate(self):
            th=threading.Thread(target=self.generateMP3)
            try:
                th.start()
            except (KeyboardInterrupt, SystemExit):
                th.join()
                sys.exit()

        def loadCsv(self, fileName):
            with open(fileName, "r") as fileInput:
                reader=csv.reader(fileInput)
                self.listLocal=next(reader)
                for row in reader:
                    rowPosition = self.tabla.rowCount()
                    self.tabla.insertRow(rowPosition)
                    contador=0
                    for field in row:
                        self.tabla.setItem(rowPosition,contador, QTableWidgetItem(field))
                        contador=contador+1

        def runSingle(self):
            self.tabla.clearSelection()
            rowIndex=self.tabla.currentRow()


            if rowIndex < 0:
                return
            df = pd.read_csv('words.csv', encoding='latin-1')
            df['French'] = df['French'].replace({'(inf)': ' '})
            nColumns = len(df.columns)
            for i in range(0, nColumns):
                if self.stopThread == 1:
                    self.stopThread = 0
                    self.removeFiles()
                    return
                self.tabla.item(rowIndex, i).setBackground(QtGui.QColor(Qt.yellow))
                self.tabla.viewport().update()
                text = df.iat[rowIndex, i]
                position = self.val_list.index(self.listLocal[i])
                valor= self.key_list[position]
                speech = gTTS(text=text, lang=valor, slow=True)
                speech.save("texto.mp3")
                audio = MP3("texto.mp3")
                duration = audio.info.length
                mixer.init()
                mixer.music.load("texto.mp3")
                mixer.music.play()
                time.sleep(duration)
                mixer.quit()
                self.tabla.item(rowIndex, i).setBackground(QtGui.QColor(255, 255, 255))
                self.tabla.viewport().update()

            self.removeFiles()

        def closeEvent(self, event):
            self.removeFiles()
            self.stylusProximityControlOff()
            self.deleteLater()

        def correr(self):
            self.fila=0
            df = pd.read_csv('words.csv', encoding='latin-1')
            for index, row in df.iterrows():
                nColumns = len(df.columns)
                for i in range(0, nColumns):
                    if self.stopThread == 1:
                        self.stopThread = 0
                        self.removeFiles()
                        return
                    self.tabla.item(self.fila, i).setBackground(QtGui.QColor(Qt.yellow))
                    self.tabla.viewport().update()
                    text = row[i]
                    position = self.val_list.index(self.listLocal[i])
                    valor = self.key_list[position]
                    speech = gTTS(text=text, lang=valor, slow=True)
                    speech.save("texto.mp3")
                    audio = MP3("texto.mp3")
                    duration = audio.info.length
                    mixer.init()
                    mixer.music.load("texto.mp3")
                    mixer.music.play()
                    time.sleep(duration)
                    mixer.quit()
                    self.tabla.item(self.fila, i).setBackground(QtGui.QColor(255, 255, 255))
                    self.tabla.viewport().update()
                self.fila = self.fila + 1
                time.sleep(0.5)
            self.removeFiles()

        def generateMP3(self):
            self.fila = 0
            df = pd.read_csv('words.csv', encoding='latin-1')
            leng=len(df)
            with open('finalArchive.mp3', 'wb') as ff:
                for index, row in df.iterrows():
                    nColumns = len(df.columns)
                    # Banderas para hilos
                    for i in range(0, nColumns):
                        if self.stopThread == 1:
                            self.stopThread = 0
                            self.removeFiles()
                            return
                        text = row[i]
                        position = self.val_list.index(self.listLocal[i])
                        valor = self.key_list[position]
                        speech = gTTS(text=text, lang=valor, slow=True)
                        speech.write_to_fp(ff)
                    self.fila = self.fila + 1
                    percentage = (index + 1) * 100 / leng
                    self.progressBar.setValue(int(percentage))

            ctypes.windll.user32.MessageBoxW(0, "MP3 created", "MP3 created", 0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI=languages_gui()
    GUI.show()
    sys.exit(app.exec_())







