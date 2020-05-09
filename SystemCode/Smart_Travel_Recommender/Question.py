class Question:

	QUESTION_TYPE_LIST = [	"Radiobutton",
							"Checkbox",
							"Slider"]

	RADIOBUTTON = 0
	CHECKBOX = 1
	SLIDER = 2


	def __init__(self, question_type, question_num, question, options=None, remarks=None):

		check = False
		for types in Question.QUESTION_TYPE_LIST:
			if question_type == types:
				self.question_type = question_type
				check = True

		if check == False:
			raise ValueError("Invalid question_type")

		self.question = str(question)

		if type(question_num) == int:
			self.question_num = question_num
		else:
			raise TypeError("Question number has to be a integer")


		if self.question_type == Question.QUESTION_TYPE_LIST[self.RADIOBUTTON]:
			
			if type(options) == list:
				self.options = options
			else:
				raise TypeError("Radio Button requires list options")

			self.answer = []
			for items in options:
				self.answer.append(False)
			self.answer[0] = True

		elif self.question_type == Question.QUESTION_TYPE_LIST[self.CHECKBOX]:

			if type(options) == list:
				self.options = options
			else:
				raise TypeError("Radio Button requires list options")

			self.answer = []
			for items in options:
				self.answer.append(False)



		elif self.question_type == Question.QUESTION_TYPE_LIST[self.SLIDER]:

			if 	(type(options) == list and
				len(options) == 2 and
				type(options[0]) == int and
				type(options[1]) == int and
				type(options[0] <= options[1])):

				self.options = options
			else:
				raise TypeError("Slider requires a list with 2 integer inputs. Element 0: min, Element 1: max")

			self.answer = option[0]

		self.remarks = remarks