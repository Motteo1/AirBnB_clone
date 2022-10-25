### AirBnB Clone
##### Description:
> This repo holds a command interpreter like a shell that can be activated, take in user input and perform certain tasks to manipulate the object instances

***

#### How to use command interpreter


#### Installation


#### Usage
##### Interactive Mode
	`
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	
	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$
	`
##### Non-Interactive Mode
	`
	$ echo "help" | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	`

### Environment
* Language: Python3
* OS: Ubuntu 20.04 LTS
* Style Guidelines: [Pycodestyle](https://pypi.org/project/pycodestyle/) ||

### Authors
LeRoy-M & 
Motteo1
