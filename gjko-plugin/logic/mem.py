from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry, QgsGeometry
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ..DEFINES import *
from ..util import layer_helper
import pdb

"""
 Merge geometries from features list that touch geom geometry.
"""
def merge(feature, features_input):
    count = 0
    features_output = [ feature ]
    geom = QgsGeometry(feature.geometry())
    #geom = QgsGeometry.fromPolygon(feature.geometry())
    while True:
        breakloop = True
        for f in features_input:
            if f in features_output:
                continue
            #if geom.equals(g): 
            #    continue
            #if geom.contains(g):
            #    continue
            #if geom.overlaps(g):
            #    continue
            g = f.geometry()
            if geom.within(g):
                geom = QgsGeometry(g)
                features_output.append(f)
                breakloop = False
                break
            if not geom.disjoint(g) or geom.touches(g):
                geom = QgsGeometry(geom.combine(g))
                features_output.append(f)
                breakloop = False
                break
        if breakloop:
            break
    return (geom, features_output)

def update_base_attributes(feature, geometry, features_set):
    #feature.append(QgsFeature(self.energy_layer.pendingFields()))
    feature.setGeometry(geom)
    feature[FIELD_ID_MEM] = feature_raw[FIELD_CATID] + '_' + str(idx)
    feature[FIELD_COMPACT_R] = 0.0
    feature[FIELD_USE] = f[FIELD_TYPE_USAGE]
    feature[FIELD_CODCAT] = f[FIELD_CATID]
    feature[FIELD_ID_EPC] = ''
    for f in features_set:
        feature[FIELD_AREA] += f[FIELD_AREA]
        feature[FIELD_DISP_SURF] += f[FIELD_DISPERSING_SURFACE] # TODO: rename to one field name not two variation of the same

def get_intersection(g1, g2):
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

"""
Compute compact ratio only on a simple volume without adiacent volumes. 
"""
def compute_simple_compact_ratio(inFeature, outFeature):
    # Compute S / V.
    geom = inFeature.geometry()
    base_area = geom.area()
    perimeter = geom.length()
    height = inFeature[FIELD_VOLUME_HEIGHT]
    S = base_area * 2 + perimeter * height 
    V = base_area * height
    SV = S / V
    outFeature[FIELD_CATID] = inFeature[FIELD_CODCAT]
    outFeature[FIELD_AREA] = base_area
    outFeature[FIELD_HEIGHT] = height
    outFeature[FIELD_PERIMETER] = perimeter
    outFeature[FIELD_COMPACT_RATIO] = SV

def compute_multiple_compact_ratio(features):
    total_vol = 0
    total_disp = 0
    for f in features:
        total_vol += f[FIELD_HEIGHT] * f[FIELD_AREA]
        total_disp += f[FIELD_DISPERSING_SURFACE]
    mcr = total_disp / total_vol
    for f in features:
        f[FIELD_MULTIPLE_COMPACT_RATIO] = mcr

def compute_multiple_compact_ratio2(index, sfeatures, features):
    for feature in sfeatures:
        total_vol = 0
        total_disp = 0
        ids = index.intersects(feature.geometry().boundingBox())
        for i in ids:
            f = features[i]
            if not feature.geometry().disjoint(f.geometry()):
                total_vol += f[FIELD_HEIGHT] * f[FIELD_AREA]
                total_disp += f[FIELD_DISPERSING_SURFACE]
        mcr = total_disp / total_vol
        feature[FIELD_COMPACT_R] = mcr

