# Form implementation generated from reading ui file 'Ui_Sucursal.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sucursal(object):
    def setupUi(self, Ui_Sucursal):
        Ui_Sucursal.setObjectName("Ui_Sucursal")
        Ui_Sucursal.resize(929, 625)
        Ui_Sucursal.setStyleSheet("QWidget{\n"
"background-color: rgb(251, 251, 254);\n"
"}\n"
"\n"
"QHBoxLayout{\n"
"background-color: black;\n"
"}\n"
"\n"
"QDateEdit{\n"
"font-family:\"Sans-serif\";\n"
"font-size:12px;\n"
"padding:10px 10px;\n"
"border-radius:20px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"\n"
"}\n"
"QLabel{\n"
"font-family:\"Sans-serif\";\n"
"font-size:12px;\n"
"padding:5px;\n"
"\n"
"}\n"
"\n"
"QComboBox{\n"
"font-family:\"Sans-serif\";\n"
"font-size:12px;\n"
"padding:10px 10px;\n"
"border-radius:20px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-family:\"Sans-serif\";\n"
"font-size:12px;\n"
"padding:10px 10px;\n"
"border-radius:20px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QPushButton{\n"
"font-family:\"Sans-serif\";\n"
"font-size:12px;\n"
"padding: 10px 10px;\n"
"border-radius: 25px;\n"
"border:2px solid rgb(228, 232, 235);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(118, 129, 249);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:2px solid rgb(118, 129, 249);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Ui_Sucursal)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=Ui_Sucursal)
        self.frame.setStyleSheet("background-color: rgb(118, 129, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAtras = QtWidgets.QPushButton(parent=Ui_Sucursal)
        self.btnAtras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/backButton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAtras.setIcon(icon)
        self.btnAtras.setIconSize(QtCore.QSize(30, 30))
        self.btnAtras.setFlat(True)
        self.btnAtras.setObjectName("btnAtras")
        self.horizontalLayout.addWidget(self.btnAtras)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblSucursal = QtWidgets.QLabel(parent=Ui_Sucursal)
        self.lblSucursal.setObjectName("lblSucursal")
        self.horizontalLayout.addWidget(self.lblSucursal)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tbSucursal = QtWidgets.QTabWidget(parent=Ui_Sucursal)
        self.tbSucursal.setObjectName("tbSucursal")
        self.tbIngresar = QtWidgets.QWidget()
        self.tbIngresar.setObjectName("tbIngresar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tbIngresar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblProvinciaIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblProvinciaIngresar.setObjectName("lblProvinciaIngresar")
        self.gridLayout_2.addWidget(self.lblProvinciaIngresar, 6, 0, 1, 1)
        self.txtTelefonoIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtTelefonoIngresar.setObjectName("txtTelefonoIngresar")
        self.gridLayout_2.addWidget(self.txtTelefonoIngresar, 5, 0, 1, 1)
        self.txtNombreIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtNombreIngresar.setObjectName("txtNombreIngresar")
        self.gridLayout_2.addWidget(self.txtNombreIngresar, 1, 0, 1, 1)
        self.lblTelefonoIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblTelefonoIngresar.setObjectName("lblTelefonoIngresar")
        self.gridLayout_2.addWidget(self.lblTelefonoIngresar, 4, 0, 1, 1)
        self.lblDireccionIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblDireccionIngresar.setObjectName("lblDireccionIngresar")
        self.gridLayout_2.addWidget(self.lblDireccionIngresar, 2, 0, 1, 1)
        self.lblNombreIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblNombreIngresar.setObjectName("lblNombreIngresar")
        self.gridLayout_2.addWidget(self.lblNombreIngresar, 0, 0, 1, 1)
        self.txtDireccionIngresar = QtWidgets.QLineEdit(parent=self.tbIngresar)
        self.txtDireccionIngresar.setObjectName("txtDireccionIngresar")
        self.gridLayout_2.addWidget(self.txtDireccionIngresar, 3, 0, 1, 1)
        self.cmbProvinciaIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbProvinciaIngresar.setEnabled(True)
        self.cmbProvinciaIngresar.setEditable(True)
        self.cmbProvinciaIngresar.setObjectName("cmbProvinciaIngresar")
        self.gridLayout_2.addWidget(self.cmbProvinciaIngresar, 7, 0, 1, 1)
        self.cmbCiudadIngresar = QtWidgets.QComboBox(parent=self.tbIngresar)
        self.cmbCiudadIngresar.setEditable(True)
        self.cmbCiudadIngresar.setObjectName("cmbCiudadIngresar")
        self.gridLayout_2.addWidget(self.cmbCiudadIngresar, 9, 0, 1, 1)
        self.lblCiudadIngresar = QtWidgets.QLabel(parent=self.tbIngresar)
        self.lblCiudadIngresar.setObjectName("lblCiudadIngresar")
        self.gridLayout_2.addWidget(self.lblCiudadIngresar, 8, 0, 1, 1)
        self.btnIngresarSucursal = QtWidgets.QPushButton(parent=self.tbIngresar)
        self.btnIngresarSucursal.setStyleSheet("border-radius: 15px;")
        self.btnIngresarSucursal.setObjectName("btnIngresarSucursal")
        self.gridLayout_2.addWidget(self.btnIngresarSucursal, 11, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 10, 0, 1, 1)
        self.tbSucursal.addTab(self.tbIngresar, "")
        self.tbModificar = QtWidgets.QWidget()
        self.tbModificar.setObjectName("tbModificar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tbModificar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblNombreModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblNombreModificar.setObjectName("lblNombreModificar")
        self.gridLayout_3.addWidget(self.lblNombreModificar, 0, 0, 1, 1)
        self.cmbNombreModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbNombreModificar.setObjectName("cmbNombreModificar")
        self.gridLayout_3.addWidget(self.cmbNombreModificar, 1, 0, 1, 1)
        self.lblDireccionModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblDireccionModificar.setObjectName("lblDireccionModificar")
        self.gridLayout_3.addWidget(self.lblDireccionModificar, 2, 0, 1, 1)
        self.txtDireccionModificar = QtWidgets.QLineEdit(parent=self.tbModificar)
        self.txtDireccionModificar.setObjectName("txtDireccionModificar")
        self.gridLayout_3.addWidget(self.txtDireccionModificar, 3, 0, 1, 1)
        self.lblTelefonoModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblTelefonoModificar.setObjectName("lblTelefonoModificar")
        self.gridLayout_3.addWidget(self.lblTelefonoModificar, 4, 0, 1, 1)
        self.txtTelefonoModificar = QtWidgets.QLineEdit(parent=self.tbModificar)
        self.txtTelefonoModificar.setObjectName("txtTelefonoModificar")
        self.gridLayout_3.addWidget(self.txtTelefonoModificar, 5, 0, 1, 1)
        self.lblProvinciaModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblProvinciaModificar.setObjectName("lblProvinciaModificar")
        self.gridLayout_3.addWidget(self.lblProvinciaModificar, 6, 0, 1, 1)
        self.cmbProvinciaModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbProvinciaModificar.setEditable(True)
        self.cmbProvinciaModificar.setObjectName("cmbProvinciaModificar")
        self.gridLayout_3.addWidget(self.cmbProvinciaModificar, 7, 0, 1, 1)
        self.lblCiudadModificar = QtWidgets.QLabel(parent=self.tbModificar)
        self.lblCiudadModificar.setObjectName("lblCiudadModificar")
        self.gridLayout_3.addWidget(self.lblCiudadModificar, 8, 0, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(parent=self.tbModificar)
        self.btnGuardarCambios.setStyleSheet("border-radius: 15px;")
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout_3.addWidget(self.btnGuardarCambios, 11, 0, 1, 1)
        self.cmbCiudadModificar = QtWidgets.QComboBox(parent=self.tbModificar)
        self.cmbCiudadModificar.setEditable(True)
        self.cmbCiudadModificar.setObjectName("cmbCiudadModificar")
        self.gridLayout_3.addWidget(self.cmbCiudadModificar, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 10, 0, 1, 1)
        self.tbSucursal.addTab(self.tbModificar, "")
        self.tbEliminar = QtWidgets.QWidget()
        self.tbEliminar.setObjectName("tbEliminar")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tbEliminar)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cmbNombreEliminar = QtWidgets.QComboBox(parent=self.tbEliminar)
        self.cmbNombreEliminar.setObjectName("cmbNombreEliminar")
        self.gridLayout_4.addWidget(self.cmbNombreEliminar, 1, 0, 1, 1)
        self.btnEliminarSucursal = QtWidgets.QPushButton(parent=self.tbEliminar)
        self.btnEliminarSucursal.setStyleSheet("border-radius: 15px;")
        self.btnEliminarSucursal.setObjectName("btnEliminarSucursal")
        self.gridLayout_4.addWidget(self.btnEliminarSucursal, 3, 0, 1, 1)
        self.lblNombreEliminar = QtWidgets.QLabel(parent=self.tbEliminar)
        self.lblNombreEliminar.setObjectName("lblNombreEliminar")
        self.gridLayout_4.addWidget(self.lblNombreEliminar, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        self.tbSucursal.addTab(self.tbEliminar, "")
        self.tbListar = QtWidgets.QWidget()
        self.tbListar.setObjectName("tbListar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tbListar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.twSucursales = QtWidgets.QTableWidget(parent=self.tbListar)
        self.twSucursales.setObjectName("twSucursales")
        self.twSucursales.setColumnCount(0)
        self.twSucursales.setRowCount(0)
        self.twSucursales.horizontalHeader().setDefaultSectionSize(400)
        self.gridLayout_5.addWidget(self.twSucursales, 0, 0, 1, 1)
        self.tbSucursal.addTab(self.tbListar, "")
        self.gridLayout.addWidget(self.tbSucursal, 2, 0, 1, 1)

        self.retranslateUi(Ui_Sucursal)
        self.tbSucursal.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Ui_Sucursal)

    def retranslateUi(self, Ui_Sucursal):
        _translate = QtCore.QCoreApplication.translate
        Ui_Sucursal.setWindowTitle(_translate("Ui_Sucursal", "Sucursal"))
        self.lblSucursal.setText(_translate("Ui_Sucursal", "Sucursal"))
        self.lblProvinciaIngresar.setText(_translate("Ui_Sucursal", "Provincia"))
        self.txtTelefonoIngresar.setPlaceholderText(_translate("Ui_Sucursal", "Ingrese teléfono"))
        self.txtNombreIngresar.setPlaceholderText(_translate("Ui_Sucursal", "Ingrese nombre sucursal"))
        self.lblTelefonoIngresar.setText(_translate("Ui_Sucursal", "Teléfono"))
        self.lblDireccionIngresar.setText(_translate("Ui_Sucursal", "Dirección"))
        self.lblNombreIngresar.setText(_translate("Ui_Sucursal", "Nombre"))
        self.txtDireccionIngresar.setPlaceholderText(_translate("Ui_Sucursal", "Ingrese dirección"))
        self.lblCiudadIngresar.setText(_translate("Ui_Sucursal", "Ciudad"))
        self.btnIngresarSucursal.setText(_translate("Ui_Sucursal", "Ingresar sucursal"))
        self.tbSucursal.setTabText(self.tbSucursal.indexOf(self.tbIngresar), _translate("Ui_Sucursal", "Ingresar"))
        self.lblNombreModificar.setText(_translate("Ui_Sucursal", "Nombre"))
        self.lblDireccionModificar.setText(_translate("Ui_Sucursal", "Dirección"))
        self.txtDireccionModificar.setPlaceholderText(_translate("Ui_Sucursal", "Ingrese dirección"))
        self.lblTelefonoModificar.setText(_translate("Ui_Sucursal", "Teléfono"))
        self.txtTelefonoModificar.setPlaceholderText(_translate("Ui_Sucursal", "Ingrese teléfono"))
        self.lblProvinciaModificar.setText(_translate("Ui_Sucursal", "Provincia"))
        self.lblCiudadModificar.setText(_translate("Ui_Sucursal", "Ciudad"))
        self.btnGuardarCambios.setText(_translate("Ui_Sucursal", "Guardar cambios"))
        self.tbSucursal.setTabText(self.tbSucursal.indexOf(self.tbModificar), _translate("Ui_Sucursal", "Modificar"))
        self.btnEliminarSucursal.setText(_translate("Ui_Sucursal", "Eliminar sucursal"))
        self.lblNombreEliminar.setText(_translate("Ui_Sucursal", "Nombre"))
        self.tbSucursal.setTabText(self.tbSucursal.indexOf(self.tbEliminar), _translate("Ui_Sucursal", "Eliminar"))
        self.tbSucursal.setTabText(self.tbSucursal.indexOf(self.tbListar), _translate("Ui_Sucursal", "Listar"))
