#INF360 - Programming in Python
#Lauren Robben
#Final Project

#This is the logging.debug section
import logging
import sys
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format =' %(asctime)s - %(levelname)s - messages)s')

#Main loop to start the program #This is where thet will be asked their name to start
#Wanted for this to appear first in program then go to menu where they can selct the direction they wanted to go but was not able to.
def main():
	print("Welcome to your own personal Fitness Routine.\n")
	while True:

#input must be one name
		print('What is your name?')
		name= input()
#.isalpha makes sure the name is only letters
		if name.isalpha():
			break
	else:
		print('You must type your name to begin customizing your Fitness Routine\n')
	print('Welcome' + name + '. Lets build your fitness routine.\n') #want their name to appear after Welcome
#This is supppsed to be the layout of what the Display of the routine would like when pressed
workout_list = ["Name of Level", "Number of sets" ,"Duration of each workout","Workouts"]

#Classify the different level types
class Levels:
	def __init__(self, name, workouts):
		self.name= name
		self.wor= workouts
#Catagorize the specific words you only want your users to use and divide them into levels.
#Having trouble getting this to show up on the Add Workout Selection		
workout_dict ={
	"Beginner": ['Stretch', 'Walking Lunges', 'Hammer Curls', 'Bent-Over Row', 'Squat Jumps', 'Plank', 'Push-Ups'],
	"Moderate": ['Stretch', 'High Knees', 'Hammer Curls', 'Bent-Over Row', 'Squat Jumps', '40 pound Deadlift','Plank', 'Bicycle Crunches'],
	"Advanced": ['Stretch', 'Jump Rope', 'Walking Lunges','High Knees', 'Box Jumps', 'Hammer Curls', 'Bent-Over Row', 'Squat Jumps', '60 pound Deadlift','Plank', 'Mountain Climbers',],
		}
#These are the different types of workouts and instructions that correspond to each level
#Want for Workout1 to correlate with Beginner when user types it in at begining of program.
workout1 = {'Name': 'Beginner',
	    'Number of Sets': '3',
	    'Duration of each workout': '30 seconds',
	    'Workouts': ['Stretch', 'Walking Lunges', 'Hammer Curls', 'Bent-Over Row', 'Squat Jumps', 'Plank', 'Push-Ups'],
		}
workout2 = {'Name': 'Moderate',
	    'Number of Sets': '4',
	    'Duration of each workout': '45 seconds',
	    'Workouts': ['Stretch', 'High Knees', 'Hammer Curls', 'Bent-Over Row', 'Squat Jumps', '40 pound Deadlift','Plank', 'Bicycle Crunches'],
		}
workout3 = {'Name': 'Advanced',
	    'Number of Sets': '6',
	    'Duration of each workout': '1 minute',
	    'Workouts': ['Stretch', 'Jump Rope', 'Walking Lunges','High Knees', 'Box Jumps', 'Hammer Curls', 'Bent-Over Row', 'Squat Jumps', '60 pound Deadlift','Plank', 'Mountain Climbers',],
		}
#This classifies the different workouts i want to be displayed
workout_list = [workout1, workout2, workout3]

#This is where the user should be able to select their level of difficulty and see the options before choosing.
#Having trouble displaying the level options below for the user to see what number correlates with what level
def pickLevel():
	levels = {'Enter 1 for': 'Beginner' ,
		  'Enter 2 for': 'Moderate',
		  'Enter 3 for': 'Advanced'}
	leftWidth = 20
	rightWidth = 5
	print()
	while True:
		try:
			levelT = input('Choose your routine type by selecting 1, 2, or 3:')
			if int(levelT) < 1 or int(levelT) > 3:
				print('You must choose a level type by selecting 1, 2, or 3:')
			elif levelT =='1':
				print('You have chosen Beginner.')
				print(workout1)
				break
			elif levelT =='2':
				print('You have chosen Moderate.')
				break
			elif levelT =='3':
				print('You have chosen Advanced.')
				break
		except ValueError:
			print('You must choose between 1, 2, or 3:')
			print()

#This is the line of code that correlates to the View Fitness Routine button in Selection List
#It is not showing the workout when I select the number on the list.
def displayWorkouts():
	global workout_list
	print()
	print('*** Custom Fitness Routine ***')

#This is the line of code that correlates to the Add Workout button in Selection List
#It is on continous loop and i have trouble exiting it after one time.
def addWorkout():
        global  workout_list
        while True:
                workout = input('What workout would you like to add:')
                print(workout + ' has been added to your Fitness Routine.')
#Having trouble with the indent error for the code below
else:
		print("That is not a valid workout. Please try again!") 

#This is the line of code that correlates with the Remove Workout button in Selection List
#Don't know how to link the workout_dict to this so it recognizes the words.
def removeWorkout():
	global workout_list
	displayWorkouts
	while True:
		workout = input('Which workout would you like to remove: ')
		try:
			if int(workout) in range(len(workout_list)+1):
				print(workout_list[int(workout)-1] + ' has been removed from your Fitness Routine')
				del workout_list[int(workout)-1]
				break
			else:
				print('That is not a valid choice. Please try again!')
		except:
			print('That is not a valid choice. Please try again!')

#This is the section that correlates with the Import command on the Selection List
def importWorkout():
	global workout_list
	Workout = input('What workout of your own would like to add: ')
	print(workout_dict)
	add workout_list.add(Workout) #Having trouble getting the program to recognize this code
	print(Workout + ' has been added to your fitness routine')

#This is the line of code that correlates with the Clear List button in Selection List
def clearList():
	global workout_list
	workout_list.clear()
	print('Your Fitness Routine is cleared')


#Menu is supposed to show after inputing their name
#Want their name to be displyed after 'Hello'.
def selectionList(): 
	print()
	print('''*** Customized Fitness Routine ***
                Hello Lauren, what would you like to do today? 

		1. Select Level of Workout Difficulty
		2. View your Fitness Routine
		3. Add Workout to Fitness Routine
		4. Remove Workout from Routine
		5. Import Personal Workout
		6. Clear Fitness Routine
		7. Exit
		''')
#This is the code that correlates with the different sections of code above and links them to the designated selection list numbers.
#Want this to appear after start of program where I ask for their name.
while True:
	selectionList()
	selection = input("Choose your action: ")
	if selection == "1":
		pickLevel()
	elif selection == "2":
		displayWorkouts()
	elif selection == "3":
		addWorkout()
	elif selection == "4":
		removeWorkout()
	elif selection == "5":
		importWorkout()
	elif selection == "6":
		clearList()
	elif selection == "7":
		print("Thanks for your using my program!")
		sys.exit()
	else:
		print("Please try again.") 

#This is the code for logging.critical
try:
	import functions as fn
except :
	logging.critical('Missing functions.py!')
	print('Missing functions.py! Program is closing')
	sys.exit()
