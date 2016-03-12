# -*- coding: utf-8 -*-

def template(x,y,z):
    return "%s時の%sは%s" % (str(x),str(y),str(z))

print template(x=12, y="気温", z=22.4)