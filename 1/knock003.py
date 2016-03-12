# coding: utf-8
# -*- coding: utf-8 -*-

import re

s = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

pat = re.compile('[.,]')
print([len(pat.sub('', word)) for word in s.split()])