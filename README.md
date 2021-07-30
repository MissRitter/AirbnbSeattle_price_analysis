# Airbnb Prices in Seattle


- [Motivation](#Project-Motivation)
- [Installation](#Installations)
- [Included](#File-Descriptions)
- [Instructions](#How-To-Run-This-Project)
- [License](#License)



## Project Motivation

Airbnb is a platform service connecting hosts and guest within the entire world.<br>
This project takes the perspective of a host who wishes to optimize his/her offer to
improve the value and optimize the price within the market.
Finally it attempts to predict the price for a new Airbnb offer using the existing listings data and a machine learning approach.<br>
For these attempts it is restricted to the area of Seattle due to the data-set it is based on.<br>

The data for this project is form [kaggle.com](https://www.kaggle.com/airbnb/seattle/data).

This project is an assignment from the [Udacity](https://www.udacity.com/) Data Science Nano Degree.<br>

There is also a blog post about this project on [Medium.com](https://medium.com/@MissRitter/make-the-most-of-airbnb-95a443b86bbe).



## Installation

If you are currently reading this on GitHub, you find all the information to get this repository at the top of the page where it says *Code*:

![Code](https://github.com/MissRitter/AirbnbSeattle_price_analysis/blob/media/code.png)

You can get this repository downloading a zip-file or by cloning it with this command:<br>
```
git clone https://github.com/MissRitter/AirbnbSeattle_price_analysis.git
```

Make sure that you have all necessary packages installed and with the correct version.<br>
This project is based on:<br>

| Module: |[jupyter][l:jupyter] |[python][l:python] |[pandas][l:pandas] |[numpy ][l:numpy] |[scikit-learn][l:scikit]  |[matplotlib][l:matplotlib] |[seaborn][l:seaborn] |
| --- |---|---|--- |---  |---  |--- |--- |
| **Version:** |1.0.0 |3.8.5 |1.2.2 |1.19.2 |0.23.2 |3.3.4 |0.11.1 |

[l:jupyter]:https://jupyter.org/
[l:python]:https://www.python.org/
[l:pandas]:https://pandas.pydata.org/
[l:numpy]:https://numpy.org/
[l:scikit]:https://scikit-learn.org/
[l:matplotlib]:https://matplotlib.org/
[l:seaborn]:https://seaborn.pydata.org/

## File Descriptions

The Repository contains a set of jupyter notebooks, some python script files
and a subdirectory with three csv files.

### Jupyter Notebooks

All steps of the process are explained in jupyter notebooks.
- 00_explore_data.ipynb
- 01_explore_categorical_values.ipynb
- 02_price_correlations.ipynb
- 03_data_cleaning.ipynb
- 04_price_model.ipynb


### Functions on The Data Set

There are three python files with functions summarizing actions on the data<br>
which have also been explored in corresponding notebooks. These functions
summarize learnings from previous notebooks and are imported into following ones.<br>
- CategoricalPrep.py
- FeatureEngine.py
- PrepAndModel.py

### Auxiliary Functions

These two files hold auxiliary functions.
- ExploreData.py
- TransformData.py

### Data

The Airbnb Seattle data can also be accessed via
[kaggle.com](https://www.kaggle.com/airbnb/seattle/data)
- /data
    - calendar.csv
    - listings.csv
    - reviews.csv

The subdirectory gridsearch holds two csv files. They are not mandatory for this project to work, since they are generated in jupyter notebook 05.
- /gridsearch
    - grid_search_best_parameter.csv
    - grid_search_parameter_results.csv



## How To Run This Project

To follow this projects process you only need to access the jupyter notebooks.
All other scrips are included into the notebook if needed.
The notebooks are numbered. To go through the entire project,
just follow the order.<br>
If you are only interested in certain parts of the process,
here comes a quick summary of each notebook:

### 00_explore_data.ipynb
A brief look at all data files to get an impression how they are connected and
what one can do with them.

### 01_explore_categorical_values.ipynb
Phrasing questions and preparing the data for further analysis.

### 02_price_correlations.ipynb
Analyzing correlations within the data, to answer the previously
posed questions.

### 03_data_cleaning.ipynb
Final preparation steps before using the data for machine learning.

### 04_price_model.ipynb
Training and scoring of a decision tree regressor to predict a price.



## License

This project is published in 2021 under the [MIT](https://opensource.org/licenses/MIT) license.




