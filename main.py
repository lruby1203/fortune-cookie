import webapp2
import random

def getRandomFortune():
	#make list of possible fortunes
	fortunes = [
		"I see much code in your future.",
		"Consider eating more fortune cookies.",
		"You have tamed the mighty Python, now you must free it onto the Great Spider's Web!"
		]
	#Randonly selelct one of the fortunes
	index = random.randint (0, 2)

	return fortunes[index]

def lucky_numbers():
	numbers = []
	number_sentence = 'Your lucky numbers are: '
	for index in range(5):
		numbers.append(str(random.randint (1, 100)))
#		if index > 0:
#			for num in numbers:
#				if num == numbers[index]:
#					match = True
#					numbers[index] = random.randint(1, 100)
		number_sentence += numbers[index] + " "
	return number_sentence

class MainHandler(webapp2.RequestHandler):

	def get(self):
		header = "<h1>Fortune Cookie</h1>"

		fortune = "<strong>" + getRandomFortune() + "</strong>"
		fortune_sentence = "Your fortune: " + fortune
		fortune_paragraph = "<p>" + fortune_sentence + "</p>"
#		lucky_number = str(random.randint(1, 100))
		numbers = "<strong>" + lucky_numbers() + "</strong>"
		number_sentence = 'Your lucky numbers are: ' + numbers
		number_paragraph = "<p>" + number_sentence + "</p>"

		cookie_again_button = "<a href='.'><button>Another cookie plz!</button></a>"

		content = header + fortune_paragraph + number_paragraph + cookie_again_button

		self.response.write(content)

app = webapp2.WSGIApplication([
	('/', MainHandler)
	], debug=True)
