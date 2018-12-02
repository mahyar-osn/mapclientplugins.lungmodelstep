import os, platform, time

from scaffoldmaker.utils.zinc_utils import *

from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.field import Field
from opencmiss.utils.maths import vectorops
from opencmiss.zinc.status import OK as ZINC_OK

from mapclientplugins.lungmodelstep.fields.nodes import Nodes as LungNodes


class MeshModel(object):

    def __init__(self, regions, materialModule, context):
        self._logger = context.getLogger()

        self._path = self.getPluginPath()

        self._leftRegion = regions['leftRegion']
        self._rightRegion = regions['rightRegion']
        self._leftAirwayRegion = regions['leftAirwayRegion']
        self._rightAirwayRegion = regions['rightAirwayRegion']
        self._leftArteryRegion = regions['leftArteryRegion']
        self._rightArteryRegion = regions['rightArteryRegion']
        self._leftVeinRegion = regions['leftVeinRegion']
        self._rightVeinRegion = regions['rightVeinRegion']

        self._initializeLeftLung()
        self._initializeRightLung()
        self._initializeLeftAirway()
        self._initializeRightAirway()
        self._initializeLeftArtery()
        self._initializeRightArtery()
        self._initializeLeftVein()
        self._initializeRightVein()

        self._leftMesh = None
        self._rightMesh = None

        self._elemGroups = {'leftUpperLobe': (63, 64, 69, 70, 75, 76, 80, 81, 85, 86, 87, 89, 90, 91, 93, 94, 96, 97,
                                              98, 99, 101, 106, 111, 112, 113, 114, 115, 116, 117, 118),
                            'leftLowerLobe': (65, 66, 67, 71, 72, 73, 77, 78, 82, 83, 102, 103, 104, 107, 108, 109,
                                              111, 112, 113, 114, 115, 116, 117, 118),
                            'rightUpperLobe': (23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 55, 56,
                                               57, 58, 59, 60, 61, 62),
                            'rightMiddleLobe': (1, 2, 7, 8, 13, 14, 18, 19, 39, 40, 45, 46, 51, 52, 53, 54, 55, 56, 57,
                                                58),
                            'rightLowerLobe': (3, 4, 5, 6, 9, 10, 11, 12, 15, 16, 17, 20, 21, 22, 41, 42, 43, 44, 47,
                                               48, 49, 50, 51, 52, 53, 54, 59, 60, 61, 62)}

        self._materialModule = materialModule
        # self._settings = {'leftUpperLobe': True,
        #                   'leftLowerLobe': True,
        #                   'rightUpperLobe': True,
        #                   'rightMiddleLobe': True,
        #                   'rightLowerLobe': True,
        #                   'displaySurfaceLeft': True,
        #                   'displaySurfaceRight': True,
        #                   'displayLAirway': False,
        #                   'displayRAirway': False,
        #                   'displayLArtery': False,
        #                   'displayRArtery': False,
        #                   'displayLVein': False,
        #                   'displayRVein': False}
        self._settings = {'displaySurfaceLeft': True,
                          'displaySurfaceRight': True,
                          'displayLAirway': False,
                          'displayRAirway': False,
                          'displayLArtery': False,
                          'displayRArtery': False,
                          'displayLVein': False,
                          'displayRVein': False}

        self._generateMesh()
        self._generateLeftAirway()
        self._generateRightAirway()
        self._generateLeftArtery()
        self._generateRightArtery()
        self._generateLeftVein()
        self._generateRightVein()

        self._nodes = LungNodes()

    def _getVisibility(self, graphicsName):
        return self._settings[graphicsName]

    def _setVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        if 'displaySurfaceLeft' in graphicsName:
            graphics = self._leftRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'displaySurfaceRight' in graphicsName:
            graphics = self._rightRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'LAirway' in graphicsName:
            graphics = self._leftAirwayRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'RAirway' in graphicsName:
            graphics = self._rightAirwayRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'LAirway' in graphicsName:
            graphics = self._leftArteryRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'LArtery' in graphicsName:
            graphics = self._leftArteryRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'RArtery' in graphicsName:
            graphics = self._rightArteryRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'LVein' in graphicsName:
            graphics = self._leftVeinRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)
        if 'RVein' in graphicsName:
            graphics = self._rightVeinRegion.getScene().findGraphicsByName(graphicsName)
            graphics.setVisibilityFlag(show)

    def _initializeLeftLung(self):
        self._initializeNodeAndElem('left_average', self._leftRegion)

    def _initializeRightLung(self):
        self._initializeNodeAndElem('right_average', self._rightRegion)

    def _initializeLeftAirway(self):
        self._initializeNodeAndElem('left_airway', self._leftAirwayRegion)

    def _initializeRightAirway(self):
        self._initializeNodeAndElem('right_airway', self._rightAirwayRegion)

    def _initializeLeftArtery(self):
        self._initializeNodeAndElem('left_artery', self._leftArteryRegion)

    def _initializeRightArtery(self):
        self._initializeNodeAndElem('right_artery', self._rightArteryRegion)

    def _initializeLeftVein(self):
        self._initializeNodeAndElem('left_vein', self._leftVeinRegion)

    def _initializeRightVein(self):
        self._initializeNodeAndElem('right_vein', self._rightVeinRegion)

    def _initializeNodeAndElem(self, filename, region):
        nodefile = filename+'.exnode'
        elemfile = filename+'.exelem'
        if platform.system() == 'Windows':
            region.readFile(os.path.join('../', self._path, 'fields', nodefile).replace("\\","/"))
            region.readFile(os.path.join('../', self._path, 'fields', elemfile).replace("\\","/"))
        else:
            region.readFile(os.path.join('../', self._path, 'fields', nodefile))
            region.readFile(os.path.join('../', self._path, 'fields', elemfile))

    def _generateMesh(self):
        """ Left Lung """
        self._leftScene = self._leftRegion.getScene()
        fmLeft = self._leftRegion.getFieldmodule()
        fmLeft.beginChange()
        self._leftCoordinates = fmLeft.findFieldByName('coordinates')
        self._leftMagnitude = fmLeft.createFieldMagnitude(self._leftCoordinates)
        self._leftMagnitude.setName('leftmag')
        self._leftMagnitude.setManaged(True)
        """ Create upper and lower lobe groups """
        # self._leftUpperLobe, self._leftUpperLobeMeshGroup = self._creteLobeGroup(fmLeft, 'leftUpperLobe')
        # self._leftlowerLobe, self._leftlowerLobeMeshGroup = self._creteLobeGroup(fmLeft, 'leftLowerLobe')
        fmLeft.endChange()

        """ Right Lung """
        self._rightScene = self._rightRegion.getScene()
        fmRight = self._rightRegion.getFieldmodule()
        fmRight.beginChange()
        self._rightCoordinates = fmRight.findFieldByName('coordinates')
        self._rightMagnitude = fmRight.createFieldMagnitude(self._rightCoordinates)
        self._rightMagnitude.setName('rightmag')
        self._rightMagnitude.setManaged(True)
        """ Create upper and lower lobe groups """
        # self._rightUpperLobe = self._creteLobeGroup(fmRight, 'rightUpperLobe')
        # self._rightMiddleLobe = self._creteLobeGroup(fmRight, 'rightMiddleLobe')
        # self._rightLowerLobe = self._creteLobeGroup(fmRight, 'rightLowerLobe')
        fmRight.endChange()
        self._setupScene(self._leftRegion, self._rightRegion)

    def _generateLeftAirway(self):
        """ Left Airway """
        self._leftAirwayScene = self._leftAirwayRegion.getScene()
        fmLeftAirway = self._leftAirwayRegion.getFieldmodule()
        fmLeftAirway.beginChange()
        self._leftAirwayCoordinates = fmLeftAirway.findFieldByName('coordinates')
        self._leftAirwayMagnitude = fmLeftAirway.createFieldMagnitude(self._leftAirwayCoordinates)
        self._leftAirwayMagnitude.setName('leftairwaymag')
        self._leftAirwayMagnitude.setManaged(True)
        fmLeftAirway.endChange()
        leftAirwayScene = self._createScene(self._leftAirwayRegion)
        leftAirwayScene.beginChange()
        line = self._createLineGraphics(leftAirwayScene, self._leftAirwayCoordinates, 'displayLAirway', 'airway')
        line.setRenderLineWidth(2)
        leftAirwayScene.endChange()
        graphics = self._leftAirwayRegion.getScene().findGraphicsByName('displayLAirway')
        graphics.setVisibilityFlag(self._settings['displayLAirway'])

    def _generateRightAirway(self):
        """ Right Airway """
        self._rightAirwayScene = self._rightAirwayRegion.getScene()
        fmRightAirway = self._rightAirwayRegion.getFieldmodule()
        fmRightAirway.beginChange()
        self._rightAirwayCoordinates = fmRightAirway.findFieldByName('coordinates')
        self._rightAirwayMagnitude = fmRightAirway.createFieldMagnitude(self._rightAirwayCoordinates)
        self._rightAirwayMagnitude.setName('rightairwaymag')
        self._rightAirwayMagnitude.setManaged(True)
        fmRightAirway.endChange()
        rightAirwayScene = self._createScene(self._rightAirwayRegion)
        rightAirwayScene.beginChange()
        line = self._createLineGraphics(rightAirwayScene, self._rightAirwayCoordinates, 'displayRAirway', 'airway')
        line.setRenderLineWidth(2)
        rightAirwayScene.endChange()
        graphics = self._rightAirwayRegion.getScene().findGraphicsByName('displayRAirway')
        graphics.setVisibilityFlag(self._settings['displayRAirway'])

    def _generateLeftArtery(self):
        """ Left Artery """
        self._leftArteryScene = self._leftArteryRegion.getScene()
        fmLeftArtery = self._leftArteryRegion.getFieldmodule()
        fmLeftArtery.beginChange()
        self._leftArteryCoordinates = fmLeftArtery.findFieldByName('coordinates')
        self._leftArteryMagnitude = fmLeftArtery.createFieldMagnitude(self._leftArteryCoordinates)
        self._leftArteryMagnitude.setName('leftarterymag')
        self._leftArteryMagnitude.setManaged(True)
        fmLeftArtery.endChange()
        leftArteryScene = self._createScene(self._leftArteryRegion)
        leftArteryScene.beginChange()
        line = self._createLineGraphics(leftArteryScene, self._leftArteryCoordinates, 'displayLArtery', 'red')
        line.setRenderLineWidth(2)
        leftArteryScene.endChange()
        graphics = self._leftArteryRegion.getScene().findGraphicsByName('displayLArtery')
        graphics.setVisibilityFlag(self._settings['displayLArtery'])

    def _generateRightArtery(self):
        """ Right Artery """
        self._rightArteryScene = self._rightArteryRegion.getScene()
        fmRightArtery = self._rightArteryRegion.getFieldmodule()
        fmRightArtery.beginChange()
        self._rightArteryCoordinates = fmRightArtery.findFieldByName('coordinates')
        self._rightArteryMagnitude = fmRightArtery.createFieldMagnitude(self._rightArteryCoordinates)
        self._rightArteryMagnitude.setName('rightarterymag')
        self._rightArteryMagnitude.setManaged(True)
        fmRightArtery.endChange()
        rightArteryScene = self._createScene(self._rightArteryRegion)
        rightArteryScene.beginChange()
        line = self._createLineGraphics(rightArteryScene, self._rightArteryCoordinates, 'displayRArtery', 'red')
        line.setRenderLineWidth(2)
        rightArteryScene.endChange()
        graphics = self._rightArteryRegion.getScene().findGraphicsByName('displayRArtery')
        graphics.setVisibilityFlag(self._settings['displayRArtery'])

    def _generateLeftVein(self):
        """ Left Vein """
        self._leftVeinScene = self._leftVeinRegion.getScene()
        fmLeftVein = self._leftVeinRegion.getFieldmodule()
        fmLeftVein.beginChange()
        self._leftVeinCoordinates = fmLeftVein.findFieldByName('coordinates')
        self._leftVeinMagnitude = fmLeftVein.createFieldMagnitude(self._leftVeinCoordinates)
        self._leftVeinMagnitude.setName('leftveinmag')
        self._leftVeinMagnitude.setManaged(True)
        fmLeftVein.endChange()
        leftVeinScene = self._createScene(self._leftVeinRegion)
        leftVeinScene.beginChange()
        line = self._createLineGraphics(leftVeinScene, self._leftVeinCoordinates, 'displayLVein', 'blue')
        line.setRenderLineWidth(2)
        leftVeinScene.endChange()
        graphics = self._leftVeinRegion.getScene().findGraphicsByName('displayLVein')
        graphics.setVisibilityFlag(self._settings['displayLVein'])

    def _generateRightVein(self):
        """ Right Vein """
        self._rightVeinScene = self._rightVeinRegion.getScene()
        fmRightVein = self._rightVeinRegion.getFieldmodule()
        fmRightVein.beginChange()
        self._rightVeinCoordinates = fmRightVein.findFieldByName('coordinates')
        self._rightVeinMagnitude = fmRightVein.createFieldMagnitude(self._rightVeinCoordinates)
        self._rightVeinMagnitude.setName('rightveinmag')
        self._rightVeinMagnitude.setManaged(True)
        fmRightVein.endChange()
        rightVeinScene = self._createScene(self._rightVeinRegion)
        rightVeinScene.beginChange()
        line = self._createLineGraphics(rightVeinScene, self._rightVeinCoordinates, 'displayRVein', 'blue')
        line.setRenderLineWidth(2)
        rightVeinScene.endChange()
        graphics = self._rightVeinRegion.getScene().findGraphicsByName('displayRVein')
        graphics.setVisibilityFlag(self._settings['displayRVein'])

    def _creteLobeGroup(self, fm, name):
        mesh = fm.findMeshByDimension(2)
        group = self._createFieldGroup(fm, name)
        elemGroup = self._createElementGroup(group, mesh)
        meshGroup = elemGroup.getMeshGroup()
        self._addSubElements(group)
        el_iter = mesh.createElementiterator()
        element = el_iter.next()
        while element.isValid():
            if element.getIdentifier() in self._elemGroups[name]:
                meshGroup.addElement(element)
            element = el_iter.next()
        return group, meshGroup

    def _createFieldGroup(self, fm, name):
        field = fm.findFieldByName(name)
        if field.isValid():
            group = field.castGroup()
            assert group.isValid(), 'Existing non-group field called ' + name
        else:
            group = fm.createFieldGroup()
            group.setName(name)
            group.setManaged(True)
        return group

    def _createElementGroup(self, grp, mesh):
        elementGroup = grp.getFieldElementGroup(mesh)
        if not elementGroup.isValid():
            elementGroup = grp.createFieldElementGroup(mesh)
        return elementGroup

    def _addSubElements(self, grp):
        from opencmiss.zinc.field import FieldGroup

        grp.setSubelementHandlingMode(FieldGroup.SUBELEMENT_HANDLING_MODE_FULL)
        fm = grp.getFieldmodule()
        for dimension in range(1, 3):
            mesh = fm.findMeshByDimension(dimension)
            elementGroup = grp.getFieldElementGroup(mesh)
            if elementGroup.isValid():
                meshGroup = elementGroup.getMeshGroup()
                meshGroup.addElementsConditional(elementGroup)
        return None

    def _setupScene(self, leftregion, rightregion):
        """ Left Lung"""
        leftScene = self._createScene(leftregion)
        leftScene.beginChange()
        line = self._createLineGraphics(leftScene, self._leftCoordinates, 'displayLinesLeft', 'transTissue')
        line.setRenderLineWidth(2.5)
        self._surfaceLeft = self._createSurfaceGraphics(leftScene, self._leftCoordinates, 'displaySurfaceLeft', 'solidTissue')
        leftScene.endChange()

        """ Right Lung"""
        rightScene = self._createScene(rightregion)
        rightScene.beginChange()
        line = self._createLineGraphics(rightScene, self._rightCoordinates, 'displayLinesRight', 'transTissue')
        line.setRenderLineWidth(2.5)
        self._surfaceRight = self._createSurfaceGraphics(rightScene, self._rightCoordinates, 'displaySurfaceRight', 'solidTissue')
        rightScene.endChange()

    def _createScene(self, region):
        return self.getScene(region)

    def _createLineGraphics(self, scene, coordinates, name, color):
        materialModule = self._materialModule
        lines = scene.createGraphicsLines()
        lines.setCoordinateField(coordinates)
        lines.setName(name)
        black = materialModule.findMaterialByName(color)
        lines.setMaterial(black)
        return lines

    def _createSurfaceGraphics(self, scene, coordinates, name, color):
        surface = scene.createGraphicsSurfaces()
        surface.setCoordinateField(coordinates)
        surface.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
        surfacesMaterial = self._materialModule.findMaterialByName(color)
        surface.setMaterial(surfacesMaterial)
        surface.setName(name)
        surface.setVisibilityFlag(self.isDisplaySurfaces(name))
        return surface

    # def setLeftUpperLobeGraphics(self):
    #     self._surfaceLeft.setSubgroupField(self._leftlowerLobe)
    #
    # def setLeftLowerLobeGraphics(self):
    #     self._surfaceLeft.setSubgroupField(self._leftUpperLobe)
    #
    # def setRightUpperLobeGraphics(self):
    #     self._surfaceRight.setSubgroupField(self._rightMiddleLobe)
    #     self._surfaceRight.setSubgroupField(self._rightLowerLobe)
    #
    # def setRightMiddleLobeGraphics(self):
    #     self._surfaceRight.setSubgroupField(self._rightUpperLobe)
    #     self._surfaceRight.setSubgroupField(self._rightLowerLobe)
    #
    # def setRighttLowerLobeGraphics(self):
    #     self._surfaceRight.setSubgroupField(self._rightUpperLobe)
    #     self._surfaceRight.setSubgroupField(self._rightMiddleLobe)

    @staticmethod
    def getScene(region):
        return region.getScene()

    @staticmethod
    def getPluginPath():
        if platform.system() == 'Windows':
            return '/'.join(__file__.split('\\')[:-2])
        else:
            return '/'.join(__file__.split('/')[1:-2])

    def isDisplaySurfaces(self, surfaceName):
        return self._getVisibility(surfaceName)

    def setDisplayObjects(self, surfaceName, show):
        self._setVisibility(surfaceName, show)

    def applyMorphing(self, nodeArray, lung=None):
        self._setNodeParameter(nodeArray, lung=lung)

    def _setNodeParameter(self, nodeArray, lung):
        fieldmodule = self._leftRegion.getFieldmodule() if lung == 'left' else self._rightRegion.getFieldmodule() if 'right' == lung else Exception(
            "Region invalid!")
        if lung == 'left' and nodeArray.shape[0] != 99:
            raise Exception("Lung and node array do not match!")
        elif lung == 'right' and nodeArray.shape[0] != 126:
            raise Exception("Lung and node array do not match!")

        nodes = self._getLeftNodeField() if lung == 'left' else self._getRightNodeField()
        cache = fieldmodule.createFieldcache()
        coordinates = getOrCreateCoordinateField(fieldmodule)
        nodeIndex = self._getLeftNodeIndex() if lung == 'left' else self._getRightNodeIndex()

        fieldmodule.beginChange()
        node_iter = nodes.createNodeiterator()
        node = node_iter.next()

        for n in range(nodeArray.shape[0]):

            if "." not in nodeIndex[n]:
                nodeID = int(nodeIndex[n])
                nodeVersion = 1
            else:
                nodeID = int(nodeIndex[n].split('.')[0])
                nodeVersion = int(nodeIndex[n].split('.')[1])

            if node.getIdentifier() == nodeID:
                pass
            else:
                node = node_iter.next()

            cache.setNode(node)
            resultList = list()
            """ setting the node xyz coordinates """
            rx = coordinates.setNodeParameters(cache, 1, Node.VALUE_LABEL_VALUE, nodeVersion, nodeArray[n, 0, 0])
            ry = coordinates.setNodeParameters(cache, 2, Node.VALUE_LABEL_VALUE, nodeVersion, nodeArray[n, 1, 0])
            rz = coordinates.setNodeParameters(cache, 3, Node.VALUE_LABEL_VALUE, nodeVersion, nodeArray[n, 2, 0])
            """ setting the nodal x derivatives """
            rxds1 = coordinates.setNodeParameters(cache, 1, Node.VALUE_LABEL_D_DS1, nodeVersion, nodeArray[n, 0, 1])
            rxds2 = coordinates.setNodeParameters(cache, 1, Node.VALUE_LABEL_D_DS2, nodeVersion, nodeArray[n, 0, 2])
            rxds12 = coordinates.setNodeParameters(cache, 1, Node.VALUE_LABEL_D2_DS1DS2, nodeVersion,
                                                   nodeArray[n, 0, 3])
            """ setting the nodal y derivatives """
            ryds1 = coordinates.setNodeParameters(cache, 2, Node.VALUE_LABEL_D_DS1, nodeVersion, nodeArray[n, 1, 1])
            ryds2 = coordinates.setNodeParameters(cache, 2, Node.VALUE_LABEL_D_DS2, nodeVersion, nodeArray[n, 1, 2])
            ryds12 = coordinates.setNodeParameters(cache, 2, Node.VALUE_LABEL_D2_DS1DS2, nodeVersion,
                                                   nodeArray[n, 1, 3])
            """ setting the nodal z derivatives """
            rzds1 = coordinates.setNodeParameters(cache, 3, Node.VALUE_LABEL_D_DS1, nodeVersion, nodeArray[n, 2, 1])
            rzds2 = coordinates.setNodeParameters(cache, 3, Node.VALUE_LABEL_D_DS2, nodeVersion, nodeArray[n, 2, 2])
            rzds12 = coordinates.setNodeParameters(cache, 3, Node.VALUE_LABEL_D2_DS1DS2, nodeVersion,
                                                   nodeArray[n, 2, 3])
            resultList.append(rx);
            resultList.append(ry);
            resultList.append(rz);
            resultList.append(rxds1);
            resultList.append(rxds2);
            resultList.append(rxds12);
            resultList.append(ryds1);
            resultList.append(ryds2);
            resultList.append(ryds12);
            resultList.append(rzds1);
            resultList.append(rzds2);
            resultList.append(rzds12);

            for result in resultList:
                if result == ZINC_OK:
                    pass
                else:
                    print("ZINC NOT OK!")
                    print("NODE: {}".format(nodeID))
                    break

        fieldmodule.endChange()
        del fieldmodule;
        del cache;
        del node;
        del coordinates
        return None

    def _getLeftNodeField(self):
        fieldmodule = self._leftRegion.getFieldmodule()
        nodes = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        return nodes

    def _getRightNodeField(self):
        fieldmodule = self._rightRegion.getFieldmodule()
        nodes = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        return nodes

    def _getLeftNodeIndex(self):
        return self._nodes.setNode(lung='left')

    def _getRightNodeIndex(self):
        return self._nodes.setNode(lung='right')
