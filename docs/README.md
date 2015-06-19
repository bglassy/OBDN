# OpenBazaar Docs
### A platform for building auto-updated static OpenBazaar documentation

###Installation
You will need Python and PIP installed.

In terminal type:

 
```git clone https://github.com/bglassy/openbazaar-docs```
 
 
 Followed by:

```sudo pip install --editable .```


###Configuration
You will need to edit two files in order to correctly configure paths.

```The first file is 'automate.py' inside the 'root' directory.```

```The second file is 'defaults.py' inside the 'obdocs/config' directory```

You will need to replace every instance of **PATH_TO_GIT_CLONE** in each file with the location of the repository clone.

