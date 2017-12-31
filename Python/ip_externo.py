#!/usr/bin/python3.5
#
# Script que mostra o ip externo
# Carlos Carvalho
# 23/05/2017

import requests

r = requests.get('http://checkip.amazonaws.com')
print("#" * 33 )
print("\n")
print("Seu ip externo é: {0}".format(r.text))
print("#" * 33)
