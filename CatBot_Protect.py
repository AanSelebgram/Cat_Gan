# -*- coding: utf-8 -*-
#Cat_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,ast,os,subprocess,wikipedia,goslate
import bs4
import ast
import requests,json,urllib
import html5lib
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS

cl = LINETCR.LINE()
cl.login(token='EmHCNHLKXReR3GUduca1.UlrDCGkj7dxSpRrrWVSpKq.g3vEaSk5iGVvPWOhpgRVkHPpLhOOwoso1OQ5i+27Iuw=')
#cl.login(token='')
cl.loginResult()
print "Cl-Login Success\n"

ki = LINETCR.LINE()
ki.login(token='EmzlLew0XTW8IODPhwRe.7oUShdLcs9TUvO5sMkXNpG.ilwEXwSYByrqIwZgDLnuJ97XA1wVn16Z8shYnSsButY')
#ki.login(token='')
ki.loginResult()
print "Ki-Login Success\n"

kk = LINETCR.LINE()
kk.login(token='EmwVS4A5cErcj6NZ939e.uHwIvq3v1iyKQZqnNrhKFG.vllaB0gxYptn8mEr+F0b1/+TSN46FCfTV5Qtm/fEXig=')
#kk.login(token='')
kk.loginResult()
print "Kk-Login Success\n"

kc = LINETCR.LINE()
kc.login(token='Em8Uj1MRqCDmBO5XiYu5.T2Obu6kd2POuq9/WqXGtnq.Eaqof4oV8GKOTFkpRESnEuh0odD3CEpkOVmeKezp3N0=')
#kc.login(token='')
kc.loginResult()
print "Kc-Login Success\n"

kr = LINETCR.LINE()
kr.login(token='EmLV5twOWfR6ybWCUO0b.sDTrH/zMSMOdJJyRwe3qQW.eJvaeOQigQYb4ukESxrJdzaTHRe1I9LExmgCz5WfzJ4=')
#kr.login(token='')
kr.loginResult()
print "Kr-Login Success\n\n=====[Sukses All Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
========『Aan Jutawan』========

『Comand In Group』
☔Creator
☔Gcreator
☔Ginfo
☔Gift/ All gift
☔Kick: (mid)
☔Invite: (mid)
☔Listgroup
☔Gurl
☔Cancelall
☔Absen
☔Add all
☔Recover
☔Speed
☔Ban @
☔Banlist
☔Unban @
☔Gn: (NamaGroup)
☔Url:on / off
☔Qr:on / off
☔Autokick:on / off
☔Autocancel:on / off

『For Creator』
🔬Tagall
🔬Nk: @
🔬Boom @
🔬Bye all
🔬@Bye
🔬Bc: text
🔬Kill ban
🔬Set member: 
🔬Ban group: 
🔬Join group:
🔬Leave group:
🔬Leave all group
🔬Auto join:on / off
🔬All join / (Cb1/2/3 join)

『Spesial Comand』
🛡Apakah
🛡Quote
🛡Translate
🛡runtime
🛡Kalender
🛡Cek contoh>>> Cek 05-03-2003
🛡Mid @
🛡Bye @
🛡Dj @
🛡wikipedia
🛡Teman all
🛡Teman
🛡Flist
🛡.Say
🛡Mode on
🛡Mimic on/off
🛡Target @
🛡Target del @
🛡Target list
🛡Copy @
🛡Mycopy @
🛡Sampul @
🛡Pp @
🛡cover @
🛡Mentionall
🛡Mybackup
🛡Salam1/Salam2
🛡Setlastpoint
🛡Viewlastseen
🛡.istagram >>>namanya
🛡/ig >>> namanya
🛡/lirik
🛡/youtube
🛡lyric
🛡Youtube:
🛡music
🛡Getname @
🛡Midpict
🛡Hack
🛡kedapkedip
🛡.reboot


