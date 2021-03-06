# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScrappedUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1200, 800))
        Form.setMaximumSize(QtCore.QSize(1200, 800))
        Form.setBaseSize(QtCore.QSize(1200, 800))
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(1200, 800))
        self.label.setMaximumSize(QtCore.QSize(1200, 800))
        self.label.setBaseSize(QtCore.QSize(1200, 800))
        self.label.setStyleSheet("background-image: url(:/bg/Purple-Abstract-Webpage-Background-Graphics-1.jpg);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(770, 380, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(400, 400))
        self.label_2.setMaximumSize(QtCore.QSize(400, 400))
        self.label_2.setBaseSize(QtCore.QSize(400, 400))
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-image: url(:/Logo/unnamed.png);\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 1151, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(80, 520, 591, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 570, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 570, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pause/icons8_pause_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 570, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("\n"
"border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resume/icons8_resume_button_48px_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 301, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 18px;\n"
"background-color: rgb(240, 240, 240)")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 620, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(80, 620, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 520, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("\n"
"border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo_start/icons8_play_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 670, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 670, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);\n"
"")
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(270, 620, 95, 31))
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(370, 620, 95, 31))
        self.radioButton_2.setAutoFillBackground(False)
        self.radioButton_2.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(470, 620, 95, 31))
        self.radioButton_3.setAutoFillBackground(False)
        self.radioButton_3.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.label.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.tableWidget.raise_()
        self.pushButton_4.raise_()
        self.comboBox.raise_()
        self.pushButton_6.raise_()
        self.label_4.raise_()
        self.pushButton_5.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.pushButton_5.clicked.connect(self.loadFileData)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
     # function to load CSV Data into the Qwidget Table
    def loadFileData(self):
        df = pd.read_csv("C:\\Users\\Khadija\\Documents\\CS261F21PID24\\GUI\\forTestingData.csv", encoding='unicode_escape')
        if df.size == 0:
            return
        df.fillna('', inplace=True)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)
                self.tableWidget.setColumnWidth(1, 300)
                self.tableWidget.setColumnWidth(10, 500)
    def clear_table(self):
             while (self.tableWidget.rowCount() > 0):
                    self.tableWidget.removeRow(0)
    def set_ProgressBar_Property(self,value):
            self.progressBar.setProperty('value', value)


    #First Algorithm (insertion Sort) to sort csv file according to the specific column
    def Algorithm(self,column_name):
        self.tableWidget.setRowCount(0)
        if(self.comboBox.currentText() == 'Insertion Sort'):
                df = pd.read_csv("C:\\Users\\Khadija\\Documents\\CS261F21PID24\\GUI\\forTestingData.csv", encoding='unicode_escape')
                count = 0
                for i in range(1, len(df)):
                                ydKey=df.iloc[i]
                                key = df.iloc[i][column_name] 
                                j = i - 1
                                x = df.iloc[j][column_name]
                                while (j >= 0 and x > key):
                                        m = j+1
                                        df.iloc[m] = df.iloc[j]
                                        j = j - 1
                                        x = df.iloc[j][column_name]
                                
                                y = j + 1
                                df.iloc[y] = ydKey
                                count = count + 1
                                perc = (count * 100) // len(df)
                                self.set_ProgressBar_Property(perc)

                print(df)

                   
                if df.size == 0:
                   return
                df.fillna('', inplace=True)
                self.tableWidget.setRowCount(df.shape[0])
                self.tableWidget.setColumnCount(df.shape[1])
                self.tableWidget.setHorizontalHeaderLabels(df.columns)
                for row in df.iterrows():
                        values = row[1]
                        for col_index, value in enumerate(values):
                            if isinstance(value, (float, int)):
                                value = '{0:0,.0f}'.format(value)
                            tableItem = QtWidgets.QTableWidgetItem(str(value))
                            self.tableWidget.setItem(row[0], col_index, tableItem)
                            self.tableWidget.setColumnWidth(1, 300)
                            self.tableWidget.setColumnWidth(10, 500)

        if(self.comboBox.currentText() == 'Selection Sort'):
                print("")
    def getColumnName (self):
        if(self.radioButton.isChecked()):
                name = "Product Name"
                self.Algorithm(name)
        if(self.radioButton_2.isChecked()):
                name = "Price"
                self.Algorithm(name)
        if(self.radioButton_3.isChecked()):
                name = "Product ID"
                self.Algorithm(name)

        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Color"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "SKU"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Sole Type"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Sale percentage"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Sale Price"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Season"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Size"))
        self.pushButton.setText(_translate("Form", "Exit"))
        self.pushButton_2.setText(_translate("Form", "Pause"))
        self.pushButton_3.setText(_translate("Form", "Resume"))
        self.label_3.setText(_translate("Form", "    Scrapped Data View"))
        self.pushButton_4.setText(_translate("Form", "Sort Data Using Algorithm"))
        self.comboBox.setItemText(0, _translate("Form", "Insertion Sort"))
        self.comboBox.setItemText(1, _translate("Form", "Counting Sort"))
        self.comboBox.setItemText(2, _translate("Form", "Merge Sort"))
        self.comboBox.setItemText(3, _translate("Form", "Selection Sort"))
        self.pushButton_5.setText(_translate("Form", "Start Loading Scrapped Data"))
        self.pushButton_6.setText(_translate("Form", "Next"))
        self.label_4.setText(_translate("Form", "  Want to Search item?"))
        self.radioButton.setText(_translate("Form", "Name "))
        self.radioButton_2.setText(_translate("Form", "Price"))
        self.radioButton_3.setText(_translate("Form", "Product ID"))
        self.pushButton_4.clicked.connect(self.getColumnName)
        
import mc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
