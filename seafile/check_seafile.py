import os
from ConfigParser import SafeConfigParser
from subprocess import call
from slack_notifier import sendSlackMessage
from slack_notifier import upload_file

INI_FILE_NAME = "check_seafile.ini"

if __name__ == "__main__":
	parent_dir = os.path.dirname(__file__)

	config_file = os.path.join(parent_dir, INI_FILE_NAME)
	if( not os.path.exists(config_file):
		sys.exit("Could not find config file \"{}\"".format(config_file))
	parser = SafeConfigParser()
	parser.read(config_file)
	seafile_root_dir = parser.get("seafile", "seafile_root_dir")
	seafile_user = parser.get("seafile", "seafile_user")
	if (not os.path.isdir(seafile_root_dir)):
		sys.exit("Could not find seafile installation under standard path \"{}\". Please supply the value in \"{}\"".format(INI_FILE_NAME, config_file))
	fsck_result_file = os.path.join(parent_dir, 'seafile_fsck_result.txt')
	#Execute seaf-fsck and save the output to fsck_result_file
	call("su " + seafile_user + " -c '"+ seafile_root_dir +"/seafile-server-latest/seaf-fsck.sh'>"+fsck_result_file,shell=True)
	#If there is the word "commit" in the file it means some library is corrupted.
	#->Send a notification and upload the file
	if 'commit' in open(fsck_result_file).read():
		sendSlackMessage("Seafile fsck failed")
		upload_file(fsck_result_file)
	else:
		sendSlackMessage("Seafile fsck without errors")
