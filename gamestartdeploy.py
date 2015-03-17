import os
import shutil
import stat
import subprocess
import sys
import time

print('Caution, replacing plug-in and editor:')
for i in range(9,0,-1):
	print(i)
	time.sleep(1)

# = = =
pathToMacuyikoProject 	= '../MinecraftPythonConsole-fork'
pathToServerPlugin 		= os.path.join(pathToMacuyikoProject,'ServerPythonInterpreterPlugin')
pathToWebEditor 		= os.path.join(pathToMacuyikoProject,'ServerEditorWeb')
if not os.path.exists(pathToServerPlugin):
	print('Oops! Missing Macuyiko\'s code. Clone from gamestartdev on github for a stable version.')
	sys.exit(1)

SERVER_PATH = os.path.join('.','server')
stuffToCopy = ['lib-common','lib-canary','python']

def exterminate(function, path):
	os.chmod(path, stat.S_IWRITE)
	os.remove(path)

for lib in stuffToCopy:
	source = os.path.join(pathToServerPlugin, lib)
	destination = os.path.join(SERVER_PATH, lib)
	if os.path.exists(destination):
		shutil.rmtree(destination,onerror=exterminate)
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

# = = =
CLIENT_PATH = os.path.join('.','client')
if os.path.exists(CLIENT_PATH):
	shutil.rmtree(CLIENT_PATH,onerror=exterminate)
shutil.copytree(pathToWebEditor, CLIENT_PATH)

print('Done!')
print('Ready to launch server from directory: ' + SERVER_PATH)
print('Ready to launch client from directory: ' + CLIENT_PATH)
