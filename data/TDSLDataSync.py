import json
import os, urllib.request
from TDSL.config import DS_URL

cls_arr = []
DS_data = urllib.request.urlopen(DS_URL).read()


def walk(node, i):
    for key, item in node.items():
        if '-' in key:
            key = key.replace('-', '_')
        if type(item) == dict:
            if item:
                cls_arr.append("\n" + "    " * i + "class " + key + ":")
                walk(item, i + 1)
                for k, v in item.items():
                    if '-' in k:
                        k = k.replace('-', '_')
                    if type(v) == dict:
                        cls_arr.append("\n    " + "    " * i + k + "=" + k + "()")
                    elif type(v) == int or type(v) == float:
                        cls_arr.append("\n    " + "    " * i + k + "=" + str(v) + "")
                    else:
                        if "'" in v:
                            v = v.replace("'", r"\'")
                        if type(v) == str:
                            v = '"{}"'.format(v)
                        print('"{}"'.format(v))
                        cls_arr.append("\n    " + "    " * i + k + "=" + str(v) + "")
            else:
                cls_arr.append("\n" + "    " * i + "class " + key + ":\n    " + "    " * i + "pass")


def createDataClass():
    path = os.path.abspath(__file__)
    pth, _ = os.path.split(path)
    f = open(pth + os.path.sep + 'TDSLData.py', 'w')
    f.write('from TDSL.TDSLType import *\n')
    data = json.loads(DS_data)
    cls_arr.reverse()
    cls_arr.append("class DS(DATA_Base):")
    walk(data, 1)
    for k, v in data.items():
        if '-' in k:
            k = k.replace('-', '_')
        if type(v) == dict:
            cls_arr.append("\n    " + k + "=" + k + "()")
        else:
            if "'" in v:
                v = v.replace("'", r"\'")
            if not isinstance(v, str):
                v = ""
            cls_arr.append("\n    " + k + "='" + v + "'")

    print("Sync data from data service.")
    for i in cls_arr:
        f.write(i)
    f.close()


createDataClass()
