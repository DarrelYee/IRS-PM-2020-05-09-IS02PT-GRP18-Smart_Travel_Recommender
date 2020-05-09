from Question import *

demographic_question1 = Question(	"Radiobutton",
									1,
									"Age",
									["20++",
									  "30++",
									  "40++",
									  "50 and above"])

demographic_question2 = Question(	"Radiobutton",
									2,
									"Gender",
									["Female",
									 "Male"])

preferences_question1 = Question(	"Radiobutton",
									3,
									"Choose the option that you prefer",
									["Playing board games with friends at home",
									 "Going out for dinner with friends"])

preferences_question2 = Question(	"Radiobutton",
									4,
									"Choose the option that you prefer",
									["Learning to play the guitar",
									 "Going to watch a play"])

preferences_question3 = Question(	"Radiobutton",
									5,
									"Choose the option that you prefer",
									["Living at a farm at a day",
									 "Spending a day at a cafe people watching"])

preferences_question4 = Question(	"Radiobutton",
									6,
									"Choose the option that you prefer",
									["Having an intellectual debate with your friends",
									 "Reading a classic"])

preferences_question5 = Question(	"Radiobutton",
									7,
									"Choose the option that you prefer",
									["Packing your day fully with activities",
									 "Leaving some space in your schedule for reflection"])

preferences_question6 = Question(	"Radiobutton",
									8,
									"Choose the option that you prefer",
									["Getting a gift that is on your wish list",
									 "Spending time with your loved ones"])

preferences_question7 = Question(	"Radiobutton",
									9,
									"Choose the option that you prefer",
									["Volunteeering your time at an elderly home",
									 "Donating to an animal shelter"])

preferences_question8 = Question(	"Radiobutton",
									10,
									"Choose the option that you prefer",
									["Having a fixed schdule",
									 "Letting the day plan itself"])

preferences_question9 = Question(	"Radiobutton",
									11,
									"Choose the option that you prefer",
									["Becoming a world famous surfer",
									 "Becoming a world famous artist"])

preferences_question10 = Question(	"Radiobutton",
									12,
									"Choose the option that you prefer",
									["Going for sunset yoga",
									 "Cooking for the family"])

preferences_question11 = Question(	"Radiobutton",
									13,
									"Choose the option that you prefer",
									["Partying through the night",
									 "Shopping till you drop"])

question_list1 = [demographic_question1, 
				  demographic_question2,
				  preferences_question1,
				  preferences_question2,
				  preferences_question3,
				  preferences_question4]
question_list2 = [preferences_question5,
				  preferences_question6,
				  preferences_question7,
				  preferences_question8,
				  preferences_question9,
				  preferences_question10,
				  preferences_question11]