
import os
import shutil
import time


countdown = 10
print('WARNING! This is about to reset the server! Halt in the next ' + str(countdown) + ' seconds to stop!')
for i in range(countdown,-1,-1):
	print(i)
	time.sleep(1)

pathToMacuyikoProject = '../MinecraftPythonConsole-fork'
pathToServerPlugin = os.path.join(pathToMacuyikoProject,'ServerPythonInterpreterPlugin')

stuffToCopy = ['lib-common','lib-canary','python']


SERVER_PATH = os.path.join('.','server')
if os.path.exists(SERVER_PATH):
	shutil.rmtree(SERVER_PATH)	#for some reason shutil.copytree freaks out if destination already exists. for safety I guess.
os.mkdir(SERVER_PATH)
	
for lib in stuffToCopy:
	source = os.path.join(pathToServerPlugin, lib)
	destination = os.path.join(SERVER_PATH, lib)
	shutil.copytree( source, destination )

#folder structure is silly. we need the server jar at the root.
jarname 	= 'CanaryMod-1.2.0.jar'
jarsource 	= os.path.join(SERVER_PATH ,'lib-canary',jarname)
jardest 	= os.path.join(SERVER_PATH, jarname)
shutil.move(jarsource, jardest)


pluginsource	= os.path.join(pathToServerPlugin, 'dist', 'console.jar')
pluginsfolder	= os.path.join(SERVER_PATH, 'plugins')
if not os.path.exists(pluginsfolder):
	os.mkdir(pluginsfolder)
shutil.copyfile(pluginsource, os.path.join(pluginsfolder,'console.jar'))

print('Done! Ready to launch server from directory: ' + SERVER_PATH)
