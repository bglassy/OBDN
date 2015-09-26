# OpenBazaar Docs
### OpenBazaar Documentation - a python based documentation compiling platform.

###Installation
You will need Python and PIP installed. The Docs platform supports Python 2.6, 2.7, 3.3 and 3.4.

In terminal type:

 
```git clone https://github.com/bglassy/OpenBazaar-Docs.git```
 
 
 Followed by:

```sudo pip install --editable .```


###Configuration
You will need to edit two files in order to correctly configure paths.

```The first file is 'automate.py' inside the 'root' directory.```

```The second file is 'defaults.py' inside the 'obdocs/config' directory```

You will need to replace every instance of **PATH_TO_GIT_CLONE** in each file with the location of the repository clone.