#!/usr/bin/python3

import sys
from auxiliares import procesar_datos, investigar

def main():   
    robo = procesar_datos(sys.argv[1])

    if robo is not None:
        investigar(robo)

if __name__ == "__main__":
    main()