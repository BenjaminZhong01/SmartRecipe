# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nutrition_main.py'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import nutrition_api
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import requests
import pandas as pd

header = {'x-app-id': '564584ad', 'x-app-key': '596ecbf4294f77e67bc3fff38c4b4465', 'x-remote-user-id': '0'}
url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'


class MyWindow(QMainWindow, nutrition_api.Ui_MainWindow):
    food_list = []
    conflict_list = []

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        df = pd.read_csv('FoodDataFinalClean.csv')
        self.conflict_list = df['food_conflicts'].str.lower().str.split(", ")
        # print(self.conflict_list)
        self.searchButton.clicked.connect(lambda: self.search_api())
        self.initUI()
        self.secondwindow = MyWindow2()
        self.btn.clicked.connect(lambda: self.passData())

  
    def initUI(self):
        self.btn = QPushButton("Continue", self)
        self.btn.move(700, 500)

    def search_api(self):
        self.food_list = []
        query = {'query': self.searchBox.toPlainText()}
        result = requests.post(url=url, headers=header, data=query)
        if 'couldn\'t match any' not in result.text:
            result = result.json()['foods']
            total_calories = 0
            for food in result:
                self.food_list.append(food['food_name'].lower())
                total_calories += food['nf_calories']
            self.resultBox.setText(str(total_calories))
            print(self.food_list)
            self.load_food_conflict()
    

    def load_food_conflict(self):

        # print(conflict_list)
        conflict_result = set()
        for l in self.conflict_list:

            if len(l) == 1:
                continue
            # print(l)
            count = 0
            temp_result = set()
            for food in self.food_list:
                if food in l:
                    count += 1
                    temp_result.add(food)
            # print(count)
            if float(count) / len(l) > 0.7:
                # print(l)
                conflict_result = conflict_result.union(temp_result)
        # print(conflict_result)
        message = ''
        if len(conflict_result) != 0:
            message = ', '.join(conflict_result)
            message = 'Warning: ' + str(message) + ' together could cause serious illness!!!!'

        allergy_list = self.find_allergy_sources()
        if len(allergy_list) != 0:
            message += '\nAllergy warning: ' + str(', '.join(allergy_list)) + ' might cause allergy!'

        self.warningMsg.setText(message)

    def find_allergy_sources(self):
        allergy_list = []
        for l in self.conflict_list:
            if len(l) == 1:
                if l[0] in self.food_list:
                    allergy_list.append(l[0])
        return allergy_list

    def passData(self):
        tftb=str(self.searchBox.toPlainText()).replace('\n', ',')
        self.secondwindow.textBrowser_2.setText(tftb)
        #self.secondwindow.textBrowser_2.setText(self.searchBox.toPlainText())
        print(self.searchBox.toPlainText())
        print(tftb)
        self.secondwindow.dispayInfo()



from python_ui import *
#from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import python_ui


class MyWindow2(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow2, self).__init__(parent)
        self.setupUi(self)

    def dispayInfo(self):
        self.show()
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MyWindow()
    b = MyWindow2()
    a.show()
    # a.btn.clicked.connect(b.show)
    sys.exit(app.exec_())
