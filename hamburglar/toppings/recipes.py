#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.
"""

from .ignorefieldtopping import IgnoreFieldTopping


class RecipesTopping(IgnoreFieldTopping):
    KEY = "recipes"
    IGNORE = ['raw']

    def filter(self, object1, object2):
        changed = {}
        for key in object1:
            if not "name" in object1[key]:
                continue
            if key in object2:
                if not self.equal(object1[key], object2[key]):
                    changed.update({key: [object1[key], object2[key]]})
            else:
                changed.update({key: [object1[key], None]})
        for key in object2:
            if not "name" in object2[key]:
                continue
            if not key in object1:
                changed.update({key: [None, object2[key]]})

        return changed
