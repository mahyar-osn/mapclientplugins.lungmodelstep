# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\lungmodelwidget_temp.ui'
#
# Created: Sun Dec  2 13:30:02 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LungModelWidget(object):
    def setupUi(self, LungModelWidget):
        LungModelWidget.setObjectName("LungModelWidget")
        LungModelWidget.resize(983, 802)
        self.horizontalLayout = QtGui.QHBoxLayout(LungModelWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.controlPanel_groupBox = QtGui.QGroupBox(LungModelWidget)
        self.controlPanel_groupBox.setObjectName("controlPanel_groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.controlPanel_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lung_groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.lung_groupBox.setObjectName("lung_groupBox")
        self.gridLayout_9 = QtGui.QGridLayout(self.lung_groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.leftLung = QtGui.QLabel(self.lung_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLung.sizePolicy().hasHeightForWidth())
        self.leftLung.setSizePolicy(sizePolicy)
        self.leftLung.setObjectName("leftLung")
        self.gridLayout_9.addWidget(self.leftLung, 0, 0, 1, 1)
        self.rightLung = QtGui.QLabel(self.lung_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLung.sizePolicy().hasHeightForWidth())
        self.rightLung.setSizePolicy(sizePolicy)
        self.rightLung.setObjectName("rightLung")
        self.gridLayout_9.addWidget(self.rightLung, 0, 2, 1, 1)
        self.rightLung_checkBox = QtGui.QCheckBox(self.lung_groupBox)
        self.rightLung_checkBox.setText("")
        self.rightLung_checkBox.setObjectName("rightLung_checkBox")
        self.gridLayout_9.addWidget(self.rightLung_checkBox, 0, 3, 1, 1)
        self.leftLung_checkBox = QtGui.QCheckBox(self.lung_groupBox)
        self.leftLung_checkBox.setText("")
        self.leftLung_checkBox.setObjectName("leftLung_checkBox")
        self.gridLayout_9.addWidget(self.leftLung_checkBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.lung_groupBox)
        self.line = QtGui.QFrame(self.controlPanel_groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.airway_groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.airway_groupBox.setObjectName("airway_groupBox")
        self.gridLayout_6 = QtGui.QGridLayout(self.airway_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.leftAirway = QtGui.QLabel(self.airway_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftAirway.sizePolicy().hasHeightForWidth())
        self.leftAirway.setSizePolicy(sizePolicy)
        self.leftAirway.setObjectName("leftAirway")
        self.gridLayout_6.addWidget(self.leftAirway, 0, 0, 1, 1)
        self.rightAirway = QtGui.QLabel(self.airway_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightAirway.sizePolicy().hasHeightForWidth())
        self.rightAirway.setSizePolicy(sizePolicy)
        self.rightAirway.setObjectName("rightAirway")
        self.gridLayout_6.addWidget(self.rightAirway, 0, 2, 1, 1)
        self.rightAirway_checkBox = QtGui.QCheckBox(self.airway_groupBox)
        self.rightAirway_checkBox.setText("")
        self.rightAirway_checkBox.setObjectName("rightAirway_checkBox")
        self.gridLayout_6.addWidget(self.rightAirway_checkBox, 0, 3, 1, 1)
        self.leftAirway_checkBox = QtGui.QCheckBox(self.airway_groupBox)
        self.leftAirway_checkBox.setText("")
        self.leftAirway_checkBox.setObjectName("leftAirway_checkBox")
        self.gridLayout_6.addWidget(self.leftAirway_checkBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.airway_groupBox)
        self.line_2 = QtGui.QFrame(self.controlPanel_groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.artery_groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.artery_groupBox.setObjectName("artery_groupBox")
        self.gridLayout_7 = QtGui.QGridLayout(self.artery_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.leftArtery = QtGui.QLabel(self.artery_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftArtery.sizePolicy().hasHeightForWidth())
        self.leftArtery.setSizePolicy(sizePolicy)
        self.leftArtery.setObjectName("leftArtery")
        self.gridLayout_7.addWidget(self.leftArtery, 0, 0, 1, 1)
        self.rightArtery = QtGui.QLabel(self.artery_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightArtery.sizePolicy().hasHeightForWidth())
        self.rightArtery.setSizePolicy(sizePolicy)
        self.rightArtery.setObjectName("rightArtery")
        self.gridLayout_7.addWidget(self.rightArtery, 0, 2, 1, 1)
        self.rightArtery_checkBox = QtGui.QCheckBox(self.artery_groupBox)
        self.rightArtery_checkBox.setText("")
        self.rightArtery_checkBox.setObjectName("rightArtery_checkBox")
        self.gridLayout_7.addWidget(self.rightArtery_checkBox, 0, 3, 1, 1)
        self.leftArtery_checkBox = QtGui.QCheckBox(self.artery_groupBox)
        self.leftArtery_checkBox.setText("")
        self.leftArtery_checkBox.setObjectName("leftArtery_checkBox")
        self.gridLayout_7.addWidget(self.leftArtery_checkBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.artery_groupBox)
        self.line_3 = QtGui.QFrame(self.controlPanel_groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.vein_groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.vein_groupBox.setObjectName("vein_groupBox")
        self.gridLayout_8 = QtGui.QGridLayout(self.vein_groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.rightVein_checkBox = QtGui.QCheckBox(self.vein_groupBox)
        self.rightVein_checkBox.setText("")
        self.rightVein_checkBox.setObjectName("rightVein_checkBox")
        self.gridLayout_8.addWidget(self.rightVein_checkBox, 0, 3, 1, 1)
        self.rightVein = QtGui.QLabel(self.vein_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightVein.sizePolicy().hasHeightForWidth())
        self.rightVein.setSizePolicy(sizePolicy)
        self.rightVein.setObjectName("rightVein")
        self.gridLayout_8.addWidget(self.rightVein, 0, 2, 1, 1)
        self.leftVein_checkBox = QtGui.QCheckBox(self.vein_groupBox)
        self.leftVein_checkBox.setText("")
        self.leftVein_checkBox.setObjectName("leftVein_checkBox")
        self.gridLayout_8.addWidget(self.leftVein_checkBox, 0, 1, 1, 1)
        self.leftVein = QtGui.QLabel(self.vein_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftVein.sizePolicy().hasHeightForWidth())
        self.leftVein.setSizePolicy(sizePolicy)
        self.leftVein.setObjectName("leftVein")
        self.gridLayout_8.addWidget(self.leftVein, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.vein_groupBox)
        self.line_4 = QtGui.QFrame(self.controlPanel_groupBox)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.morphing_groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.morphing_groupBox.setObjectName("morphing_groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.morphing_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.modeTwo_doubleSpinBox = QtGui.QDoubleSpinBox(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeTwo_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.modeTwo_doubleSpinBox.setSizePolicy(sizePolicy)
        self.modeTwo_doubleSpinBox.setMinimum(-3.0)
        self.modeTwo_doubleSpinBox.setMaximum(3.0)
        self.modeTwo_doubleSpinBox.setSingleStep(0.1)
        self.modeTwo_doubleSpinBox.setObjectName("modeTwo_doubleSpinBox")
        self.gridLayout_2.addWidget(self.modeTwo_doubleSpinBox, 0, 3, 1, 1)
        self.modeFour_label = QtGui.QLabel(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeFour_label.sizePolicy().hasHeightForWidth())
        self.modeFour_label.setSizePolicy(sizePolicy)
        self.modeFour_label.setObjectName("modeFour_label")
        self.gridLayout_2.addWidget(self.modeFour_label, 2, 2, 1, 1)
        self.modeThree_doubleSpinBox = QtGui.QDoubleSpinBox(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeThree_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.modeThree_doubleSpinBox.setSizePolicy(sizePolicy)
        self.modeThree_doubleSpinBox.setMinimum(-3.0)
        self.modeThree_doubleSpinBox.setMaximum(3.0)
        self.modeThree_doubleSpinBox.setSingleStep(0.1)
        self.modeThree_doubleSpinBox.setObjectName("modeThree_doubleSpinBox")
        self.gridLayout_2.addWidget(self.modeThree_doubleSpinBox, 2, 1, 1, 1)
        self.modeOne_label = QtGui.QLabel(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeOne_label.sizePolicy().hasHeightForWidth())
        self.modeOne_label.setSizePolicy(sizePolicy)
        self.modeOne_label.setObjectName("modeOne_label")
        self.gridLayout_2.addWidget(self.modeOne_label, 0, 0, 1, 1)
        self.modeSix_label = QtGui.QLabel(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeSix_label.sizePolicy().hasHeightForWidth())
        self.modeSix_label.setSizePolicy(sizePolicy)
        self.modeSix_label.setObjectName("modeSix_label")
        self.gridLayout_2.addWidget(self.modeSix_label, 4, 2, 1, 1)
        self.modeThree_label = QtGui.QLabel(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeThree_label.sizePolicy().hasHeightForWidth())
        self.modeThree_label.setSizePolicy(sizePolicy)
        self.modeThree_label.setObjectName("modeThree_label")
        self.gridLayout_2.addWidget(self.modeThree_label, 2, 0, 1, 1)
        self.modeSix_doubleSpinBox = QtGui.QDoubleSpinBox(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeSix_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.modeSix_doubleSpinBox.setSizePolicy(sizePolicy)
        self.modeSix_doubleSpinBox.setMinimum(-3.0)
        self.modeSix_doubleSpinBox.setMaximum(3.0)
        self.modeSix_doubleSpinBox.setSingleStep(0.1)
        self.modeSix_doubleSpinBox.setObjectName("modeSix_doubleSpinBox")
        self.gridLayout_2.addWidget(self.modeSix_doubleSpinBox, 4, 3, 1, 1)
        self.modeFive_label = QtGui.QLabel(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeFive_label.sizePolicy().hasHeightForWidth())
        self.modeFive_label.setSizePolicy(sizePolicy)
        self.modeFive_label.setObjectName("modeFive_label")
        self.gridLayout_2.addWidget(self.modeFive_label, 4, 0, 1, 1)
        self.modeOne_doubleSpinBox = QtGui.QDoubleSpinBox(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeOne_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.modeOne_doubleSpinBox.setSizePolicy(sizePolicy)
        self.modeOne_doubleSpinBox.setMinimum(-3.0)
        self.modeOne_doubleSpinBox.setMaximum(3.0)
        self.modeOne_doubleSpinBox.setSingleStep(0.1)
        self.modeOne_doubleSpinBox.setObjectName("modeOne_doubleSpinBox")
        self.gridLayout_2.addWidget(self.modeOne_doubleSpinBox, 0, 1, 1, 1)
        self.modeFive_doubleSpinBox = QtGui.QDoubleSpinBox(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeFive_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.modeFive_doubleSpinBox.setSizePolicy(sizePolicy)
        self.modeFive_doubleSpinBox.setMinimum(-3.0)
        self.modeFive_doubleSpinBox.setMaximum(3.0)
        self.modeFive_doubleSpinBox.setSingleStep(0.1)
        self.modeFive_doubleSpinBox.setObjectName("modeFive_doubleSpinBox")
        self.gridLayout_2.addWidget(self.modeFive_doubleSpinBox, 4, 1, 1, 1)
        self.modeTwo_label = QtGui.QLabel(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeTwo_label.sizePolicy().hasHeightForWidth())
        self.modeTwo_label.setSizePolicy(sizePolicy)
        self.modeTwo_label.setObjectName("modeTwo_label")
        self.gridLayout_2.addWidget(self.modeTwo_label, 0, 2, 1, 1)
        self.modeFour_doubleSpinBox = QtGui.QDoubleSpinBox(self.morphing_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeFour_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.modeFour_doubleSpinBox.setSizePolicy(sizePolicy)
        self.modeFour_doubleSpinBox.setMinimum(-3.0)
        self.modeFour_doubleSpinBox.setMaximum(3.0)
        self.modeFour_doubleSpinBox.setSingleStep(0.1)
        self.modeFour_doubleSpinBox.setObjectName("modeFour_doubleSpinBox")
        self.gridLayout_2.addWidget(self.modeFour_doubleSpinBox, 2, 3, 1, 1)
        self.verticalLayout.addWidget(self.morphing_groupBox)
        self.reset_pushButton = QtGui.QPushButton(self.controlPanel_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_pushButton.setSizePolicy(sizePolicy)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.verticalLayout.addWidget(self.reset_pushButton)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.exit_pushButton = QtGui.QPushButton(self.groupBox)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.horizontalLayout_3.addWidget(self.exit_pushButton)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.controlPanel_groupBox)
        self.sceneviewer_widget = SceneviewerWidget(LungModelWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.horizontalLayout.addWidget(self.sceneviewer_widget)

        self.retranslateUi(LungModelWidget)
        QtCore.QMetaObject.connectSlotsByName(LungModelWidget)

    def retranslateUi(self, LungModelWidget):
        LungModelWidget.setWindowTitle(QtGui.QApplication.translate("LungModelWidget", "lungmodel", None, QtGui.QApplication.UnicodeUTF8))
        self.controlPanel_groupBox.setTitle(QtGui.QApplication.translate("LungModelWidget", "Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.lung_groupBox.setTitle(QtGui.QApplication.translate("LungModelWidget", "Lung surface", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLung.setText(QtGui.QApplication.translate("LungModelWidget", "Left lung", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLung.setText(QtGui.QApplication.translate("LungModelWidget", "Right lung", None, QtGui.QApplication.UnicodeUTF8))
        self.airway_groupBox.setTitle(QtGui.QApplication.translate("LungModelWidget", "Grow airway tree!", None, QtGui.QApplication.UnicodeUTF8))
        self.leftAirway.setText(QtGui.QApplication.translate("LungModelWidget", "Left lung", None, QtGui.QApplication.UnicodeUTF8))
        self.rightAirway.setText(QtGui.QApplication.translate("LungModelWidget", "Right lung", None, QtGui.QApplication.UnicodeUTF8))
        self.artery_groupBox.setTitle(QtGui.QApplication.translate("LungModelWidget", "Grow arterial vessels tree!", None, QtGui.QApplication.UnicodeUTF8))
        self.leftArtery.setText(QtGui.QApplication.translate("LungModelWidget", "Left lung", None, QtGui.QApplication.UnicodeUTF8))
        self.rightArtery.setText(QtGui.QApplication.translate("LungModelWidget", "Right lung", None, QtGui.QApplication.UnicodeUTF8))
        self.vein_groupBox.setTitle(QtGui.QApplication.translate("LungModelWidget", "Grow venous vessels tree!", None, QtGui.QApplication.UnicodeUTF8))
        self.rightVein.setText(QtGui.QApplication.translate("LungModelWidget", "Right lung", None, QtGui.QApplication.UnicodeUTF8))
        self.leftVein.setText(QtGui.QApplication.translate("LungModelWidget", "Left lung", None, QtGui.QApplication.UnicodeUTF8))
        self.morphing_groupBox.setTitle(QtGui.QApplication.translate("LungModelWidget", "Morph the lung! ", None, QtGui.QApplication.UnicodeUTF8))
        self.modeFour_label.setText(QtGui.QApplication.translate("LungModelWidget", "Four", None, QtGui.QApplication.UnicodeUTF8))
        self.modeOne_label.setText(QtGui.QApplication.translate("LungModelWidget", "One", None, QtGui.QApplication.UnicodeUTF8))
        self.modeSix_label.setText(QtGui.QApplication.translate("LungModelWidget", "Six", None, QtGui.QApplication.UnicodeUTF8))
        self.modeThree_label.setText(QtGui.QApplication.translate("LungModelWidget", "Three", None, QtGui.QApplication.UnicodeUTF8))
        self.modeFive_label.setText(QtGui.QApplication.translate("LungModelWidget", "Five", None, QtGui.QApplication.UnicodeUTF8))
        self.modeTwo_label.setText(QtGui.QApplication.translate("LungModelWidget", "Two", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_pushButton.setText(QtGui.QApplication.translate("LungModelWidget", "Reset to Average model", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_pushButton.setText(QtGui.QApplication.translate("LungModelWidget", "Exit", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