Owner Team Boruto Bot 『AanJutawan』
"""

KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid]
Creator="ub76a0153a283da9a1443dfb043181335"
admin=["ub76a0153a283da9a1443dfb043181335","ube597dd17603406a6b278bc62cc5fdcf"]

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "Members":1,
    "AutoCancel":True,
    "AutoKick":True,
    "blacklist":{},
    "teman":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":True,
    "Timeline":True,
    "Contact":True,
    "lang":"JP",
    "BlGroup":{}

}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


def mention(to, nama):
	aa = ""
	bb = ""
	strt = int(0)
	akh = int(0)
	nm = nama
	print nm
	for mm in nm:
		akh = akh + 3
		aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M","""+json.dumps(mm)+"),"""
		strt = strt + 4
		akh = akh + 1
		bb += "@x \n"
	aa = (aa[:int(len(aa)-1)])
	msg = Message()
	msg.to = to
	msg.from_ = admin
	msg.text = bb
	msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
	print msg
	try:
		cl.sendMessage(msg)
	except Exception as error:
            print error
		
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
mulai = time.time()


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)


def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Bmid:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"Ketik 'Help' untuk bantuan\n\nHarap gunakan dengan bijak!")
                else:
		    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"Ketik 'Help' untuk bantuan\n\nHarap gunakan dengan bijak!")
		    else:
                        cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Bots:
			    pass
		        if op.param2 in Bots:
			    pass
		        else:
		            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
			    kk.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass

#-----------------------------------------------------------------
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#--------------------------------------------------------
                if Creator in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Bots:
		    pass
		else:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti) #kicker join
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    kr.kickoutFromGroup(msg.to,[op.param2])
                    kr.leaveGroup(msg.to)
            else:
                pass
#--------------------------RECEIVE_MESSAGE---------------------------
        if op.type == 26:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            ki.sendText(msg.to,"already")
                            kk.sendText(msg.to,"already")
                            kc.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            ki.sendText(msg.to,"aded")
                            kk.sendText(msg.to,"aded")
                            kc.sendText(msg.to,"aded")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
#--------------------------------------------------------
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))


