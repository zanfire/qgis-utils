from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry, QgsGeometry
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ..DEFINES import *
from ..util import layer_helper
import pdb

def merge(feature, features_input):
    """
    Merge geometries from features list that touch given feature.
    """
    count = 0
    features_output = [ feature ]
    geom = QgsGeometry(feature.geometry())
    #geom = QgsGeometry.fromPolygon(feature.geometry())
    while True:
        breakloop = True
        for f in features_input:
            if f in features_output:
                continue
            g = f.geometry()
            #if geom.equals(g): 
            #    continue
            if geom.contains(g):
                continue
            if geom.within(g):
                geom = QgsGeometry(g)
                features_output.append(f)
                breakloop = False
                break
            if not geom.disjoint(g) or geom.touches(g) or geom.overlaps(g):
                geom = QgsGeometry(geom.combine(g))
                features_output.append(f)
                breakloop = False
                break
        if breakloop:
            break
    return (geom, features_output)

def get_intersection(g1, g2):
    """
    This function returns a set of QgsGeometry. Each geometry is the intersection of external ring of given geometry. 
    """

    #if len(p1) == 0 or len(p2) == 0:
    #    pyqtRemoveInputHook()
    #    pdb.set_trace()
    result = []
    p1 = g1.asPolygon()
    p2 = g2.asPolygon()
    if len(p1) > 0 and len(p2) > 0:
        r1 = QgsGeometry.fromPolyline(p1[0])
        r2 = QgsGeometry.fromPolyline(p2[0])
        if not r1.equals(r2) and r1.intersects(r2):
            i = r1.intersection(r2)
            result.append(QgsGeometry(i))
    return result
  
def compute_external_wall_surface(index, geometry, features, height):
    """
    Returns the external wall surface.
    """
    ids = index.intersects(geometry.boundingBox())
    common_part = 0
    for i in ids:
        g = features[i].geometry()
        if not g.equals(geometry) and not geometry.disjoint(g):
            intersection_set = get_intersection(g, geometry)
            h = features[i][FIELD_VOLUME_HEIGHT]
            h2 = height
            if h2 <= h:
                h = h2
            for intersection in intersection_set:
                common_part += intersection.length() * h
    return (geometry.length() * height) - common_part
