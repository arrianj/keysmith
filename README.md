# Keysmith
> A personal dictionary attack value generator.

Keysmith is less of a proof-of-concept project, and more of a proof-of-me-being-able-to-code project. It takes inputs of personal information, and breaks the inputs down into potential representations of the received data (i.e. First Name: Aaron returns AARON, aaron, Aaron, noraa, noraA, a., a, A, etc.) It then combines all possible permutations of the data it receives, saves them to a .txt file, and you have my basic attempt at building a personalized dictionary attack list.

Keysmith makes no attempt to do anything with the values it generates. I do not claim that it generates comprehensive dictionaries, but this was a fun project to become more comfortable and familiar with python in. Feel free to play with the script, run it, browse it, fork it, and let me know your thoughts.

## Installing

$ pip install -r requirements.txt
$ python app.py

### Features

Currently, the only inputs it takes are first name and last name. I plan on adding more inputs such as birthday, numeric characters, special characters, and custom inputs.

## License

The code in this project is licensed under the MIT license.