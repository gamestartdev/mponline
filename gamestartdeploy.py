
import os
import shutil

pathToMacuyikoProject = '../MinecraftPythonConsole-fork'
pathToServerPlugin = os.path.join(pathToMacuyikoProject,'ServerPythonInterpreterPlugin')

stuffToCopy = ['lib-common','lib-canary','python']


SERVER_PATH = 'server'
if os.path.exists(SERVER_PATH):
	shutil.rmtree(SERVER_PATH)	#for some reason shutil.copytree freaks out if destination already exists. for safety I guess.

for lib in stuffToCopy:
	source = os.path.join(pathToServerPlugin, lib)
	destination = os.path.join(SERVER_PATH, lib)
	shutil.copytree( source, destination )

#folder structure is silly. we need the server jar at the root.
jarname 	= 'CanaryMod-1.2.0.jar'
jarsource 	= os.path.join(SERVER_PATH ,'lib-canary',jarname)
jardest 	= os.path.join(SERVER_PATH, jarname)
shutil.move(jarsource, jardest)

print('Done! Ready to launch server from directory: ' + SERVER_PATH)
