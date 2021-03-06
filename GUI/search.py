# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Searched.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1068, 595)
        self.label = QtWidgets.QLabel(Form)
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
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 130, 981, 381))
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
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 60, 181, 31))
        self.pushButton_4.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(240, 240, 240)\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(240, 60, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 530, 121, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-radius: 12px;\n"
"background-color: rgb(192,192,192);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
        self.pushButton_4.setText(_translate("Form", "Search Data by Selecting:"))
        self.comboBox.setItemText(0, _translate("Form", "Name"))
        self.comboBox.setItemText(1, _translate("Form", "Product ID"))
        self.comboBox.setItemText(2, _translate("Form", "SKU"))
        self.comboBox.setItemText(3, _translate("Form", "Brand "))
        self.pushButton_3.setText(_translate("Form", "Close"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
