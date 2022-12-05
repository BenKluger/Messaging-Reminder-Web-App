cd C:\Users\Ben\CodingProjects\my_flask

Ben@DESKTOP-8K54FHO MINGW64 ~/CodingProjects/my_flask
$ python -m venv virtual

Ben@DESKTOP-8K54FHO MINGW64 ~/CodingProjects/my_flask
$ ls
**pycache**/ app.py templates/ virtual/

Ben@DESKTOP-8K54FHO MINGW64 ~/CodingProjects/my_flask
$ source virtual/Scripts/activate
(virtual)
Ben@DESKTOP-8K54FHO MINGW64 ~/CodingProjects/my_flask
$ flask run

///////// To make it run dynamically:
(virtual)
Ben@DESKTOP-8K54FHO MINGW64 ~/CodingProjects/my_flask
$ export FLASK_ENV=development
(virtual)
Ben@DESKTOP-8K54FHO MINGW64 ~/CodingProjects/my_flask
$ export FLASK_APP=app.py
(virtual)

source virtual/Scripts/activate
export FLASK_ENV=development
export FLASK_APP=app.py
