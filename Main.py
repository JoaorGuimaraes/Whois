import whois
import os

#atualizando o sistema
os.system("apt update && apt upgrade -y")

#instalando a biblioteca python-whois
os.system("pip2 install python-whois")

#limpando a tela
os.system("clear")

dominio = raw_input("Alvo: ")

consulta_whois = whois.whois(dominio)

print consulta_whois.text
