# time2lib
A small program that reminds you that it's time to live!

## Overview
A small set of instructions that can be executed in the background which reminds the user to take a break
from the heavy computing we all do in this age.

## Usage
It's mostly meant for Python developers to integrate into their code. Right now, it doesn't have much functionality, and the 
implementation saved as "main.py" is pretty basic- just to give you an idea of how it can be used.

To execute the sample program, write
`$ python3 main.py`

Enter the time duration for each session as hour:minute in whole numbers.

## Install
To install time2lib, clone this git repository using git-

#### On GNU\Linux and Mac OS:
```
git clone https://github.com/gotlougit/time2lib.git 
```

`cd` into the directory created and-

`$ python3 setup.py install`

#### On Windows:
Not supported yet! The install instructions should translate over the same.

Download the code as a .zip file from GitHub, extract it and run setup.py just like in the 
above instructions.

## Roadmap

* Add notification support
* Make a reference GUI for easy usage
* Add the ability to run the program automatically in the background.
* Build a fully featured reference implementation that can be used to build other versions for all platforms
