import yaml
import random
import os
import time

CONFIGFILE = "./nonsense.yaml"

with open(CONFIGFILE) as yamlConfigFile:
  YAMLCONFIG = yaml.load(yamlConfigFile)

class TrumpSpeak(object):

	def __init__(self, topic):

		self.topic = topic
		self.response = ""
		self.generate_values()
		self.add_to_response(random.choice(YAMLCONFIG['beginning']))
		self.add_to_response(self.middle)
		self.add_to_response(self.end)		

		self.response = self.response.replace("$topic$", topic)

		print("  President Trump's Reponse: \n\n    %s\n\n\n" % self.response)


	def update_variables(self):
		for variable in YAMLCONFIG:
			try:
				self.response = self.response.replace("$%s$" % variable, eval('self.%s' % variable))
			except:
				continue
	

	def add_to_response(self, item):
		self.response += item + self.random_emphasis
		self.generate_values()
		self.update_variables()

	def generate_values(self):
		self.emphasis = random.choice(YAMLCONFIG['emphasis'])
		self.severity = random.choice(YAMLCONFIG['severity'])
		self.big_adj = random.choice(YAMLCONFIG['big_adj'])
		self.status_adj = random.choice(YAMLCONFIG['status_adj'])
		self.counts = random.choice(YAMLCONFIG['counts'])
		self.professions = random.choice(YAMLCONFIG['professions'])
		self.middle = random.choice(YAMLCONFIG['middle'])
		self.end = random.choice(YAMLCONFIG['end'])
		self.random_emphasis = random.choice(YAMLCONFIG['random_emphasis'])
 
if __name__ == "__main__":
	os.system('clear')
	print("\n\n  What topic do you want President Trump's opinion on?\n")
	topic = raw_input("    ")
	print("\n  Trump is thinking...\n\n")
	time.sleep(5)
	TrumpSpeak(topic)