#--------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Bikin BOT")
#--------------------------------------------------------
            elif msg.text in ["Creator gw"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                jawab = ("This is my Creator","My creator is handsome","My creator is cool")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
#--------------------------------------------------------
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#--------------------------------- TRANSLATE ------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#---------------------------------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
            elif "/lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"
            elif "/lagu " in msg.text.lower():
                songname = msg.text.replace("/lagu ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendAudioWithURL(msg.to,song[3])
                    print "[Command] Lagu"
            elif "/youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#-------------------------------------------------------
            elif msg.text.lower() == '.reboot':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif ("Hack " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mi = cl.getContact(key1)
                cl.sendText(msg.to,"Mid:" +  key1)
#-------------------------------------------------------
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif msg.text in ["Backup:on","Backup on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Reject"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
#--------------------------------------------------
            elif "Sampul @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Sampul @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#--------------------------------------------------
            elif "Midpict " in msg.text:
                umid = msg.text.replace("Midpict ","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#-------------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi"," Capek aku pantek!")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-------------------------------------------------
            
#-------------------------------------------------
            elif msg.text in ["Mimic on","mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
#--------------------------------------------------
            elif msg.text in ["Mimic off","mimic:off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)
            elif "Mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#-------------------------------------------------
            elif msg.text in ["Clear ban"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
#-------------------------------------------------
            elif msg.text in ["Mentionall"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    name = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in name:
                       akh = akh + int(5)
                       cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                       strt = strt + int(6)
                       akh = akh + 1
                       cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
#--------------------------------------------------
            elif "Ambilkan " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Ambilkan ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")


#--------------------------------------------------------
            elif "v10" in msg.text:
                cl.sendText(msg.to,"""
คำสั่งบอท siri
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่มไรแบบนี้• บอทจะไม่เตะเเอทมินทุกกรณี
มีตั้งเเต่ชุดบอท 12-37 บอท
ชุดล๊อกห้อง
ล๊อกกันรันสติ๊กเกอร์
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม
Set:changenamelock:on

ล๊อกการเชิญของสมาชิก
Set:blockinvite:on

ล๊อกแอทมินกลุ่ม
Set:ownerlock:on

ล๊อกรูปกลุ่ม
Set:iconlock:on

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeowner
เปลี่ยนเจ้าของห้องสั่งแล้วส่งคอลแทคคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มสั่งแล้วส่งคอลแทคคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งคอลแทคคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl         เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite  ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คเจ้าของบ้านตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คเจ้าของบ้านคนสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeextraowner
เพิ่มเจ้าของบ้านคนที2หรือเรียกคนสำรองสั่งแล้วส่งคอลแทคคนที่จะเป็นคนสำรองลงในกลุ่ม

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:turncreator

สลับให้เจ้าของบ้านคนที่2เป็นตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

ดูคนอ่าน

สั่งตั้งค่าก่อนแล้วค่อยสั่งอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen   สั่งอ่าน
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

สนใจติดต่อที่

ทราย
http://line.me/ti/p/~bot_botv13
0902853778
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
""")
            elif "Getname @" in msg.text:
                 _name = msg.text.replace("Getname @","")
                 _nametarget = _name.rstrip(" ")
                 gs = cl.getGroup(msg.to)
                 for h in gs.members:
                   if _nametarget == h.displayName:
                      cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                   else:
                     pass
#----------------------------------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    ki.cloneContactProfile(target)
                                    kk.cloneContactProfile(target)
                                    kc.cloneContactProfile(target)
                                except:
				       cl.sendText(msg.to," Sudah Astro")
#------------------------------------------------
            elif "Steal dp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                        print "[Command]dp executed"
#--------------------------------------------------------
            elif msg.text in ["Salam1"]:
                ki.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Assalamu'alaikum")
#--------------------------------------------
            elif msg.text in ["Salam2"]:
                ki.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif msg.text in ["Quote","quote","quotes","Quotes"]:
                quote = ['Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut\n\nQuote By Ari.','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL.\n\nQuote By Ari.','Sebaik-baik orang memberi lebih baik ditabung\n\nQuote By Ari.','Lebih baik tangan diatas dari pada tangan di dalam celana\n\nQuote By Ari.','Pantang pulang sebelum goyang\n\nIni Bukan Quote.']
                psn = random.choice(quote)
                cl.sendText(msg.to,psn)
#-------------------------------------------------------
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#--------------------------------------------------------
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
#--------------------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("iya","Tidak")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
#--------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#----------------------------------------------------
            elif ".Say- " in msg.text:
                say = msg.text.replace(".Say- ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#--------------------------------------------------------
            elif msg.text in ["Kalender"]:
	    	      wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	              cl.sendText(msg.to, "         KALENDER\n\n" + (wait2['setTime'][msg.to]))
#--------------------------------------------------------
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#--------------------------------------------------------
            elif msg.text in ["Key","help","Help"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,helpMessage)
#--------------------------------------------------------
            elif "Teman all" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Teman]ok"
                        _name = msg.text.replace("Teman all","")
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
			gs = kr.getGroup(msg.to)
                        cl.sendText(msg.to,"oke")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                                if targets == []:
                                    ki.sendText(msg.to,"Tidak Ada Boss Yuda")
                                else:
                                    for target in targets:
                                        try:
                                            wait["teman"][target] = True
                                            f=codecs.open('teman.json','w','utf-8')
                                            json.dump(wait["teman"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        except:
                                            ki.sendText(msg.to,"Error")
#------------------------------------------------------
            elif "Teman " in msg.text:
                gName = msg.text.replace("Teman ","")
                for semua in wait["teman"]:
                    cl.createGroup(gName, semua)
#------------------------------------------------------
            elif msg.text in ["Flist"]:
                if msg.from_ in admin:
                    if wait["teman"] == {}:
                        cl.sendText(msg.to,"nothing")
                    else:
                        cl.sendText(msg.to,"Ini list teman kita")
                        mc = ""
                        for mi_d in wait["teman"]:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)
#-------------------------------------------------------
            elif msg.text in ["Allprotect on","Mode on"]:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
                    else:
                        jawab = ("PROTECTION SET TO ON","Warning protection on danger for you")
                        jawaban = random.choice(jawab)
                        tts = gTTS(text=jawaban, lang='ja')
                        tts.save('tts.mp3')
                        cl.sendAudio(msg.to,'tts.mp3')
#--------------------------------------------------------
            elif "Cek " in msg.text:
                tanggal = msg.text.replace("Cek ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#---------------------------------------------------------
            elif msg.text in ["Allprotect on"]:
            	if msg.from_ in admin or staff:
            	    if wait["AllProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = True
                        wait["Protectcancl"] = True
                        wait["Protectjoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Allprotect off"]:
            	if msg.from_ in admin or staff:
            	    if wait["AllProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = False
                        wait["Protectcancl"] = False
                        wait["Protectjoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
#--------------------------------------------------------            
            elif msg.text in ["runtime"]:
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
#--------------------------------------------------------
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
#--------------------------------------------------------
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
#--------------------------------------------------------
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
#--------------------------------------------------------
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#--------------------------------------------------------
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)
#-------------------------------------------------------
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#--------------------------------------------------------
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#----------------------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#-----------------------------------------------------------
            elif '.lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#-----------------------------------------------------------
            elif "Youtube:" in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------------------
            elif msg.text in ["List group"]:
		if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total group: "+str(jml))
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Creator")
#--------------------------------------------------------
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        ki.sendText(msg.to,"nothing")
                        kk.sendText(msg.to,"nothing")
                        kc.sendText(msg.to,"nothing")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        ki.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Khusus Creator")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
#--------------------------------------------------------
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot di paksa keluar oleh owner!")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    cl.sendText(msg.to,"Success left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"Khusus Creator")
#--------------------------------------------------------
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Bot di paksa keluar oleh owner!")
		        cl.leaveGroup(i)
			ki.leaveGroup(i)
			kk.leaveGroup(i)
			kc.leaveGroup(i)
		    cl.sendText(msg.to,"Success leave all group")
		else:
		    cl.sendText(msg.to,"Khusus Creator")
#--------------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    Cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Ourl","Url:on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Active")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Curl","Url:off"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    cl.sendText(msg.to,"AutoJoin Active")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin:off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"AutoJoin inActive")
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
	    elif msg.text in ["Autocancel:on"]:
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
		print wait["AutoCancel"][msg.to]

	    elif msg.text in ["Autocancel:off"]:
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Invitation refused turned off")
		print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
	    elif "Qr:on" in msg.text:
	        wait["Qr"] = True
	    	cl.sendText(msg.to,"QR Protect Active")

	    elif "Qr:off" in msg.text:
	    	wait["Qr"] = False
	    	cl.sendText(msg.to,"Qr Protect inActive")
#--------------------------------------------------------
	    elif "Autokick:on" in msg.text:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif "Autokick:off" in msg.text:
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in ["K on","Contact:on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Active")

            elif msg.text in ["K off","Contact:off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in ["Status"]:
                md = ""
		if wait["AutoJoin"] == True: md+="✦ Auto join : on\n"
                else: md +="✦ Auto join : off\n"
		if wait["Contact"] == True: md+="✦ Info Contact : on\n"
		else: md+="✦ Info Contact : off\n"
                if wait["AutoCancel"] == True:md+="✦ Auto cancel : on\n"
                else: md+= "✦ Auto cancel : off\n"
		if wait["Qr"] == True: md+="✦ Qr Protect : on\n"
		else:md+="✦ Qr Protect : off\n"
		if wait["AutoKick"] == True: md+="✦ Autokick : on\n"
		else:md+="✦ Autokick : off"
                cl.sendText(msg.to,"=====[Status]=====\n"+md)
#--------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)

            elif msg.text in ["Cb1 Gift","Cb1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text in ["Cb2 Gift","Cb2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kk.sendMessage(msg)

            elif msg.text in ["Cb3 Gift","Cb3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kc.sendMessage(msg)

#--------------------------------------------------------
	    elif "Tagall" == msg.text:
		if msg.from_ in Creator:
		    group = cl.getGroup(msg.to)
		    mem = [contact.mid for contact in group.members]
		    for mm in mem:
		        xname = cl.getContact(mm).displayName
		        xlen = str(len(xname)+1)
		        msg.contentType = 0
		        msg.text = "@"+xname+" "
		        msg.contentMetadata = {'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		        try:
		            cl.sendMessage(msg)
		        except Exception as e:
			    print str(e)
		else:
		    cl.sendText(msg.to, "Tag manual bos jgn males!")
#--------------------------CEK SIDER------------------------------

            elif "setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#-------Cek sider biar mirip kek siri-----------------------------
            elif "Setlastpoint" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #cl.sendText(msg.to, "Checkpoint checked!")
                cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                print "Setlastpoint"

            elif "Viewlastseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%d日 %H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        grp = '\n• '.join(str(f) for f in dataResult)
                        total = '\nThese %iuesrs have seen at the lastseen\npoint(｀・ω・´)\n\n%s' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "• %s %s" % (grp, total))
                    else:
                        cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
                    print "Viewlastseen"
#---------------------Sider ala anu---------------
            elif msg.text == "Cek om":
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Sider":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik kau dulu Cek baru Sider")
#--------------------------------------------------------

#KICK_BY_TAG
	    elif "Boom " in msg.text:
		if msg.from_ in Creator:
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ki.kickoutFromGroup(msg.to,[mention['M']])
		else:
		    cl.sendText(msg.to, "Khusus Creator")
#--------------------------------------------------------
	    elif "Set member: " in msg.text:
		if msg.from_ in admin:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
	    elif "Add all" in msg.text:
		if msg.from_ in admin:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
		cl.removeAllMessages(op.param2)
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		kc.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------------
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		kicker = [ki,kk,kc]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")
#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["#welcome","Welcome","welcome","Welkam","welkam"]:
                gs = cl.getGroup(msg.to)
                ki.sendText(msg.to,"Selamat datang di "+ gs.name)
#--------------------------------------------------------
	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
			cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~alrahmantoganteng")
		    cl.sendText(msg.to,"Success BC BosQ")
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Cb1 Cancelall"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                ki.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Cb2 Cancelall"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                kk.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Cb3 Cancelall"]:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                kc.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
            elif msg.text in ["All join"]:
		if msg.from_ in admin:
		    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Cb1 join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Cb2 join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Cb3 join"]:
		if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

#--------------------------------------------------------
	    elif msg.text in ["Cb Like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    ki.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    kk.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    kc.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @alrahmanto_selebgram\nLalu dm ke dia")
		    ki.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @alrahmanto_selebgram\nLalu dm ke dia")
		    kk.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @alrahmanto_selebgram\nLalu dm ke dia")
		    kc.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @alrahmanto_selebgram\nLalu dm ke dia")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#--------------------------------------------------------
            elif msg.text in ["Bye all"]:
		if msg.from_ in admin:
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                else:
                    cl.sendText(msg.to,"Lu Sapa!")

            elif msg.text in ["@Bye"]:
		if msg.from_ in admin:
		    cl.leaveGroup(msg.to)
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
		else:
		    cl.sendText(msg.to,"Lu Sapa!")
#--------------------------------------------------------
            elif msg.text in ["Absen"]:
              if msg.from_ in admin:
		cl.sendText(msg.to,"Pasukan absen!!")
                ki.sendText(msg.to,"Cb1 Hadiir  \(ˆ▿ˆ)/")
                kk.sendText(msg.to,"Cb2 Hadiir  \(ˆ▿ˆ)/")
                kc.sendText(msg.to,"Cb3 Hadiir  \(ˆ▿ˆ)/")

#--------------------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
              if msg.from_ in admin:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		cl.sendText(msg.to, "Progress...")
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                kc.sendText(msg.to, "%sseconds" % (elapsed_time))

#--------------------------------------------------------
            elif "Nk: " in msg.text:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti) #kicker join
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                kr.kickoutFromGroup(msg.to,[target])
                                kr.leaveGroup(msg.to)
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Pakyu~")
			    else:
			        cl.sendText(msg.to,"Admin Detected")
		else:
		    cl.sendText(msg.to,"Lu sape!")
#--------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
#--------------------------------------------------------
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        kk.sendText(msg.to,"Not found")
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes BosQ")
                                    kk.sendText(msg.to,"Succes BosQ")
                                    kc.sendText(msg.to,"Succes BosQ")
                                except:
                                    ki.sendText(msg.to,"Error")
                                    kk.sendText(msg.to,"Error")
                                    kc.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"nothing")
                    kk.sendText(msg.to,"nothing")
                    kc.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,"===[Blacklist User]===\n"+mc)

#--------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        kk.sendText(msg.to,"Not found")
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Succes BosQ")
                                kc.sendText(msg.to,"Succes BosQ")
                            except:
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Succes BosQ")
                                kc.sendText(msg.to,"Succes BosQ")
#--------------------------------------------------------
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                            kk.sendText(msg.to,"There was no blacklist user")
                            kc.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                        kk.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                        kc.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    cl.sendText(msg.to, "Khusus creator")
#--------------------------------------------------------
            elif msg.text in ["Kill"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kk.sendText(msg.to,"Fuck You")
                            kc.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

#--------------------------------------------------------
            elif "Buldozer" == msg.text:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Buldozer","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        ki.sendText(msg.to,"Sampai jumpaa~")
                        kc.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            kk.sendText(msg.to,"Not found.")
                            kc.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[ki,kk,kc]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)
#--------------------------------------------------------
            elif "Dj " in msg.text:
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                        for target in targets:
                            try:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                            except:                                                    cl.sendText(msg.to,"Error")
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["Bot:restart"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Bot has been restarted")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
#--------------------------------------------------------



        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

