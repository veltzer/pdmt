#!/usr/bin/python

# this is a release script.
# it runs git status -s in order to see that everything is commited.
# it then tags the current tree with one + the old tag.
# it then cleans and then rebuilds everything and puts the results in the output.

# TODO:
# - add integration with twitter and facebook to announce new versions.
# - try to use a better git interface (there are native python git interfaces).

# this is for running the various commands that we need
import subprocess
import os # for getcwd
import releasemanager
import subproc

##############
# parameters #
##############
# do you want debug info printed?
debug=True
# do you want to check if everything is commited ? Answer True to this
# unless you are doing development on this script...
check=True
# what is the name of the project?
project=os.getcwd().split('/')[-1]

def doit():
	out=subprocess.check_output(['git','status','-s'])
	if check and out!='':
		raise ValueError('first commit everything, then call me...')
	tag=subprocess.check_output(['git','describe','--abbrev=0']).strip()
	tag=int(tag)
	if debug:
		print 'old tag is '+str(tag)
	tag+=1
	if debug:
		print 'new tag is '+str(tag)
	# tag the new tag
	subprocess.check_output(['git','tag','-s','-m',project+' version '+str(tag),str(tag)])
	# new name
	newname=project+'-'+str(tag)
	print('newname is',newname)
	subprocess.check_call(['make','clean'])
	subprocess.check_call(['make','install'])
	pdmt.utils.subproc.system_pipe(
		[
			'git',
			'archive',
			'--format=tar',
			'--prefix='+newname+'/',
			str(tag),
		],
		[
			'bzip2',
		],
		out=open(newname+'.tar.bz2','w'),
	)
	rm=ReleaseManager()
	rm.release()