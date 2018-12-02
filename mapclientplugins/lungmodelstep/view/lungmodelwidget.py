import time

from PySide import QtGui, QtCore

from mapclientplugins.lungmodelstep.view.ui_lungmodelwidget_temp import Ui_LungModelWidget


class LungModelWidget(QtGui.QWidget):

    def __init__(self, model, pcaModelData, parent=None):
        super(LungModelWidget, self).__init__(parent)
        self._logger = model._logger
        self._meshModel = model.getMeshModel()
        self._pcaModel = pcaModelData
        self._modeDict = {
            'modeOne': 0.0,
            'modeTwo': 0.0,
            'modeThree': 0.0,
            'modeFour': 0.0,
            'modeFive': 0.0,
            'modeSix': 0.0,
        }

        self._ui = Ui_LungModelWidget()
        self._ui.setupUi(self)

        self._settings = {'view-parameters': {}}
        self._doneCallback = None

        self._airwayLeftFirstClicked = True
        self._airwayRightFirstClicked = True
        self._arteryLeftFirstClicked = True
        self._arteryRightFirstClicked = True
        self._veinLeftFirstClicked = True
        self._veinRightFirstClicked = True

        self._ui.sceneviewer_widget.setContext(model.getContext())
        self._initialUiState()
        self._makeConnections()

    def _makeConnections(self):
        self._ui.sceneviewer_widget.graphicsInitialized.connect(self._graphicsInitialized)
        self._ui.exit_pushButton.clicked.connect(self._doneClicked)
        self._ui.reset_pushButton.clicked.connect(self._resetClicked)
        """ Left lung """
        self._ui.leftLung_checkBox.clicked.connect(self._leftLungClicked)
        # self._ui.leftlungUpper_checkBox.clicked.connect(self._leftLungUpperClicked)
        # self._ui.leftlungLower_checkBox.clicked.connect(self._leftLungLowerClicked)
        """ Right lung """
        self._ui.rightLung_checkBox.clicked.connect(self._rightLungClicked)
        # self._ui.rightlungUpper_checkBox.clicked.connect(self._rightLungUpperClicked)
        # self._ui.rightlungMiddle_checkBox.clicked.connect(self._rightLungMiddleClicked)
        # self._ui.rightlungLower_checkBox.clicked.connect(self._rightLungLowerClicked)
        """ Airway """
        self._ui.leftAirway_checkBox.clicked.connect(self._leftAirwayClicked)
        self._ui.rightAirway_checkBox.clicked.connect(self._rightAirwayClicked)
        """ Artery """
        self._ui.leftArtery_checkBox.clicked.connect(self._leftArteryClicked)
        self._ui.rightArtery_checkBox.clicked.connect(self._rightArteryClicked)
        """ Vein """
        self._ui.leftVein_checkBox.clicked.connect(self._leftVeinClicked)
        self._ui.rightVein_checkBox.clicked.connect(self._rightVeinClicked)
        """ Modes """
        self._ui.modeOne_doubleSpinBox.valueChanged.connect(self._modeOneChanged)
        self._ui.modeTwo_doubleSpinBox.valueChanged.connect(self._modeTwoChanged)
        self._ui.modeThree_doubleSpinBox.valueChanged.connect(self._modeThreeChanged)
        self._ui.modeFour_doubleSpinBox.valueChanged.connect(self._modeFourChanged)
        self._ui.modeFive_doubleSpinBox.valueChanged.connect(self._modeFiveChanged)
        self._ui.modeSix_doubleSpinBox.valueChanged.connect(self._modeSixeChanged)

    def _doneClicked(self):
        self._doneCallback()

    def _initialUiState(self):
        self._ui.leftLung_checkBox.setChecked(True)
        self._ui.rightLung_checkBox.setChecked(True)
        # self._ui.leftlungUpper_checkBox.setChecked(True)
        # self._ui.leftlungLower_checkBox.setChecked(True)
        # self._ui.rightlungUpper_checkBox.setChecked(True)
        # self._ui.rightlungMiddle_checkBox.setChecked(True)
        # self._ui.rightlungLower_checkBox.setChecked(True)

    def _graphicsInitialized(self):
        sceneViewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneViewer is not None:
            sceneViewer.setLookatParametersNonSkew([1.9, -4.5, 2.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0])
            sceneViewer.setTransparencyMode(sceneViewer.TRANSPARENCY_MODE_SLOW)
            self._viewAll()

    def _viewAll(self):
        if self._ui.sceneviewer_widget.getSceneviewer() is not None:
            self._ui.sceneviewer_widget.viewAll()

    def setSettings(self, settings):
        self._settings.update(settings)

    def getSettings(self):
        eye, look_at, up, angle = self._ui.sceneviewer_widget.getViewParameters()
        self._settings['view-parameters'] = {'eye': eye, 'look_at': look_at, 'up': up, 'angle': angle}
        return self._settings

    def registerDoneCallback(self, done_callback):
        self._doneCallback = done_callback

    def _leftLungClicked(self):
        checkBox = self._ui.leftLung_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displaySurfaceLeft', checkBox)

    def _rightLungClicked(self):
        checkBox = self._ui.rightLung_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displaySurfaceRight', checkBox)

    # def _leftLungUpperClicked(self):
    #     checkBox1 = self._ui.leftlungUpper_checkBox.isChecked()
    #     checkBox2 = self._ui.leftlungLower_checkBox.isChecked()
    #     if checkBox1 and checkBox2:
    #         print("Upper Lobe: ON")
    #         print("Lower Lobe: ON")
    #         self._meshModel.setDisplayObjects('displaySurfacesLeft', True)
    #     elif checkBox1 is False and checkBox2 is True:
    #         print("Upper Lobe: OFF")
    #         print("Upper Lobe: ON")
    #         self._meshModel.setLeftUpperLobeGraphics()
    #
    # def _leftLungLowerClicked(self):
    #     # num = self._logger.getNumberOfMessages()
    #     # print num
    #     # for i in range(0, num):
    #     #     print self._logger.getMessageTextAtIndex(i)
    #     checkBox1 = self._ui.leftlungUpper_checkBox.isChecked()
    #     checkBox2 = self._ui.leftlungLower_checkBox.isChecked()
    #     if checkBox1 and checkBox2:
    #         print("Upper Lobe: ON")
    #         print("Lower Lobe: ON")
    #         self._meshModel.setDisplayObjects('displaySurfacesLeft', True)
    #     elif checkBox1 is True and checkBox2 is False:
    #         print("Upper Lobe: ON")
    #         print("Lower Lobe: OFF")
    #         self._meshModel.setLeftLowerLobeGraphics()

    # def _rightLungUpperClicked(self):
    #     self._meshModel.setDisplayObjects('displaySurfacesRight', self._ui.rightlungUpper_checkBox.isChecked())
    #     self._meshModel.setRightUpperLobeGraphics()
    #
    # def _rightLungMiddleClicked(self):
    #     self._meshModel.setDisplayObjects('displaySurfacesRight', self._ui.rightlungMiddle_checkBox.isChecked())
    #     self._meshModel.setRightMiddleLobeGraphics()
    #
    # def _rightLungLowerClicked(self):
    #     self._meshModel.setDisplayObjects('displaySurfacesRight', self._ui.rightlungLower_checkBox.isChecked())
    #     self._meshModel.setRighttLowerLobeGraphics()

    def _leftAirwayClicked(self):
        self._resetClicked()
        # pausing the time just to pretend as if a real growing is happening.
        # (this will obviously be replace with real growing!)
        if self._airwayLeftFirstClicked:
            time.sleep(3)
            self._airwayLeftFirstClicked = False
        checkBox = self._ui.leftAirway_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displayLAirway', checkBox)
        if self._ui.leftAirway_checkBox.isChecked() or self._ui.rightAirway_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftArtery_checkBox.isChecked() or self._ui.rightArtery_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftVein_checkBox.isChecked() or self._ui.rightVein_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        else:
            self._ui.morphing_groupBox.setEnabled(True)

    def _rightAirwayClicked(self):
        self._resetClicked()
        # pausing the time just to pretend as if a real growing is happening.
        # (this will obviously be replace with real growing!)
        if self._airwayRightFirstClicked:
            time.sleep(3)
            self._airwayRightFirstClicked = False
        checkBox = self._ui.rightAirway_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displayRAirway', checkBox)
        if self._ui.leftAirway_checkBox.isChecked() or self._ui.rightAirway_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftArtery_checkBox.isChecked() or self._ui.rightArtery_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftVein_checkBox.isChecked() or self._ui.rightVein_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        else:
            self._ui.morphing_groupBox.setEnabled(True)

    def _leftArteryClicked(self):
        self._resetClicked()
        # pausing the time just to pretend as if a real growing is happening.
        # (this will obviously be replace with real growing!)
        if self._arteryLeftFirstClicked:
            time.sleep(3)
            self._arteryLeftFirstClicked = False
        checkBox = self._ui.leftArtery_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displayLArtery', checkBox)
        if self._ui.leftArtery_checkBox.isChecked() or self._ui.rightArtery_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftAirway_checkBox.isChecked() or self._ui.rightAirway_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftVein_checkBox.isChecked() or self._ui.rightVein_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        else:
            self._ui.morphing_groupBox.setEnabled(True)

    def _rightArteryClicked(self):
        self._resetClicked()
        # pausing the time just to pretend as if a real growing is happening.
        # (this will obviously be replace with real growing!)
        if self._arteryRightFirstClicked:
            time.sleep(3)
            self._arteryRightFirstClicked = False
        checkBox = self._ui.rightArtery_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displayRArtery', checkBox)
        if self._ui.leftArtery_checkBox.isChecked() or self._ui.rightArtery_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftAirway_checkBox.isChecked() or self._ui.rightAirway_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftVein_checkBox.isChecked() or self._ui.rightVein_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        else:
            self._ui.morphing_groupBox.setEnabled(True)

    def _leftVeinClicked(self):
        self._resetClicked()
        # pausing the time just to pretend as if a real growing is happening.
        # (this will obviously be replace with real growing!)
        if self._veinLeftFirstClicked:
            time.sleep(3)
            self._veinLeftFirstClicked = False
        checkBox = self._ui.leftVein_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displayLVein', checkBox)
        if self._ui.leftVein_checkBox.isChecked() or self._ui.rightVein_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftAirway_checkBox.isChecked() or self._ui.rightAirway_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftArtery_checkBox.isChecked() or self._ui.rightArtery_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        else:
            self._ui.morphing_groupBox.setEnabled(True)

    def _rightVeinClicked(self):
        self._resetClicked()
        # pausing the time just to pretend as if a real growing is happening.
        # (this will obviously be replace with real growing!)
        if self._veinRightFirstClicked:
            time.sleep(3)
            self._veinRightFirstClicked = False
        checkBox = self._ui.rightVein_checkBox.isChecked()
        self._meshModel.setDisplayObjects('displayRVein', checkBox)
        if self._ui.leftVein_checkBox.isChecked() or self._ui.rightVein_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftAirway_checkBox.isChecked() or self._ui.rightAirway_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        elif self._ui.leftArtery_checkBox.isChecked() or self._ui.rightArtery_checkBox.isChecked():
            self._ui.morphing_groupBox.setEnabled(False)
        else:
            self._ui.morphing_groupBox.setEnabled(True)

    def _resetClicked(self):
        self._resetSpinBoxValues()
        self._applyMorphing()

    def _getAverageLung(self):
        return self._pcaModel.averageLung()

    def _getMorphedLung(self):
        weights = [self._modeDict['modeOne'],
                   self._modeDict['modeTwo'],
                   self._modeDict['modeThree'],
                   self._modeDict['modeFour'],
                   self._modeDict['modeFive'],
                   self._modeDict['modeSix']
                   ]
        return self._pcaModel.morph(weights)

    def _modeOneChanged(self, value):
        self._changeMode('modeOne', value)

    def _modeTwoChanged(self, value):
        self._changeMode('modeTwo', value)

    def _modeThreeChanged(self, value):
        self._changeMode('modeThree', value)

    def _modeFourChanged(self, value):
        self._changeMode('modeFour', value)

    def _modeFiveChanged(self, value):
        self._changeMode('modeFive', value)

    def _modeSixeChanged(self, value):
        self._changeMode('modeSix', value)

    def _changeMode(self, mode, value):
        self._modeDict[mode] = value
        self._applyMorphing()

    def _resetSpinBoxValues(self):
        self._ui.modeOne_doubleSpinBox.setValue(0.0)
        self._ui.modeTwo_doubleSpinBox.setValue(0.0)
        self._ui.modeThree_doubleSpinBox.setValue(0.0)
        self._ui.modeFour_doubleSpinBox.setValue(0.0)
        self._ui.modeFive_doubleSpinBox.setValue(0.0)
        self._ui.modeSix_doubleSpinBox.setValue(0.0)
        return

    def _applyMorphing(self):
        leftNodes, rightNodes = self._getMorphedLung()
        self._meshModel.applyMorphing(leftNodes, lung='left')
        self._meshModel.applyMorphing(rightNodes, lung='right')



