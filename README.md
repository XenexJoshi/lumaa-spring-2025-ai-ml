This program contains a simple movie recommendation model that takes in a text description
from the user, and outputs 5 movies with similar premise as the description, based on the
plot synopsis, and relevant tags associated with the movie. The dataset for the program
was obtained through: https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags?resource=download,
and the dataset was shortened by sampling ranodmly 500 datapoints to generate a simple recommendation
model.

You can update the number of recommendations by updating the COUNT field in the main.py
file. Additionally, you can update the program to return movie synopsis by uncommenting
a commented section in the model.py file.

To run this program, firstly set up a virtual environment using the following commands:
      python3 -m venv venv
      source ./venv/bin/activate

The above code is specific to mac only. Similar command for other OS can be found
through a simple google search. After setting up the virtual environment, use the pip
command to install the required libraries from requirements.txt, and you're set to
run the program.

Navigate to the main.py file, and run the program. The program will prompt you to 
input the movie prompt, and you will obtain the recommendations after typing in the description.

Salary expectations: $25/hr