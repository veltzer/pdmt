import imp
import os
imp.load_source('config','cfg.py')
overridefiles=os.path.expanduser('~/.cfg.py')
if os.path.isfile(overridefiles):
	imp.load_source('config',overridefiles)
