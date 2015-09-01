"""
/***************************************************************************
Name                 : gjko plugin
Description          : Describe me
Date                 : 20/Aug/15 
copyright            : (C) 2015 by Matteo Valdina
email                : matteo.valdina@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "gjko plugin" 
def description():
  return "Describe me"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "2.0"
def classFactory(iface): 
  # load Gjko class from file Gjko
  from Gjko import Gjko 
  return Gjko(iface)
