# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 300)
        MainWindow.setMinimumSize(QtCore.QSize(900, 300))
        MainWindow.setMaximumSize(QtCore.QSize(900, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setMinimumSize(QtCore.QSize(60, 0))
        self.label_50.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.gridLayout_10.addWidget(self.label_50, 0, 2, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setMinimumSize(QtCore.QSize(35, 0))
        self.label_51.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.gridLayout_10.addWidget(self.label_51, 0, 5, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setMinimumSize(QtCore.QSize(20, 0))
        self.label_49.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout_10.addWidget(self.label_49, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_10.addWidget(self.lineEdit, 0, 4, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setMinimumSize(QtCore.QSize(400, 35))
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_10.addWidget(self.label_39, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setMinimumSize(QtCore.QSize(400, 35))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout_11.addWidget(self.label_40, 0, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setMinimumSize(QtCore.QSize(20, 0))
        self.label_46.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.gridLayout_11.addWidget(self.label_46, 0, 2, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setMinimumSize(QtCore.QSize(35, 0))
        self.label_47.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout_11.addWidget(self.label_47, 0, 4, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_9.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_9.setFont(font)
        self.doubleSpinBox_9.setDecimals(2)
        self.doubleSpinBox_9.setMinimum(-16777215.0)
        self.doubleSpinBox_9.setMaximum(16777215.0)
        self.doubleSpinBox_9.setSingleStep(0.01)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_11.addWidget(self.doubleSpinBox_9, 0, 3, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setMinimumSize(QtCore.QSize(60, 0))
        self.label_45.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.gridLayout_11.addWidget(self.label_45, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.gridLayout_5.addWidget(self.label_44, 0, 1, 1, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setMinimumSize(QtCore.QSize(400, 35))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout_12.addWidget(self.label_41, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setMinimumSize(QtCore.QSize(60, 0))
        self.label_55.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 0, 0, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setMinimumSize(QtCore.QSize(20, 0))
        self.label_56.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.gridLayout.addWidget(self.label_56, 0, 1, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_11.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_11.setFont(font)
        self.doubleSpinBox_11.setDecimals(0)
        self.doubleSpinBox_11.setMinimum(-16777215.0)
        self.doubleSpinBox_11.setMaximum(16777215.0)
        self.doubleSpinBox_11.setSingleStep(1.0)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout.addWidget(self.doubleSpinBox_11, 0, 2, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setMinimumSize(QtCore.QSize(35, 0))
        self.label_57.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 0, 3, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.gridLayout.addWidget(self.label_58, 0, 4, 1, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: red")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_14.addWidget(self.label_13, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_14.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_14, 3, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверка гипотезы о существовании различий урожайности двух сортов некоторой культуры "))
        self.label_50.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p>Введите наименование культуры:</p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p>Введите уровень значимости:</p></body></html>"))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p>α</p></body></html>"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p>Введите количество лет, на протяжении которых проводилось наблюдение:</p></body></html>"))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p>n</p></body></html>"))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Заполните исходную таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Результат"))
