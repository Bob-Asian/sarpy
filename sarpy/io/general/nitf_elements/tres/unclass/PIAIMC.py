# -*- coding: utf-8 -*-

from ..tre_elements import TREExtension, TREElement

__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


class PIAIMCType(TREElement):
    def __init__(self, value):
        super(PIAIMCType, self).__init__()
        self.add_field('CLOUDCVR', 'd', 3, value)
        self.add_field('SRP', 's', 1, value)
        self.add_field('SENSMODE', 's', 12, value)
        self.add_field('SENSNAME', 's', 18, value)
        self.add_field('SOURCE', 's', 255, value)
        self.add_field('COMGEN', 'd', 2, value)
        self.add_field('SUBQUAL', 's', 1, value)
        self.add_field('PIAMSNNUM', 's', 7, value)
        self.add_field('CAMSPECS', 's', 32, value)
        self.add_field('PROJID', 's', 2, value)
        self.add_field('GENERATION', 'd', 1, value)
        self.add_field('ESD', 's', 1, value)
        self.add_field('OTHERCOND', 's', 2, value)
        self.add_field('MEANGSD', 'd', 7, value)
        self.add_field('IDATUM', 's', 3, value)
        self.add_field('IELLIP', 's', 3, value)
        self.add_field('PREPROC', 's', 2, value)
        self.add_field('IPROJ', 's', 2, value)
        self.add_field('SATTRACK', 'd', 8, value)


class PIAIMC(TREExtension):
    _tag_value = 'PIAIMC'
    _data_type = PIAIMCType
