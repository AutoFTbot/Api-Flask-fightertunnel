import os,json
from flask import *
import subprocess, random, re,sys
try:
	import speedtest
except:
	os.system("pip3 install speedtest-cli")
std = subprocess.PIPE
app = Flask(__name__)
auth = sys.argv[2]

import math

@app.route("/backend")
def backend():
	return send_file("/usr/bin/backend")

@app.route("/cektr")
def cektr():
	x = subprocess.check_output(f"cat /etc/trojan/.trojan.db | grep '###' | cut -d ' ' -f 2 | nl",shell=True).decode("ascii")
	return x

@app.route("/cekvm")
def cekvm():
	x = subprocess.check_output(f"cat /etc/vmess/.vmess.db | grep '###' | cut -d ' ' -f 2 | nl",shell=True).decode("ascii")
	return x

@app.route("/ceksh")
def ceksh():
	x = subprocess.check_output(f"cat /etc/ssh/.ssh.db | grep '###' | cut -d ' ' -f 2 | nl",shell=True).decode("ascii")
	return x
	
@app.route("/renws")
def renws():
	num = request.args.get("num")
	exp = request.args.get("exp")
	quota = request.args.get("quota")
	limitip = request.args.get("limitip")
	cmd = f'printf "%s\n" "{num}" "{exp}" "{quota}" "{limitip}" | renew-ws'
	x = subprocess.check_output(cmd,shell=True).decode("utf-8")
	return x

@app.route("/rentr")
def rentr():
	num = request.args.get("num")
	exp = request.args.get("exp")
	quota = request.args.get("quota")
	limitip = request.args.get("limitip")
	cmd = f'printf "%s\n" "{num}" "{exp}" "{quota}" "{limitip}" | renew-tr'
	x = subprocess.check_output(cmd,shell=True).decode("utf-8")
	return x

@app.route("/rensh")
def rensh():
	num = request.args.get("num")
	exp = request.args.get("exp")
	cmd = f'printf "%s\n" "{num}" "{exp}"| renew-ssh'
	x = subprocess.check_output(cmd,shell=True).decode("utf-8")
	return x
	
@app.route("/trial-ssh")
def ssshhhh():
	x = subprocess.check_output(f"printf '%s\n' '60' | trial-ssh",shell=True).decode("utf-8")
	print(x)
	user = re.search("trial(.*)\n",x).group().replace('\n',"")
	pw = re.search("Password         : (.*)\n",x).group()
	pw = pw.split(": ")
	return user+":"+pw[1]

@app.route("/trial-ss")
def trlss():
	x = subprocess.check_output(f"printf '%s\n' '60' | trial-ss",shell=True).decode("utf-8")
	a = [x.group() for x in re.finditer("ss://(.*)",x)]
	return a
	
@app.route("/trial-vmess")
def vmmss():
	x = subprocess.check_output(f"printf '%s\n' '60' | trial-ws",shell=True).decode("utf-8")
	a = [x.group() for x in re.finditer("vmess://(.*)",x)]
	return (a)

@app.route("/trial-trojan")
def trltjw():
	x = subprocess.check_output(f"printf '%s\n' '60' | trial-tr",shell=True).decode("utf-8")
	a = [x.group() for x in re.finditer("trojan://(.*)",x)]
	return (a)

@app.route("/trial-vless")
def trlvl():
	x = subprocess.check_output(f"printf '%s\n' '60' | trial-vl",shell=True).decode("utf-8")
	a = [x.group() for x in re.finditer("vless://(.*)",x)]
	return (a)

@app.route("/create-vmess")
def create_vmess():
	user = request.args.get("user")
	exp = request.args.get("exp")
	qu = request.args.get("quota")
	lim = request.args.get("limitip")
	cmd = f"printf '%s\n' '{user}' '{exp}' '{qu}' '{lim}' | add-ws"
	try:
		x = subprocess.check_output(cmd,shell=True).decode("utf-8")
		a = [x.group() for x in re.finditer("vmess://(.*)",x)]
	except:
		return "error"
	else:
		return(a)


@app.route("/adduser/exp")
def add_user_exp():
	u = request.args.get("user")
	p = request.args.get("password")
	exp = request.args.get("exp")
	lim = request.args.get("limitip")
	cmd = f"printf '%s\n' '{u}' '{p}' '{exp}' '{lim}' | add-ssh"
	try:
		x = subprocess.check_output(cmd,shell=True).decode("utf-8")
	except:
		return "error"
	else:
		return "success"

@app.route("/trojan-create")
def create_trojan():
	user = request.args.get("user")
	exp = request.args.get("exp")
	qu = request.args.get("quota")
	lim = request.args.get("limitip")
	cmd = f"printf '%s\n' '{user}' '{exp}' '{qu}' '{lim}' | add-tr"
	try:
		x = subprocess.check_output(cmd,shell=True).decode("utf-8")
		a = [x.group() for x in re.finditer("trojan://(.*)",x)]
	except:
		return "error"
	else:
		return(a)

@app.route("/vless-create")
def create_vless():
	user = request.args.get("user")
	exp = request.args.get("exp")
	qu = request.args.get("quota")
	lim = request.args.get("limitip")
	cmd = f"printf '%s\n' '{user}' '{exp}' '{qu}' '{lim}' | add-vless"
	try:
		x = subprocess.check_output(cmd,shell=True).decode("utf-8")
		a = [x.group() for x in re.finditer("vless://(.*)",x)]
	except:
		return "error"
	else:
		return(a)

@app.route("/shadowsocks-create")
def create_shadowsocks():
	user = request.args.get("user")
	exp = request.args.get("exp")
	qu = request.args.get("quota")
	lim = request.args.get("limitip")
	cmd = f"printf '%s\n' '{user}' '{exp}' '{qu}' '{lim}' | add-ss"
	try:
		x = subprocess.check_output(cmd,shell=True).decode("utf-8")
		a = [x.group() for x in re.finditer("ss://(.*)",x)]
	except:
		return "error"
	else:
		return(a)

#@app.route("/restart")
def restart():
	try:
		subprocess.check_output(f'systemctl restart xray', shell=True)
	except:
		return "error"
	else:
		return "done"
		
#@app.route("/reboot")
def reboot():
	try:
		subprocess.check_output(f'reboot', shell=True)
	except:
		return "error"
	else:
		return "done"
		
#@app.route("/kill")
def kill():
	try:
		subprocess.check_output(f'init 0', shell=True)
	except:
		return "error"
	else:
		return "done"

		
app.run(host=sys.argv[1], port=6969)
