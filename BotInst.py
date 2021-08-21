#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BotInst.py
#  
#  Copyright 2021 Elizeu Barbosa Abreu
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from time import sleep
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from random import randint

contatos = list(open('contatos.txt', 'r'))
usuario_e_senha = list(open('user_password.txt', 'r'))
contatos_ordem_alfabetica = sorted(contatos)

url = str(input('''ATENÇÃO!!! Certifique-se de seguir todas as regras do sorteio no Instagram!
	***Este programa marca apenas um contato por postagens.
Siga todos os perfils solicitados, curta ou compartilhe a postagem como solicitado.
Certifique-se de que tem os contatos dentro do arquivo 'contatos.txt' (sem o '@' e um contato por linha) e editou o arquivo 'user_password.txt' com usuario e senha do instagram, na primeira e segunda respectivamente
Entre com o link do sorteio no Instagram: '''))

navegador = wb.Chrome()
navegador.get(url)
sleep(randint(10,15))
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()

sleep(randint(3,8))
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usuario_e_senha[0])
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(usuario_e_senha[1])
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
sleep(randint(5,10))
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
sleep(randint(5,10))


while True:
    for contato in contatos_ordem_alfabetica:
        
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys('@'+ contato)
        
        # AQUI É DEFINIDO UM TEMPO ALEATORIO ENTRE 240 E 380 SEGUNDOS ENTRE AS POSTAGENS. ALTERE-O POR CONTA E RISCO! SE DIMINUIR ESTE TEMPO HAVERÁ MAIS COMENTÁRIOS, MAS O INSTA VAI TE BLOQUEAR
        sleep(randint(240,380))
        
