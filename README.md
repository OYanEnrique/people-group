# 📊 Group Data Analyzer

A command-line application for collecting demographic data (name, gender, age) for a group of people. After data entry is complete, it performs and displays a statistical analysis on the group.

## Features

* **Continuous Data Entry**: Users can enter data for an unlimited number of people in a single session.
* **Statistical Summary**: After data collection, the script calculates and displays:
    * The total number of people registered.
    * The average age of the group.
    * A list of all women in the group.
* **Above-Average Filter**: The script identifies and lists all individuals whose age is higher than the group's average.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `group_people.py`).
3.  Run the script from your terminal:
    ```sh
    python group_people.py
    ```
4.  The program will prompt you to enter the name, gender (m/f), and age for each person.
5.  After each person, it will ask if you want to continue. Enter `y` for yes or `n` to stop.
6.  When you enter `n`, the script will display the final analysis.

### Example Session

```sh
> python group_people.py
------Group of People Data------
Name:
John
Gender:
m
Age:
30
Continue? [y/n]y
Name:
Maria
Gender:
f
Age:
25
Continue? [y/n]y
Name:
Peter
Gender:
m
Age:
40
Continue? [y/n]n
See you soon!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
3 People registered
The average age of the Group is 31.67
Woman in this group: ['Maria']
The following person(s) have age above average!
   name: Peter; gender: m; age: 40; 
Finished
```
