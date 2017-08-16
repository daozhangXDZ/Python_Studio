#coding=utf-8
import  xml.dom.minidom;
import  subprocess;
from subprocess import Popen,PIPE
def openUnity(pUnityPath,pProjectPath):
    p = Popen(pUnityPath+"-projectPath "+pProjectPath + " -force-gles", shell=True)

dom = xml.dom.minidom.parse('unitybuilder.xml')
root = dom.documentElement;
unity_ExePath = root.getElementsByTagName('unity')[0].getAttribute("exepath");
Builder_Project = root.getElementsByTagName('Projectpath');
unity_OpenProject =Builder_Project[0].getAttribute("path");
print("unity_ExePath        ->>> "+unity_ExePath);
print("unity_OpenProject    ->>> "+unity_OpenProject);

buildnode_arr = Builder_Project[0].getElementsByTagName('BuilderTarget');
#OPen UNity
openUnity(unity_ExePath,Builder_Project);
#打包工程
for child in buildnode_arr:
    #print(child);
    print(" ***** builder target--> | ",child.getAttribute("target"),' | ',child.getAttribute("patform"));

