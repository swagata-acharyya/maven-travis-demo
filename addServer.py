#!/usr/bin/env python

import sys

import os

import os.path

import xml.dom.minidom





homedir = os.path.expanduser("~")



m2 = xml.dom.minidom.parse(homedir + '/.m2/settings.xml')

settings = m2.getElementsByTagName("settings")[0]


mirrorNodes = settings.getElementsByTagName("mirrors")

if not mirrorNodes:

  mirrorNode = m2.createElement("mirrors")

  settings.appendChild(mirrorNode)

else:

  mirrorNode = mirrorNodes[0]

  

sonatypeMirrorNode = m2.createElement("mirror")

sonatypeMirrorId = m2.createElement("id")

sonatypeMirrorOf = m2.createElement("mirrorOf")

sonatypeMirrorUrl = m2.createElement("url")



idNodeMirror = m2.createTextNode("nexus")

userNodeMirror = m2.createTextNode("*,!cloudant-sync-eap,!maven-central,!oss.sonatype.org-jayway-snapshots")

urlNodeMirror = m2.createTextNode("http://nexus.miairline.com/nexus/content/groups/public/")



sonatypeMirrorId.appendChild(idNodeMirror)

sonatypeMirrorOf.appendChild(userNodeMirror)

sonatypeMirrorUrl.appendChild(urlNodeMirror)



sonatypeMirrorNode.appendChild(sonatypeMirrorId)

sonatypeMirrorNode.appendChild(sonatypeMirrorOf)

sonatypeMirrorNode.appendChild(sonatypeMirrorUrl)



mirrorNode.appendChild(sonatypeMirrorUrl)





serversNodes = settings.getElementsByTagName("servers")

if not serversNodes:

  serversNode = m2.createElement("servers")

  settings.appendChild(serversNode)

else:

  serversNode = serversNodes[0]

  

sonatypeServerNode = m2.createElement("server")

sonatypeServerId = m2.createElement("id")

sonatypeServerUser = m2.createElement("username")

sonatypeServerPass = m2.createElement("password")



idNode = m2.createTextNode("nexus")

userNode = m2.createTextNode("admin")

passNode = m2.createTextNode("EOCa1uiceT")



sonatypeServerId.appendChild(idNode)

sonatypeServerUser.appendChild(userNode)

sonatypeServerPass.appendChild(passNode)



sonatypeServerNode.appendChild(sonatypeServerId)

sonatypeServerNode.appendChild(sonatypeServerUser)

sonatypeServerNode.appendChild(sonatypeServerPass)



serversNode.appendChild(sonatypeServerNode)

  
str(m2)
m2Str = m2.toxml()

f = open(homedir + '/.m2/settings.xml', 'w')

f.write(m2Str)

f.close()

