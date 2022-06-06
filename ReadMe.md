# Shift start

I often have to click around applications to prepare myself during the start of my work shift. This code is a template program to help start all desired applications automatically with a waiting period between each iteration using a .bat executable file and save time clicking around applications (More time for a cup of tea).

## Prerequisite

To be able to run this program you would need to have the applications listed below installed on your laptop or desktop computer.

- [Git](https://git-scm.com/downloads).
- [Python](https://www.python.org/downloads/).
- Notepad / Notepad++.

## Usage

From your favourite terminal, Clone this git repo using the command below:

```python
git clone https://github.com/fodare/shift-start.git
```

Once the repo is successfully cloned, you can navigate to the cloned dir using the command:

```Python
cd shift-start
```

Modify the *start.py* file to add the path to your local applications you would like to start automatically.
Example below:

```Python
app_list = {r"c:\path to app 1",
            r"c:\path to app 2",
            r"c:\path to app 3",
            r"c:\path to app 4",
            r"c:\path to app 5",
            r"c:\path to app 6",
            r"c:\path to app 7"}
```

Further down the code, you can modify the sleep period to either increase or decrease the sleep period. Example below:

```python
 time.sleep(4) # Wait for 4s before opening the next application in the list.
```

Save the program and modify the *script.bat* file. You can change the file name if desired.

In the .bat file, you would need to provide the path to where your python.exe file is located and the path to where your python code is stored. Example below:

default template

```python
"path to where your python.exe file is located" "path to where your executable python code is stored."
```

will change to

```python
"c:\Python39\python.exe" "c:\Users\demo\Desktop\start.py"
```

## Run .bat command

To reduce the number of clicks, you can add the .bat file to your Desktop and when you are resuming your shift, you can double-click the file and the program would be executed.
