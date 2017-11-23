# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
#import gTTS
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests , ctypes, urllib, urllib2, wikipedia


print "===[Login Success]==="

mulai = time.time() 

helpBot ="""╠═════════════════╣
║             cᴏᴍᴍᴀɴᴅ ᴏɴ ʙᴏᴛ 
╠═════════════════╣
╠➩〘/ᴡᴇʟᴄᴏᴍᴇ〙
╠➩〘/ᴄʀᴇᴀᴛᴏʀ〙
╠➩〘/ɢᴄʀᴇᴀᴛᴏʀ〙
╠➩〘/ɢɪɴꜰᴏ〙
╠➩〘/ʟɪsᴛ ɢʀᴏᴜᴘ〙
╠➩〘/ʀᴜɴ〙
╠➩〘/ᴄᴇᴋ〙
╠➩〘/ᴄᴄᴛᴠ〙
╠➩〘/sᴘᴇᴇᴅ〙
╠➩〘/ᴍᴇᴅɪᴀ〙
╠➩〘/ʙᴀɴʟɪsᴛ〙
╠➩〘/ᴋᴇʏ sᴛᴀғғ〙
╠➩〘/ᴋᴇʏ ᴏᴡɴᴇʀ〙
╠➩〘/ʙᴀɴʟɪsᴛ〙
╠═════════════════╣
║  🅱🅾🆃 🅿🆁🅸🆅🅰🆃 🆃🅱🅲
╠═════════════════╣
║            🅲🆁🅴🅰🆃🅾🆁       
║http://line.me/ti/p/~aries_jabrik                     
╚═════════════════╝
"""
helpMedia ="""╠═════════════════╣
║             cᴏᴍᴍᴀɴᴅ ᴍᴇᴅɪᴀ  
╠═════════════════╣
╠➩〘/ʏᴏᴜᴛᴜʙᴇ:〙
╠➩〘/ᴍᴜsɪᴄ〙
╠➩〘/ɪɴsᴛᴀɢʀᴀᴍ〙
╠➩〘/ʟʏʀɪᴄ〙
╠➩〘/ᴡɪᴋɪᴘᴇᴅɪᴀ〙
╠➩〘/ᴡᴇᴛᴏɴ〙
╠➩〘Aᴘᴀᴋᴀʜ〙fitur kerang ajaib
║
║ Next project;fitur sim-simi
║
╠═════════════════╣
║  ɢᴏsᴀʜ 🅺🅴 🅱🅾🆃 🅰🅽    
╠═════════════════╣
║  ɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ᴅᴇɴɢᴀɴ        
║                 . ʙɪᴊᴀᴋ                   
╚═════════════════╝
"""
helpStaf ="""╠═════════════════╣
║             cᴏᴍᴍᴀɴᴅ sᴛᴀꜰꜰ 
╠═════════════════╣
╠➩〘/ᴄᴀɴᴄᴇʟ〙
╠➩〘/ɢᴜʀʟ〙
╠➩〘/ɢɪꜰᴛ〙1,2,3
╠➩〘/ᴜɴʙᴀɴ〙
╠➩〘/ᴜɴʙᴀɴ @〙
╠➩〘/ɢɴ:〙(nama)
╠➩〘ᴋɪʟʟ ʙᴀɴ〙
║
╠═════════════════╣
║     ʜᴜʙᴜɴɢɪ ᴏᴡɴᴇʀ ʙᴏᴛ 
║   ᴜɴᴛᴜᴋ ᴘᴇɴᴀᴍʙᴀʜᴀɴ sᴛᴀꜰ                
╚═════════════════╝
"""

mid = cl.getProfile().mid
Bots=[mid]
Creator="u17ce7606c05a31e55cfccb35487cfbf3"
admin=["ucc9e126446008609724bb076d8cda07a"]
adminSA = Bots + Creator + admin

contact = cl.getProfile()
profile = cl.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "Members":0,
    "AutoCancel":False,
    "AutoKick":False,       
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":True,
    "Timeline":True,
    "Contact":True,
    "lang":"JP",
    "BlGroup":{}
}

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()


