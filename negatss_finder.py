# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:53:13 2019

@author: moimo
"""

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import time
#import re
#
#
#
#driver = webdriver.Chrome('C:/chromedriver',desired_capabilities={'javascriptEnabled': True})
#driver.get("https://birse.borgia-app.com/")
#
#elem =driver.find_element_by_name("username")
#elem.send_keys("106Li218")
#
#elem =driver.find_element_by_name("password")
#elem.send_keys("Redhawk's2018")
#elem.send_keys(Keys.RETURN)
#
#print("connexion réussie")
#
#
##
#driver.get("https://birse.borgia-app.com/users/")
#
#l_posits = driver.find_elements_by_class_name("success")
#
#posits_raw = [elem.text for elem in l_posits]
##print(posits_raw)
#
##"25Li218 jackowiak julien InfinityGnè'∫∫ 25 LI 2018 0,07€ Détail".split(' ')[-2]
##Out[8]: '0,07€'
#posits_raw = [elem.split(' ')[-2] for elem in posits_raw]
##posits_raw_extracted = []
##for elem in posits_raw:
##    if elem.split(' ')[0] == 'AE_ENSAM':
##        picsou_account = elem.split(' ')[-2]
##        picsou_account = float(picsou_account[:-1].replace(',', '.'))
##        print("picous_account", picsou_account)
##    else:
##        posits_raw_extracted += [ elem.split(' ')[-2] ]
#
##float('0,07€'[:-1].replace(',', '.'))
##0.07
#posits_raw_extracted = [float(elem[:-1].replace(',', '.')) for elem in posits_raw]
##print(posits_raw)
#print(sum(posits_raw_extracted))
#
#
#
#l_negats = driver.find_elements_by_class_name("danger")
#negats_raw = [elem.text for elem in l_negats]
#negats_raw = [elem.split(' ')[-2] for elem in negats_raw]
#negats_raw = [float(elem[:-1].replace(',', '.')) for elem in negats_raw]
##print(negats_raw)
#print(sum(negats_raw))

import sys
import os

from configparser import ConfigParser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from menu import Ui_MainWindow

import sys
import requests
from multiprocessing import Queue
from bs4 import BeautifulSoup

# sets the path to the certificate file
if getattr(sys, "frozen", False):
# if frozen, get embeded file
    cacert = os.path.join(os.path.dirname(sys.executable), "cacert.pem")
else:
# else just get the default file
    cacert = requests.certs.where()


def get_creditentials():
    parser = ConfigParser()
    parser.read("config.cfg")

    user = parser["SETTINGS"]["user"]
    pwd = parser["SETTINGS"]["pwd"]
    return user, pwd

class CloneThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.git_url = ""

    # run method gets called when we start the thread
    def run(self):
        #import sys
        #import requests
        
        URL = 'https://birse.borgia-app.com/'
        client = requests.session()
        
        # Retrieve the CSRF token first
        client.get(URL)  # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']
        
        user, pwd = get_creditentials()
        login_data = dict(username=user, password=pwd, csrfmiddlewaretoken=csrftoken, next='/')
        r = client.post(URL, data=login_data, headers=dict(Referer=URL), verify=cacert)
        
        
        r = client.get('https://birse.borgia-app.com/users/', verify=cacert)
        
        #from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, 'html.parser')
        
        l_posits = []
        l_negats = []
        for elem in soup.find_all('td'):
            #print(elem.text)
            if elem.text != '' and elem.text[-1] == '€':
                nombre = float(elem.text[:-1].replace(',', '.'))
                if nombre >= 0:
                    l_posits.append(nombre)
                elif nombre < 0:
                    l_negats.append(nombre)
        print(sum(l_posits), sum(l_negats))
        total_positss = sum(l_posits)
        total_negats = sum(l_negats)
        
        self.signal.emit([total_positss, total_negats])

class Ecran_menuPrincipal(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # Configure l'interface utilisateur.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Negat'ss finder")
        #self.setWindowIcon(QtGui.QIcon("res/icone vaisseau.png"))

        #self.ui.UI_BUTTON_FIND.clicked.connect(self.find_negatss)
        self.ui.UI_BUTTON_FIND.clicked.connect(self.get_thread)
        
        self.get_thread = CloneThread()  # This is the thread object
        # Connect the signal from the thread to the finished method
        self.get_thread.signal.connect(self.finished)
        
        self.statusBar().showMessage('Ready')  #érit ready en bas à gauche

        #self.find_negatss()
        
    def finished(self, result):
        print(result)
        print(type(result))
        #[1164.7000000000007, -8481.380000000005]
        total_posits, total_negats = result
        #here change text value
        self.ui.UI_TEXT_POSITS.setText(str(total_posits))
        self.ui.UI_TEXT_NEGATS.setText(str(total_negats))
        self.ui.UI_TEXT_TOTAL.setText(str(total_posits + total_negats))
        self.statusBar().showMessage('Fini')

        #self.textEdit.setText("Cloned at {0}".format(result))  # Show the output to the user
        #self.pushButton.setEnabled(True)  # Enable the pushButton
        
    def get_thread(self):
        self.statusBar().showMessage("Recherche en cours... ~10s d'attente")
        self.get_thread.start()  # Finally starts the thread
        
    """def find_negatss(self):
        #QtWidgets.qApp.processEvents()
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        #import time
        #import re
        
        
        
        driver = webdriver.Chrome('C:/chromedriver',desired_capabilities={'javascriptEnabled': True})
        driver.get("https://birse.borgia-app.com/")
        
        elem =driver.find_element_by_name("username")
        elem.send_keys("106Li218")
        
        elem =driver.find_element_by_name("password")
        elem.send_keys("Redhawk's2018")
        elem.send_keys(Keys.RETURN)
        
        print("connexion réussie")
        self.statusBar().showMessage('Connexion réussie')
        
        
        #
        driver.get("https://birse.borgia-app.com/users/")
        
        self.statusBar().showMessage('Recherche positss')
        l_posits = driver.find_elements_by_class_name("success")
        
        self.statusBar().showMessage('Traitement positss')
        posits_raw = [elem.text for elem in l_posits]
        #print(posits_raw)
        
        #"25Li218 jackowiak julien InfinityGnè'∫∫ 25 LI 2018 0,07€ Détail".split(' ')[-2]
        #Out[8]: '0,07€'
        posits_raw = [elem.split(' ')[-2] for elem in posits_raw]
        #posits_raw_extracted = []
        #for elem in posits_raw:
        #    if elem.split(' ')[0] == 'AE_ENSAM':
        #        picsou_account = elem.split(' ')[-2]
        #        picsou_account = float(picsou_account[:-1].replace(',', '.'))
        #        print("picous_account", picsou_account)
        #    else:
        #        posits_raw_extracted += [ elem.split(' ')[-2] ]
        
        #float('0,07€'[:-1].replace(',', '.'))
        #0.07
        posits_raw_extracted = [float(elem[:-1].replace(',', '.')) for elem in posits_raw]
        #print(posits_raw)
        total_positss = sum(posits_raw_extracted)
        print(total_positss)
        self.ui.UI_TEXT_POSITS.setText(str(total_positss))
        
        
        self.statusBar().showMessage('Recherche negatss')
        l_negats = driver.find_elements_by_class_name("danger")
        self.statusBar().showMessage('Traitement negatss')
        negats_raw = [elem.text for elem in l_negats]
        negats_raw = [elem.split(' ')[-2] for elem in negats_raw]
        negats_raw = [float(elem[:-1].replace(',', '.')) for elem in negats_raw]
        #print(negats_raw)
        total_negats = sum(negats_raw) 
        print(total_negats)
        self.ui.UI_TEXT_NEGATS.setText(str(total_negats))
        
        self.ui.UI_TEXT_TOTAL.setText(str(total_positss + total_negats))
        self.statusBar().showMessage('Fini')"""






if __name__ == "__main__":
    #PyQT
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("plastique"))

    selection = Ecran_menuPrincipal()
    selection.show()
    sys.exit(app.exec_())
