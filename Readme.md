# Python Environment Backup

##### Author: Andrew Laganaro

#### [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)

## 📜 About this project

#### A simple script generates a backup of a given Python environment

>It’s always good to maintain your **Python** environment packages properly listed and well-kept in case you have any problems with your computer or Anaconda’s installation.

#### 🚀 Built with
- 🐍Python
- 🪐Jupyter Notebook
- 🖼Drawio

### 🛠 Projects

  [![Store Sales Analysis](https://img.shields.io/badge/Projects-Store%20Sales%20Analysis-orange)](https://github.com/AndrewLaganaro/Store_Sales_Analysis)
  
  [![Data Science Framework](https://img.shields.io/badge/Projects-Data%20Science%20Framework-blue)](https://github.com/AndrewLaganaro/Data_Science_Framework)
  
  [![Data Science Classes](https://img.shields.io/badge/Projects-Data%20Science%20Classes-red)](https://github.com/AndrewLaganaro/Data_Science_Classes)

####  ⬇️ Take a look at my Portfolio ⬇️
  
  [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)
  
#### 📝 How to use this Project

This simple script does just that by generating two files in a known folder:

* Environment.yml
* Packages.txt 

Both these files can be used to restore a full Python installation via Anaconda on Windows and Linux.

##### 💻 Pre-requisites

Before starting, make sure you've met the following requirements:

- You have installed the latest version of Python, pandas, numpy, matplotlib, seaborn, and Jupyter Notebook.
    - At least Python 3.6 is required.
- You have either Windows, Linux or Mac machine.

##### 🚀 Installing Environment Backup Python

To install Environment Backup Python, follow these steps:

- 📁 Select a folder which you want your backup script to live in.
```
...
📁 Data Science ⬅️ 💻 Start your terminal here 💻
    📁 Diamond_Analysis
    📁 Python_Studies
    📁 Iris_Analysis
    ...
```
    
- 💻 For now the script isn't directly installable, but you can download it directly by cloning this repository:

```
git clone https://github.com/AndrewLaganaro/Environment_Backup_Python
```

```
...
📁 Data Science
    📁 Diamond_Analysis
    📁 Python_Studies
    📁 Iris_Analysis
    📁 Environment_Backup_Python
    ...
```

#### ☕ Using Environment Backup Python

In general the .yml file tends to bring problems with Anaconda mainly because of some packages’ metadata that may have come incorrect on their text file, whereas the packages.txt file always works, you’ll always have to remember your Python version as this file doesn’t provide that information by default.

You can get more information on how to correct the text file problem in the .yml's case with some regex functions on the link below, then the .yml file works flawlessly:

- [Solve broken Env.yml file](https://github.com/conda/conda/issues/9624#issuecomment-801623523)

Also, it’s possible do schedule the script execution in Windows and Linux in order to take consistent snapshots of your Python configuration given certain interval per say, days, weeks or months.

- [Schedule Backup Script in Windows](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279)

- [Schedule Backup Script in Linux](https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915)

Although I advise doing that with caution because again, some snapshots may be taken in a bad moment of your system, say when you’ve downloaded a package that broke compatibility between other packages previously installed, for instance: a new package that relies on an *older version of pandas*, then by obligatorily downgrading it causes the break of scikit-learn and every other package that relied on your previous updated pandas version.

Because of that, it’s always good to maintain a ‘main’ version of your environment from time to time in order to prevent those issues to happen.

##### ⭐️ Features to be added

- [ ] The script may also be modified in order to change filenames periodically, say “Env_01/02/2021”, “Env_01/03/2021” to help with maintainability

- [ ] Add a file emission containing solely the Python version in case the .yml file doesn’t work and you also can’t fix it, you can use the Packages.txt and the new Versions.txt in order to fully restore your configuration manually via conda

- [ ] Add the Brazilian translation version to a new .md file

- [ ] Add a second script in order to execute the backup's installation considering the case in which both three generated files are used

> [Brazilian Readme](ReadmeBr.md)

---

####  ⬇️ Take a look at my Portfolio ⬇️
  
  [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)
  
