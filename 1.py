import pyautogui
import time
import os
import threading
import urllib.request
import requests
import json
import random
import datetime
import subprocess


command_list = ['whoami', 'hostname', 'set', 'dir', 'netstat -ano']

#def auto_altman():
zzz = 0
for i in range(1,220):
	t = datetime.datetime.now()
	p = t.strftime('%Y%m%d%H%M%S')
	t_shark_path = 'C:/Wireshark/tshark.exe -i "本地连接" -F "pcap" -w C:/Users/Cainr/Desktop/xd/bx/gsl/' + p + '.pcap tcp and port 3389 and host 192.168.28.153'
	#pcap_result = os.system(t_shark_path)
	pcap_result = subprocess.Popen(t_shark_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	time.sleep(2)
	pyautogui.keyDown('win')
	pyautogui.press('r')
	pyautogui.keyUp('win')
	time.sleep(2)
	pyautogui.moveTo(169, 830, 1)
	pyautogui.click()
	pyautogui.moveTo(922, 377, 1)
	pyautogui.click()
	pyautogui.moveTo(1033, 514, 1)
	pyautogui.click()
	time.sleep(25)
	pyautogui.moveTo(1627, 7, 1)
	pyautogui.click()
	pyautogui.moveTo(1080, 846, 1)
	pyautogui.click()
	pyautogui.write('shell SocksOverRDP-Server.exe',0.2)
	pyautogui.press('enter')
	pyautogui.moveTo(215, 175, 1)
	pyautogui.rightClick()
	pyautogui.moveTo(237, 188, 1)
	pyautogui.click()
	pyautogui.moveTo(306, 110, 1)
	pyautogui.click()
	pyautogui.moveTo(435, 139, 1)
	pyautogui.click()
	time.sleep(10)
	for z in command_list:
		pyautogui.write(z, 0.2)
		pyautogui.PAUSE = 1
		pyautogui.press('enter')
		time.sleep(3)
#time.sleep(20)
	time.sleep(80)
	pyautogui.moveTo(1484, 20, 1)
	pyautogui.click()
	#pyautogui.moveTo(119, 205, 1)
	#pyautogui.rightClick()
	#pyautogui.moveTo(179, 418, 1)
	#pyautogui.click()
	#pyautogui.moveTo(457, 345, 1)
	#pyautogui.click()
	pyautogui.moveTo(1080, 846, 1)
	pyautogui.click()
	pyautogui.write('shell taskkill /IM SocksOverRDP-Server.exe /F',0.2)
	pyautogui.press('enter')
	pyautogui.moveTo(462, 896, 1)
	pyautogui.rightClick()
	pyautogui.moveTo(436, 846, 1)
	pyautogui.click()
	pyautogui.moveTo(944, 519, 1)
	pyautogui.click()
	os.system('taskkill /IM tshark.exe /F')
	print('停止抓包')
	zzz = i + 1
	print(zzz)
	print(zzz)
	print(zzz)
