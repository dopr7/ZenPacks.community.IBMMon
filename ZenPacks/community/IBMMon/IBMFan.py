################################################################################
#
# This program is part of the IBMMon Zenpack for Zenoss.
# Copyright (C) 2009, 2010, 2011 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""IBMFan

IBMFan is an abstraction of a fan or probe.

$Id: IBMFan.py,v 1.1 2011/01/07 19:10:17 egor Exp $"""

__version__ = "$Revision: 1.1 $"[11:-2]

from Products.ZenModel.Fan import Fan
from IBMComponent import *

class IBMFan(Fan, IBMComponent):
    """Fan object"""

    threshold = 0
    status = 0

    _properties = Fan._properties + (
                 {'id':'threshold', 'type':'int', 'mode':'w'},
                 {'id':'status', 'type':'int', 'mode':'w'},
                 )

    def state(self):
        return self.statusString()

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates

InitializeClass(IBMFan)
