#!/usr/bin/env python

import sys

import os

import os.path

import xml.dom.minidom


m2 = xml.dom.minidom.parse('pom.xml')

properties = m2.getElementsByTagName("properties")[0]
branchNode = m2.createElement("sonar.branch")

dataNodeBranch = m2.createTextNode(os.environ["BRANCH_NAME"])
branchNode.appendChild(dataNodeBranch)

properties.appendChild(branchNode)

m2Str = m2.toxml()

f = open('pom.xml', 'w')

f.write(m2Str)

f.close()
