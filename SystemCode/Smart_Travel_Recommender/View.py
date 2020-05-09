from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from io import BytesIO
import numpy as np
import requests
import ctypes
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Activity import *
from Question import *

#Learn tkinter
#https://www.youtube.com/watch?v=YXPyB4XeYLA

class View:

	NOIMAGE_LINK = r'images\noimage.png'

	MAX_WIDTH = 240
	MAX_HEIGHT = 160
	instance = None	

	def __init__(self, root):
		if View.instance != None:
			raise Exception ("View is a Singleton Class")
		else:
			View.instance = self

		self.root = root
		self._changeview = None
		self._getanswers = None
		self._redo = None
		self.frame_content_dict = {}
		self.frame_header_dict = {}

		#intialise font family
		self.font_family_header = font.Font(size=24, family="bold")
		self.font_family_questiontitle = font.Font(size=16, family="bold")
		self.font_family_questionremark = font.Font(size=9)
		self.font_family_activitytitle = font.Font(size=16, family="bold")
		self.font_family_activitycategory = font.Font(size=12)
		self.font_family_activityaddress = font.Font(size=9, family="italic")
		self.font_family_activitydescription = font.Font(size=10)
		self.font_family_activitylocation = font.Font(size=9, family="italic")
		self.font_family_footer = font.Font(size=8)

	'''
	Method: To set a callback function so that View Instance will be able to actively
			call functions from the program that called View Instance.
	Arguements:
		callback: The function to callback
	'''
	def bind_to(self, func_changeview, func_getanswers, func_redo, func_next):
		self._changeview = func_changeview
		self._getanswers = func_getanswers
		self._redo = func_redo
		self._next = func_next

	'''
	Method: Set title of the windows
	Arguements:
		Title: Name of the windows
	'''
	def set_title(self, title):
		self.root.title(title)

	'''
	Method: Set icon at the top left of the window
	Arguements:
		icon_path: Path to the icon image. Image has to be in .ico
	'''
	def set_icon(self, icon_path):
		self.root.iconbitmap(icon_path)

	'''
	Method: Set size of window
	Arguements:
		width: width of the window
		height: height of the window
	'''
	def set_window_size(self, width, height):
		if type(width) != int and type(height) != int:
			raise TypeError("width and height inputs needs to be integer")

		max_width = ctypes.windll.user32.GetSystemMetrics(78) 
		max_height = ctypes.windll.user32.GetSystemMetrics(79)
		self.root.geometry(str(min(max_width,width)) + "x" + str(min(max_height,height)))

	'''
	Method: Apportioning spaces for Menubar, headers, sidebars, main content and footer
	Arguements:
		frame_names: Names for the mutiple header and content frames, which enables
					 changing of content in the header and content frames.
	'''
	def set_frames(self, frame_names):
		self.frame_menu = Frame(self.root)
		self.frame_menu.grid(row=0, pady=2, sticky=W+E)
		
		for F in frame_names:
			frame_header = LabelFrame(self.root, padx=5, pady=5)
			self.frame_header_dict[F] = frame_header 
			frame_header.grid(row=1, column=0, sticky=N+S+W+E)

		self.frame_mainframe = Frame(self.root)
		self.frame_mainframe.grid(row=2, pady=1, stick=N+S+W+E)

		self.frame_footer = Frame(self.root)
		self.frame_footer.grid(row=3, sticky=W+E)

		self.frame_sidebar = LabelFrame(self.frame_mainframe, padx=5, pady=5)		
		self.frame_sidebar.grid(row=0, column=0, padx=2, sticky=N+S)

		for F in frame_names:
			frame_content = LabelFrame(self.frame_mainframe, padx=5, pady=5)
			self.frame_content_dict[F] = frame_content 
			frame_content.grid(row=0, column=1, sticky=N+S+W+E)

		self.root.grid_rowconfigure(0, weight=0)
		self.root.grid_rowconfigure(1, weight=0)
		self.root.grid_rowconfigure(2, weight=1)
		self.root.grid_rowconfigure(3, weight=0)
		self.root.grid_columnconfigure(0, weight=1)
	
		self.frame_mainframe.grid_rowconfigure(0, weight=1)
		self.frame_mainframe.grid_columnconfigure(0, weight=0)
		self.frame_mainframe.grid_columnconfigure(1, weight=1)

	'''
	Method: Setting up the default menubar with exit and credits functionality
	Arguements: 
		None
	'''
	def menu_template(self):
		menu_bar = Menu(self.frame_menu)
		
		menu_file = Menu(menu_bar, tearoff=0)
		menu_file.add_command(label="Exit", command=quit)
		menu_bar.add_cascade(label="File", menu=menu_file)
		
		menu_about = Menu(menu_bar, tearoff=0)
		menu_about.add_command(label="Credits", command=lambda: self.popup("Credits", "This project is created by: \n\nDarrel, Jie Shen, KC & Wei Cheng"))
		menu_bar.add_cascade(label="About", menu=menu_about)

		Tk.config(self.root, menu=menu_bar)

	'''
	Method: Setting up the template for the header
	Arguements:
		frame_name: name of the header frame
		title: Text for the header
	'''
	def header_template(self, frame_name, title):
		label_title = Label(self.frame_header_dict[frame_name], 
							text=title,
							font=self.font_family_header)
		label_title.grid(row=0, column=0)

	'''
	Method: Setting up the sidebar
	Arguements:	
		button_dict: A dict with {"name of header and content frame":"text for the button"}
	'''
	def sidebar_template(self, button_dict):

		for name, wording in button_dict.items():
			button_sidebar = Button(self.frame_sidebar, 
									text=wording, 
									height=3, width=15, 
									command=lambda cur_name = name: self.clicked_sidebar_button(cur_name))

			button_sidebar.pack(pady=3)

	'''
	Method: Setting up the footer
	Arguements:
		ack: An acknowledgement sentence that wil be placed at the footer
	'''
	def footer_template(self, ack):
		label_footer_ack = Label(	self.frame_footer, 
									text = ack, 
									anchor=E,
									font=self.font_family_footer)
		label_footer_ack.pack(expand=True, anchor=E)

	'''
	Method: Triggers when the sidebar buttons are being pressed. It will activate
			the function to show the page corresponding to the button pressed
	Arguments:
		buttont_type: Name of the header and content frame to be activated
	'''
	def clicked_sidebar_button(self,button_type):
		self._changeview(button_type)


	def question_template(self, frame_name, questions_list, is_final=False):
		for question in questions_list:
			if question.question_type == Question.QUESTION_TYPE_LIST[Question.RADIOBUTTON]:
				self.singleselection_question_template(frame_name, question)
			elif question.question_type == Question.QUESTION_TYPE_LIST[Question.CHECKBOX]:
				self.mutipleselection_question_template(frame_name, question)
			elif question.question_type == Question.QUESTION_TYPE_LIST[Question.SLIDER]:
				self.slider_question_template(frame_name, question)

		if is_final:
			button_submit = Button(self.frame_content_dict[frame_name], 
								 text="Submit",
								 font=self.font_family_questiontitle,
								 command=self.clicked_submit_button)
			button_submit.pack(anchor=E, padx=20, pady=2)


	def singleselection_question_template(self, frame_name, question):
		
		self.question_printing(frame_name, question)
		self.remarks_printing(frame_name, question.remarks)

		ans = IntVar()
		index = 0
		for option in question.options:
			radiobutton_option = Radiobutton(	self.frame_content_dict[frame_name], 
												text=option, 
												var=ans, 
												value=index, 
												command=lambda cur_ans = ans, cur_question = question: self.clicked_singleselection_question(cur_ans, cur_question))
			if question.answer[index]:
				ans.set(index) 

			radiobutton_option.pack(anchor=W)
			index += 1

		self.print_padding(frame_name, 10)


	def clicked_singleselection_question(self, index, question):
		
		ans_list = []
		for option in question.options:
			ans_list.append(False)

		ans_list[index.get()] = True
		question.answer = ans_list


	def mutipleselection_question_template(self, frame_name, question):

		self.question_printing(frame_name, question)
		self.remarks_printing(frame_name, question.remarks)

		intvar_list = []
		for option in question.options:
			intvar_list.append(IntVar())

		index = 0
		for option in question.options:
			radiobutton_option = Checkbutton(	self.frame_content_dict[frame_name], 
												text=option, 
												var=intvar_list[index], 
												command=lambda cur_intvar_list = intvar_list, cur_question = question: self.clicked_mutipleselection_question(cur_intvar_list, question))
			radiobutton_option.pack(anchor=W)
			index += 1

		self.print_padding(frame_name, 10)


	def clicked_mutipleselection_question(self, intvar_list, question):
		
		ans_list = []
		for intvariable in intvar_list:
			ans_list.append(intvariable.get())

		question.answer = ans_list


	def slider_question_template(self, frame_name, question):

		self.question_printing(frame_name, question)
		self.remarks_printing(frame_name, question.remarks)

		ans = IntVar()
		slider_option = Scale(	self.frame_content_dict[frame_name],
								to=question.options[1],
								from_=question.options[0],
								orient=HORIZONTAL,
								length=300,
								variable=ans,
								command=lambda cur_ans = ans, cur_question = question: self.clicked_slider_question(cur_ans, cur_question))
		slider_option.pack(anchor=W)
		
		self.print_padding(frame_name, 10)


	def clicked_slider_question(self, answer, question):
		question.answer = answer

	def clicked_submit_button(self):
		self._getanswers()

	def clicked_redo_button(self):
		self._redo()

	def clicked_next_button(self):
		self._next()

	def question_printing(self, frame_name, question):
		label_question = Label (self.frame_content_dict[frame_name], 
								text=str(question.question_num) + ". " + question.question,
								font=self.font_family_questiontitle)
		label_question.pack(anchor=W, pady=2)

	def remarks_printing(self, frame_name, remarks):
		if remarks != None:
			label_remarks = Label (self.frame_content_dict[frame_name], 
									text=remarks,
									font=self.font_family_questionremark)
			label_remarks.pack(anchor=W)

	def print_padding(self, frame_name, padding):
		label_padding = Frame(self.frame_content_dict[frame_name])
		label_padding.pack(pady=padding)

	'''
	Method:
	Arguements:
		frame_name: name of the start frame
		text: Text to be presented in the start page
	'''
	def start_template(self, frame_name, instructions, mode, mode_assistance, image_link, count_graph=None, redo_mode=None, have_next_city=None, remarks=None):

		normal_image = Image.open(image_link)
		tkready_image= ImageTk.PhotoImage(normal_image)
		label_picture = Label(self.frame_content_dict[frame_name], image=tkready_image)
		label_picture.image = tkready_image
		label_picture.pack()

		if count_graph is not None:
		 	f = Figure(figsize=(5,3), dpi=80)
		 	ax = f.add_subplot(111)
		 	ax.set_ylabel('Website Matches')
		 	cat = []
		 	count = []

		 	for key, value in count_graph.items():
			 	cat.append(key.partition(' ')[0])
		 		count.append(value)

		 	ax.bar(cat, count)

		 	canvas = FigureCanvasTkAgg(f, self.frame_content_dict[frame_name])
		 	canvas.get_tk_widget().pack(pady=10)

		label_instruction = Label(self.frame_content_dict[frame_name],
							text = instructions,
							font=self.font_family_activitycategory,
							wraplength = 600)
		label_instruction.pack(pady = 10)

		label_remarks = Label(self.frame_content_dict[frame_name],
							text = remarks,
							font=self.font_family_questionremark,
							wraplength = 400)
		label_remarks.pack()

		if count_graph is not None:
			self.print_padding(frame_name, 25)
		else:
			self.print_padding(frame_name, 50)			

		label_mode = Label(	self.frame_content_dict[frame_name],
							text = mode,
							font=self.font_family_questiontitle)
		label_mode.pack()

		label_assistance = Label(self.frame_content_dict[frame_name],
								text = mode_assistance,
								font=self.font_family_questionremark,
								wraplength = 400)
		label_assistance.pack(anchor=S)

		if redo_mode == "offline":

			redo_button = Button(	self.frame_content_dict[frame_name], 
									text="Redo Questionaire",
									command=self.clicked_redo_button,
									height=2,
									width=20)
			redo_button.pack(pady=40, padx=40, side=RIGHT)

			if have_next_city:
				next_button = Button(	self.frame_content_dict[frame_name], 
										text="Show Next City",
										command=self.clicked_next_button,
										height=2,
										width=20)
				next_button.pack(pady=40, padx=40, side=LEFT)
		
		elif redo_mode == "online":
			redo_button = Button(	self.frame_content_dict[frame_name], 
									text="Try Offline Method",
									command=self.clicked_redo_button,
									height=2,
									width=20)
			redo_button.pack(pady=40, padx=40, side=RIGHT)

			if have_next_city:
				next_button = Button(	self.frame_content_dict[frame_name], 
										text="Show Next City",
										command=self.clicked_next_button,
										height=2,
										width=20)
				next_button.pack(pady=40, padx=40, side=LEFT)


	def activity_template(self, frame_name, activity_list):

		self.frame_content_dict[frame_name].grid_columnconfigure(0, weight=1)

		i=0
		for activity in activity_list:
			self.frame_container = Frame(self.frame_content_dict[frame_name])
			self.frame_container.grid(row = i, column = 0, sticky=W+E, pady=5)
			self.frame_container.grid_columnconfigure(0, weight=0)
			self.frame_container.grid_columnconfigure(1, weight=1)

			self.set_activity_frames(self.frame_container)
			label_activity = Label(	self.frame_activity, 
									text = activity.activity_name,
									font = self.font_family_activitytitle,
									wraplength = 400)
			label_activity.pack()

			if activity.address is not np.nan:
				label_address = Label(	self.frame_address,
										text = activity.address,
										font = self.font_family_activityaddress,
										wraplength = 325)
				label_address.pack()

			seperator_address = ttk.Separator(	self.frame_address,
											orient=HORIZONTAL)
			seperator_address.pack(side=RIGHT, fill=X, expand=True, padx=20)

			label_category = Label(	self.frame_category, 
									text = activity.category,
									font = self.font_family_activitycategory)
			label_category.pack(pady=5)

			if activity.description is np.nan:
				activity.description = activity.web_url

			elif type(activity.description) == str and len(activity.description) > 250: 
				activity.description = activity.description[:246] + " ..."

			label_description = Label(	self.frame_description, 
										text = activity.description,
										font = self.font_family_activitydescription,
										wraplength = 325,
										justify=CENTER)
			label_description.pack()
			


			if activity.image_link is not np.nan and activity.image_link is not None:
				try:
					response = requests.get(activity.image_link)
					normal_image = Image.open(BytesIO(response.content))
				except:
					normal_image = Image.open(self.NOIMAGE_LINK)
			else:
				normal_image = Image.open(self.NOIMAGE_LINK)
			
			width, height = normal_image.size
			ratio = self.MAX_WIDTH/width
			resized_image = normal_image.resize((int(width*ratio),int(height*ratio)), Image.ANTIALIAS)
			width, height = resized_image.size
			if height > 1.2*self.MAX_HEIGHT:
				resized_image = resized_image.crop((0, (height-self.MAX_HEIGHT)/2, width, (height+self.MAX_HEIGHT)/2))
			tkready_image = ImageTk.PhotoImage(resized_image)
			label_picture = Label(self.frame_picture, image=tkready_image)
			label_picture.image = tkready_image
			label_picture.pack()
			
			if activity.location is not np.nan:
				label_location = Label(	self.frame_location, 
										text = activity.location,
										font = self.font_family_activitylocation,
										wraplength = 240)
				label_location.pack()
			i += 1


	def set_activity_frames(self, frame):
		self.frame_left = LabelFrame(frame)
		self.frame_right = LabelFrame(frame)
		self.frame_left.grid(row = 0, column = 0, sticky=N+S+W+E)
		self.frame_right.grid(row = 0, column = 1, sticky=N+S+W+E)

		self.frame_picture = Frame(self.frame_left)
		self.frame_location = Frame(self.frame_left) 
		self.frame_picture.grid(row = 0, column = 0, sticky = N+S+W+E)
		self.frame_location.grid(row = 1, column = 0, sticky = N+S+W+E)

		self.frame_activity = Frame(self.frame_right)
		self.frame_address = Frame(self.frame_right)
		self.frame_category = Frame(self.frame_right)
		self.frame_description = Frame(self.frame_right)
		self.frame_activity.grid(row = 0, column = 0, sticky = N+S+W+E)
		self.frame_address.grid(row = 1, column = 0, sticky = N+S+W+E)
		self.frame_category.grid(row = 2, column = 0, sticky = N+S+W+E)
		self.frame_description.grid(row = 3, column = 0, sticky = N+S+W+E)

		self.frame_left.grid_rowconfigure(0, weight=1)
		self.frame_left.grid_rowconfigure(1, weight=0)
		self.frame_left.grid_columnconfigure(0, weight=1)

		self.frame_right.grid_rowconfigure(0, weight=0)
		self.frame_right.grid_rowconfigure(1, weight=0)
		self.frame_right.grid_rowconfigure(2, weight=0)
		self.frame_right.grid_rowconfigure(3, weight=1)
		self.frame_right.grid_columnconfigure(0, weight=1)

	def raise_frame(self, frame_name):
		self.frame_header_dict[frame_name].tkraise()
		self.frame_content_dict[frame_name].tkraise()

	def popup(self, title, message):
		messagebox.showinfo(title, message)

	def load_template(self, frame_name, default_text, additonal_text, image_link):
		label_text = Label(	self.frame_content_dict[frame_name], 
							text = default_text,
							wraplength = 400)
		label_text.pack()

		label_additonal = Label(self.frame_content_dict[frame_name], 
								text = additonal_text,
								wraplength = 300)
		label_additonal.pack()



		self.print_padding(frame_name, 2)

		normal_image = Image.open(image_link)
		width, height = normal_image.size
		ratio = self.MAX_WIDTH/width
		resized_image = normal_image.resize((int(width*ratio),int(height*ratio)), Image.ANTIALIAS)
		tkready_image= ImageTk.PhotoImage(resized_image)

		label_picture = Label(self.frame_content_dict[frame_name], image=tkready_image)
		label_picture.image = tkready_image
		label_picture.pack()

		skip_button = Button(	self.frame_content_dict[frame_name], 
								text="Skip",
								command=self.clicked_submit_button,
								height=3,
								width=30)
		skip_button.pack(pady=2)

		self.frame_content_dict[frame_name].update_idletasks()
		self.frame_content_dict[frame_name].update()
