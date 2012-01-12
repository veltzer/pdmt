# do not import any pdmt classes here except boot
# you may use other classes as long as they are supported in all versions
# of python you will be using
import pdmt.utils.boot

class ns_pdmt:
	p_version=pdmt.utils.boot.system_check_output(['git','describe']).rstrip()
class ns_release:
	p_email=True
	p_tweet=False
	p_subject='A new version of optimus is out'
	p_from='Optimus release manager: Mark Veltzer'
	p_to='mark.veltzer@gmail.com,shay@hinbit.com'
	p_smtp_host='smtp.gmail.com'
	p_content='Check out the new version of optimus in http://www.veltzer.net/optimus'
	#p_mail_user=[mail_user]
	#p_mail_password=[mail_password]
	#p_twitter_user=[twitter_user]
	#p_twitter_password=[twitter_password]
	p_debug=True
	p_usetls=True
class ns_install:
	p_name='pdmt'
	p_description='Project Dependency Management Tool'
	p_author='Mark Veltzer'
	# this key is used for signing...
	p_email='mark@veltzer.net'
	p_dir_list=pdmt.utils.boot.dir_list('pdmt')
	p_deps=[
		'python-pygraph',
		'python-pyinotify',
		'python-pyinotify-doc',
		'python-inotifyx',
		'python-stdeb',
	]
	p_require=[
		'pygraph',
	]
	p_version=pdmt.utils.boot.system_check_output(['git','describe']).rstrip()
	p_url='http://veltzer.net/pdmt'
	p_classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: LGPL',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: Software Development :: Building',
	]
	p_scripts=[
	]
	p_data_files=[
		'cfg.py',
	]
class ns_reprepro:
	p_sudo=True
	p_conf='conf'
	p_folder='apt'
	p_servicedir='/var/www/'+p_folder
	p_component='main'
	p_components='main'
	p_codename=pdmt.utils.boot.system_check_output(['lsb_release','--codename','--short']).rstrip()
	p_redirect=True
	p_cannonical='python-pdmt'
	p_id=pdmt.utils.boot.system_check_output(['lsb_release','--id','-s']).rstrip()
	p_hostname=pdmt.utils.boot.system_check_output(['hostname','--domain']).rstrip()
	p_fullname='Mark Veltzer <mark.veltzer@gmail.com>'
	p_key='6752126F'
	p_keyname='public_key.gpg'
	p_architectures='i386 source'
	p_name='veltzer.net'
	p_url='http://'+p_name+'/'+p_folder
class ns_chandler:
	p_sourcefilesuffix='.c'
	p_objectfilesuffix='.o'
class ns_makohandler:
	p_sourcefilesuffix='.mako'
	p_targetdir='makot'
class ns_fileops:
	p_debug=True
	p_debug=False
class ns_subproc:
	p_debug=True
	p_debug=False
