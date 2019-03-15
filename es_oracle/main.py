# -*- coding: utf-8 -*-
import configPath
import esServer
def main():
    configPath.confFile().loadPath()
    host_ = configPath.confFile().loadPath()[0]
    print(host_)
    port_ = configPath.confFile().loadPath()[1]
    print(port_)
    esServer.ServerA()


if __name__ == "__main__":
    main()



