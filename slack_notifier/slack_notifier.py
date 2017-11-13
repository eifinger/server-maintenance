import os
import sys
import configparser
import argparse
from slackclient import SlackClient

# instantiate Slack
parent_dir = os.path.dirname(__file__)
token_file = os.path.join(parent_dir, "token.ini")
if( not os.path.exists(token_file)):
	sys.exit("Could not find token file \"{}\"".format(token_file))
parser = configparser.ConfigParser()
parser.read(token_file)
token = parser.get("slack_notifier", "token")
print("Token is: {}".format(token))

slack_client = SlackClient(token)

channel = "notifications"

def sendSlackMessage(message,channel=channel):
	slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)

def upload_file(filename,channel=channel):
	ret = slack_client.api_call('files.upload', channels=channel, filename=filename, file=open(filename, 'rb'))
	if not 'ok' in ret or not ret['ok']:
		self.logger.error('fileUpload failed %s', ret['error'])

def instantiate_Slack_Client(token):
	return SlackClient(token)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Sents Notifications to a Slack Channel')
	parser.add_argument('-m','--message', help='The message to send', required=True)
	parser.add_argument('-t','--token', help='The Bot token to use', required=False)
	parser.add_argument('-c','--channel', help='The channel to use', required=False)
	parser.add_argument('-i','--id', help='The Bot id to use', required=False)
	args = vars(parser.parse_args())
	try:
		slack_client = instantiate_Slack_Client(args['token'])
	except KeyError:
		pass
	try:
		channel = args['channel']
	except KeyError:
		pass

	if slack_client.rtm_connect():
		sendSlackMessage(args['message'])
	else:
		sys.exit("Connection failed. Invalid Slack token or bot ID?")
