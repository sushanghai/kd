# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree
import xml.dom.minidom

class confFile():
    def loadPath(self):
        global host_
        global port_

        configFilePath = os.path.abspath(os.path.join('config','config.xml'))
        #print("configFile:"+ configFilePath)

        tree = xml.etree.ElementTree.parse(configFilePath)
        #print(tree)
        root = tree.getroot()
        #print(root)

        host_ = root.find("es").get("host")
        #print(host_)
        port_ =root.find("es").get("port")
        #print(port_)
        return  host_,port_
if __name__ == "__main__":
    #confFile.loadPath()
#    confFile().loadPath()
    pass


