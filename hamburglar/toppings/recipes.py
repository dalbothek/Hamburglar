#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.
"""

from .ignorefieldtopping import Topping


class RecipesTopping(Topping):
    KEY = "recipes"

    def filter(self, object1, object2):
        changed = {}

        def make_map(recipes):
                rec_map = {}
                for rec in recipes:
                    key = ""
                    if rec["type"] == "shape":
                        for row in rec["shape"]:
                            for col in row:
                                if ":" in str(col):
                                    key += "x."
                                else:
                                    key += str(col) + "."
                            key += ","
                    else:
                        for item in rec["ingredients"]:
                            if ":" in str(item):
                                key += "x."
                            else:
                                key += str(item) + "."
                    rec_map[key] = rec
                return rec_map

        for id in object1:
            if ":" in id:
                continue

            if id not in object2:
                changed[id] = [object1[id], None]
                continue

            obj = object1[id]
            if isinstance(obj, dict):
                obj = [obj]

            obj2 = make_map(object2[id])
            obj1 = make_map(obj)

            changed1 = []
            changed2 = []

            for key in obj1:
                if key not in obj2:
                    changed1.append(obj1[key])
                    continue
                if not self.equal(obj1[key], obj2[key]):
                    changed1.append(obj1[key])
                    changed2.append(obj2[key])

            for key in obj2:
                if key not in obj1:
                    changed2.append(obj2[key])

            if len(changed1) + len(changed2) != 0:
                changed[id] = [changed1, changed2]

        for id in object2:
            if ":" in id:
                continue

            if id not in object1:
                changed[id] = [None, object2[id]]
                continue

        return changed

    def equal(self, rec1, rec2):
        if rec1["amount"] != rec2["amount"]:
            return False
        if rec1["makes"]["id"] != rec2["makes"]["id"]:
            return False
        if rec1["type"] != rec2["type"]:
            return False
        if rec1["type"] == "shape":
            sh1 = rec1["shape"]
            sh2 = rec2["shape"]
            if len(sh1) != len(sh2):
                return False
            for i in range(len(sh1)):
                if len(sh1[i]) != len(sh2[i]):
                    return False
                for j in range(len(sh1[i])):
                    if (not (":" in str(sh1[i][j]) and
                             ":" in str(sh2[i][j])) and
                        sh1[i][j] != sh2[i][j]):
                        return False
        else:
            i1 = [x["id"] if "id" in x else None for x in rec1["ingredients"]]
            i2 = [x["id"] if "id" in x else None for x in rec2["ingredients"]]
            for item in i1:
                if item not in i2:
                    return False
        return True
