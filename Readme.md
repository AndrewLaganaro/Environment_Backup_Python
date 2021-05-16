# Python Environment Backup

It's always good to mantain your **Python** and **R** Anaconda environment packages properly listed and well kept in case you have any problems with your computer or Anaconda's installation.

This simple script does just that by generating two files in a known folder, although I think anaconda should provide a clearer way to do it with more easiness:

* Environment.yml
* Packages.txt

Both these files can be used to restore a full Python and R installation via Anaconda on Windows and Linux.

In general the .yml file tends to bring problems with Anaconda mainly because of some packages metadata that may have come incorrect on their text file, wheres the packages.txt file always works, you'll always have to remember your Python and R version as this file doesn't provide that information by default.

You can get more information on how to correct the .yml text file issue with some regex functions on the link below, then the .yml file works flawlessly:

- [Solve broken Env.yml file](https://github.com/conda/conda/issues/9624#issuecomment-801623523)

Also it's possible do schedule the script execution in Windows and Linux in order to take consistent snapshots of your Python configuration given certain interval per say, days, weeks or months.

- [Schedule Backup Script in Windows](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279)

- [Schedule Backup Script in Linux](https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915)

Although I advise doing that with caution because again, some snapshots may be taken in a bad moment of your system, say when you've downloaded a package that broke compatibility between other packages previously installed, for instante: a new package that relies on an *older version of pandas*, then by obligatorily downgrading it causes the break of scikit-learn and every other package that relied on your previous updated pandas version.

Because of that it's always good to mantain a 'main' version of your environment from time to time to prevent those issues to happen.

### **Planned improvements:**

1. The script may also be modified in order to change filenames periodically, say "Env_01/02/2021", "Env_01/02/2021" to help with maintainability

1. Add a file emission containing solely the Python version in case the .yml file doesn't works and you also can't fix it, you can use the Packages.txt and the ner Versions.txt in order to fully restore your configuration manually via conda

The files present on this repo are also my own backups that I did for myselft from my environment, currently I'm using Python 3.6 but I'm planning to change to Python 3.7 or maybe 3.8 soon enough. The long package list besides referring to the main ones also refers to dependencies and dependencie's dependencies. Feel free to use them as you wish.