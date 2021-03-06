# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_group_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 287)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 11, 471, 265))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_form = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_form.setContentsMargins(0, 0, 0, 0)
        self.layout_form.setObjectName("layout_form")
        self.edit_title = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_title.setObjectName("edit_title")
        self.layout_form.addWidget(self.edit_title, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem, 1, 0, 1, 2)
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_title.setObjectName("label_title")
        self.layout_form.addWidget(self.label_title, 0, 0, 1, 1)
        self.edit_description = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_description.setObjectName("edit_description")
        self.layout_form.addWidget(self.edit_description, 2, 1, 1, 1)
        self.combo_type = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_type.setObjectName("combo_type")
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.layout_form.addWidget(self.combo_type, 4, 1, 1, 1)
        self.label_type = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_type.setObjectName("label_type")
        self.layout_form.addWidget(self.label_type, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem1, 3, 0, 1, 2)
        self.check_deletePast = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_deletePast.setObjectName("check_deletePast")
        self.layout_form.addWidget(self.check_deletePast, 6, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem2, 5, 0, 1, 2)
        self.label_description = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_description.setObjectName("label_description")
        self.layout_form.addWidget(self.label_description, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem3, 7, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layout_form.addWidget(self.buttonBox, 10, 0, 1, 2)
        self.label_info = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_info.setStyleSheet("QLabel {\n"
"color: rgb(255, 53, 53);\n"
"}")
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.layout_form.addWidget(self.label_info, 9, 0, 1, 2)
        self.label_remark = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_remark.setObjectName("label_remark")
        self.layout_form.addWidget(self.label_remark, 8, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "Название *"))
        self.combo_type.setItemText(0, _translate("Dialog", "Без даты и времени"))
        self.combo_type.setItemText(1, _translate("Dialog", "Только дата"))
        self.combo_type.setItemText(2, _translate("Dialog", "Дата и время"))
        self.label_type.setText(_translate("Dialog", "Тип задач"))
        self.check_deletePast.setText(_translate("Dialog", "Удалять прошедшие задачи"))
        self.label_description.setText(_translate("Dialog", "Описание"))
        self.label_remark.setText(_translate("Dialog", "* Обязательно к заполнению"))
