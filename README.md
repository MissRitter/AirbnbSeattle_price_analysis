# Airbnb Prices in Seattle





- [Motivation](#Project-Motivation)
- [Installation](#Installations)
- [Included](#File-Descriptions)
- [Instructions](#How-To-Run-This-Project)
- [ToDo](#ToDo)
- [Copyright and license](#License)

---

## Project Motivation

AirBnB is a platform service connecting hosts and guest from the entire world.<br>
This project tries to assist a host who wishes to optimize his/her offer to
improve<br>
value and get the best price possible in the market using the Airbnb Seattle<br>
data form [kaggle.com](https://www.kaggle.com/airbnb/seattle/data).

This project is an assignment from the Udacity Data Science Nano Degree.<br>

### Project Description
1. The data set could be chosen freely
1. Answer at least three questions based on the data
1. The project structure should follow the CRISP-DM process

Deliveries: This repository on GitHub and a related blog post

---

## Installation
This project is based on:<br>

| Module | Version|
|---|---|
|Jupiter | 1.0.0 |
|Python | 3.8.5 |
|Pandas | 1.2.2 |
|Numpy  | 1.19.2 |
|Scikit-learn  | 0.23.2 |
|Matplotlib | 3.3.4 |
|Seaborn | 0.11.1 |

---

## File Descriptions
The Repository contains a set of Jupyter Notebooks, some Python script files
and a subdirectory with three csv data files.
### Jupyter Notebooks
All importent steps are explained in Jupyter notebooks.
- 00_explore_data.ipynb
- 01_explore_categorical_values.ipynb
- 02_price_correlations.ipynb


### Functions on The Data Set
There are three python scrips which contain functions performing actions on the data<br>
which have also been explored in corresponding notebooks. These functions are used<br>
to encapsulate learnings from privieous notebooks and are imported into the following ones.<br>
- CategoricalPrep.py


### Auxilliary Functions
These two files only hold auxilliary functions.
- ExploreData.py
- TransformeData.py

### Data
The data can also be accessed via
[kaggle.com](https://www.kaggle.com/airbnb/seattle/data)
- /data
    - calendar.csv
    - listings.csv
    - reviews.csv

---

## How To Run This Project
To follow this projects process you only need to access the Jupyter Notebooks.<br>
All other scrips are included into the notebook if needed.<br>
The notebooks are numbered. To go through the entire project,
just follow the numbers.<br>
If you are only interessted in certain parts of the process,
here comes a quick summary of each notbook:

### 00_explore_data.ipynb
A brief look at all data files to get an impression how they are conected and
what one can to with it.
### 01_explore_categorical_values.ipynb
Phrasing questions and preparing the data for further analysis.
### 02_price_correlations.ipynb
Analysing the correlations within the data, to answer the previously
posed questions.

---

## ToDo
The answer to question tree is still missing.
### 03_data_cleaning.ipynb
To answer the third question the data has to be cleaned completeley.<br>
That is done in this notebook.
### 04_price_model.ipynb
Modell training and avaluation on the final data set, to answer the last question.

---

## License

MIT