def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


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

	    if mid in op.param3:
                if wait["AutoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
		    cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in admin:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
                    if op.param2 not in adminSA:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
			    cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in admin:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in admin:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True



#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 not in adminSA:
		    pass
		else:
                    cl.sendText(msg.to, "Jangan otak atik ntr dikira kicker")
            else:
                pass
#--------------------------SEND_MESSAGE---------------------------
        if op.type == 26:
            msg = op.message
#----------------------------------------------------------------------------

            if 'MENTION' in msg.contentMetadata.keys() != None:
               #  if ["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Kenapa sayangku",cName + " kangen ya?",cName + " nggk ush tag.klo kangen pc aja"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break
#******************************************

            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in adminSA:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            cl.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            cl.sendText(msg.to,"aded")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
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
            elif msg.text == "/ginfo":
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
            elif msg.text in ["/creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"ᴅɪᴀ ʙᴏs'ǫ...!!!!")
#--------------------------------------------------------
	    elif msg.text in ["Group creator","Gcreator","/gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"ᴅɪᴀ ʏɢ ᴘᴜɴʏᴀ ᴋᴏsᴛ'ᴀɴ sɪɴɪ...!!!!")
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#--------------------------------------------------------
            elif msg.text == '/key bot':
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
                        cl.sendText(msg.to,"╔═════════════════╗\n║〘Gʀᴏᴜᴘ Nᴀᴍᴇ〙➩ " + str(ginfo.name) + "\n║〘GCʀᴇᴀᴛᴏʀ〙➩ " + gCreator + "\n║〘Mᴇᴍʙᴇʀ〙➩ " + str(len(ginfo.members)) + "ᴇᴋᴏʀ\n║〘Pᴇɴᴅɪɴɢ〙➩ " + sinvitee + "ᴇᴋᴏʀ\n║〘ᴜʀʟ〙➩ " + u + "\n" + helpBot)
                    else:
                       # cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        pass

#--------------------------------------------------------
            elif msg.text == '/media':
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
                        cl.sendText(msg.to,"╔═════════════════╗\n║〘Gʀᴏᴜᴘ Nᴀᴍᴇ〙➩ " + str(ginfo.name) + "\n║〘GCʀᴇᴀᴛᴏʀ〙➩ " + gCreator + "\n║〘Mᴇᴍʙᴇʀ〙➩ " + str(len(ginfo.members)) + "ᴇᴋᴏʀ\n║〘Pᴇɴᴅɪɴɢ〙➩ " + sinvitee + "ᴇᴋᴏʀ\n║〘ᴜʀʟ〙➩ " + u + "\n" + helpMedia)
                    else:
                       # cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        pass

#--------------------------------------------------------
            elif msg.text == '/key staf':
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
                        cl.sendText(msg.to,"╔═════════════════╗\n║〘Gʀᴏᴜᴘ Nᴀᴍᴇ〙➩ " + str(ginfo.name) + "\n║〘GCʀᴇᴀᴛᴏʀ〙➩ " + gCreator + "\n║〘Mᴇᴍʙᴇʀ〙➩ " + str(len(ginfo.members)) + "ᴇᴋᴏʀ\n║〘Pᴇɴᴅɪɴɢ〙➩ " + sinvitee + "ᴇᴋᴏʀ\n║〘ᴜʀʟ〙➩ " + u + "\n" + helpStaf)
                    else:
                       # cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        pass

#--------------------------------------------------------
            elif msg.text in ["/list group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
		jml = 0
                for i in gid:
		    gn = cl.getGroup(i).name
                    h += "♦【%s】\n" % (gn)
		    jml += 1
                cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total group: "+str(jml))
#--------------------------------------------------------
	    elif "/leave group: " in msg.text:
        if msg.from_ in Creator:
		ng = msg.text.replace("/leave group: ","")
		gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
		    if h == ng:
			cl.sendText(i,"Bye "+h+"~")
		        cl.leaveGroup(i)
			cl.sendText(msg.to,"Success left ["+ h +"] group")
		    else:
			pass
#--------------------------------------------------------
#--------------------------------------------------------
            elif msg.text in ["/cancel","Cancel"]:
              if msg.from_ in adminSA:
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
            elif msg.text in ["/url","/url:on"]:
              if msg.from_ in adminSA:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Active")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["/curl","/url:off"]:
              if msg.from_ in adminSA:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["/join on","/autojoin:on"]:
              if msg.from_ in Creator:
                wait["AutoJoin"] = True
                cl.sendText(msg.to,"AutoJoin Active")

            elif msg.text in ["/join off","/autojoin:off"]:
              if msg.from_ in Creator:
                wait["AutoJoin"] = False
                cl.sendText(msg.to,"AutoJoin inActive")

#--------------------------------------------------------
	    elif msg.text in ["/autocancel:on"]:
        if msg.from_ in Creator:
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
		print wait["AutoCancel"][msg.to]

	    elif msg.text in ["/autocancel:off"]:
        if msg.from_ in Creator:
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Invitation refused turned off")
		print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
	    elif "/qr:on" in msg.text:
        if msg.from_ in Creator:
	        wait["Qr"] = True
	    	cl.sendText(msg.to,"QR Protect Active")

	    elif "/qr:off" in msg.text:
        if msg.from_ in Creator:
	    	  wait["Qr"] = False
	    	cl.sendText(msg.to,"Qr Protect inActive")
#--------------------------------------------------------
	    elif "/autokick:on" in msg.text:
        if msg.from_ in Creator:
		      wait["AutoKick"] = True
		    cl.sendText(msg.to,"AutoKick Active")

	    elif "/autokick:off" in msg.text:
        if msg.from_ in Creator:
	        wait["AutoKick"] = False
		    cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in ["K on","/contact:on"]:
              if msg.from_ in Creator:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Active")

            elif msg.text in ["K off","/contact:off"]:
              if msg.from_ in Creator:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in ["/status"]:
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
            elif msg.text in ["Gift","/gift"]:
              if msg.from_ in adminSA:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["/gift1"]:
              if msg.from_ in adminSA:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["/gift2"]:
              if msg.from_ in adminSA:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["/gift3"]:
              if msg.from_ in adminSA:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
 #aplahapalhapalahapalahapalahapalahapalahapalah

            elif msg.text.lower() == '/run':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
#apalahapalahapalahapalahapalahapalahapalah                       
           
            elif msg.text in ["/jam","/time","/waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
#apalahapalahapalahaapalahapalahapalahapalah

            elif "/weton " in msg.text:
                tanggal = msg.text.replace("/weton ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
               
#--------------------------------------------------------
	    elif "/tagall" == msg.text:
        if msg.from_ in adminSA:
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

#--------------------------CEK SIDER------------------------------

            elif "/cek" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "/cctv" in msg.text:
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
#--------------------------------------------------------

#KICK_BY_TAG
	    elif "/boom " in msg.text:
        if msg.from_ in Creator:
		if 'MENTION' in msg.contentMetadata.keys()!= None:
		    names = re.findall(r'@(\w+)', msg.text)
		    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		    mentionees = mention['MENTIONEES']
		    print mentionees
		    for mention in mentionees:
			cl.kickoutFromGroup(msg.to,[mention['M']])

#--------------------------------------------------------
	    elif "/add all" in msg.text:
        if msg.from_ in Creator:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.findAndAddContactsByMids(mi_d)
		cl.sendText(msg.to,"Success Add all")
#--------------------------------------------------------
	    elif "/recover" in msg.text:
        if msg.from_ in Creator:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["/remove all chat"]:
        if msg.from_ in Creator:
		cl.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif ("/gn: " in msg.text):
              if msg.from_ in adminSA:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------------
            elif "/kick: " in msg.text:
              if msg.from_ in Creator:
                midd = msg.text.replace("/kick: ","")
		if midd not in admin:
		    cl.kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")
#--------------------------------------------------------
            elif "/invite: " in msg.text:
              if msg.from_ in Creator:
                midd = msg.text.replace("/invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["#welcome","Welcome","/welcome","kam","welkam"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat datang di "+ gs.name)

#==================================================
            elif '/lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params)) 
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#==========================================

            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/music ','')
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

#++++++++++++++++++++++++++++++++
            elif "/youtube:" in msg.text.lower():
               # if msg.from_ in admin:
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

  #+++++++++++++++++++++++++++++++++++++++++++++++++                     
                      
            elif '/wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/wikipedia ","")
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
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif '/instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/instagram ","")
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
                  
#Sc Kerang By Zado next gen with vn__________

            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("iya","Tidak")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "/kedapkedip " in msg.text.lower():
                txt = msg.text.lower().replace("kedapkedip ","")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)       

#--------------------------------------------------------
	    elif "/bc: " in msg.text:
        if msg.from_ in Creator:
       # if msg.from_ in Creator:
		bc = msg.text.replace("/bc: ","")
		gid = cl.getGroupIdsJoined()
		for i in gid:
		    cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n")
		cl.sendText(msg.to,"Success BC BosQ")
#--------------------------------------------------------
            elif msg.text in ["/cancelall"]:
              if msg.from_ in Creator:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in ["/gurl"]:
              if msg.from_ in Creator:
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
	    elif msg.text in ["/self Like"]:
        if msg.from_ in Creator:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @rid1bdbx\nLalu dm ke dia")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
            elif msg.text in ["/Sp","/sp","/Speed","/speed"]:
                start = time.time()
		print("Speed")
                elapsed_time = time.time() - start
		cl.sendText(msg.to, "Progress...")
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#+++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Sp","Speed","speed"]:
                fake=["0.00271114197 detik","0.0019165887 detik","0.0025112297 detik","0.00218382292 detik","0.0026668778 detik","0.00218382117 detik","0.001193829922 detik","0.003524116 detik"]
                fspeed=random.choice(fake)
                cl.sendText(msg.to,"Progress...")
                cl.sendText(msg.to,(fspeed))    

#--------------------------------------------------------
            elif msg.text in ["/ban"]:
              if msg.from_ in Creator:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")

            elif msg.text in ["/unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
#--------------------------------------------------------
	    elif "/backup me" in msg.text:
        if msg.from_ in Creator:
		try:
		    cl.updateDisplayPicture(profile.pictureStatus)
		    cl.updateProfile(profile)
		    cl.sendText(msg.to, "Success backup profile")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
#--------------------------------------------------------
	    elif "/copy " in msg.text:
        if msg.from_ in adminSA:
                copy0 = msg.text.replace("/copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = cl.getGroup(msg.to)
		for contact in group.members:
		    cname = cl.getContact(contact.mid).displayName
		    if cname == _name:
			cl.CloneContactProfile(contact.mid)
			cl.sendText(msg.to, "Success~")
		    else:
			pass
		
#--------------------------------------------------------
            elif "/ban @" in msg.text:
              if msg.from_ in Creator:
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes BosQ")
                                except:
                                    cl.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in ["/banlist"]:
             # if msg.from_ in Creator:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"===[Blacklist User]===\n"+mc)

#--------------------------------------------------------
            elif "/unban @" in msg.text:
              if msg.from_ in adminSA:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
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
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes BosQ")
                            except:
                                cl.sendText(msg.to,"Succes BosQ")
#--------------------------------------------------------
            elif msg.text in ["/kill ban"]:
              if msg.from_ in adminSA:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
#--------------------------------------------------------
#            elif "Cleanse" in msg.text:
#                if msg.toType == 2:
#                    print "Kick all member"
#                    _name = msg.text.replace("Cleanse","")
#                    gs = cl.getGroup(msg.to)
#                    cl.sendText(msg.to,"Dadaaah~")
#                    targets = []
#                    for g in gs.members:
#                        if _name in g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        cl.sendText(msg.to,"Not found.")
#                    else:
#                        for target in targets:
#			     if target not in admin:
#                                try:
#                                    cl.kickoutFromGroup(msg.to,[target])
#                                    print (msg.to,[g.mid])
#                                except Exception as e:
#                                    cl.sendText(msg.to,str(e))
#			 cl.inviteIntoGroup(msg.to, targets)
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["/restart"]:
        if msg.from_ in Creator:
		cl.sendText(msg.to, "Bot has been restarted")
		restart_program()
		print "@Restart"
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

