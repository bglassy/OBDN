# -*- coding: utf-8 -*-
import git, os, shutil
 
DIR_NAME = "PATH_TO_GIT_CLONE/docs"
REMOTE_URL = "https://github.com/OpenBazaar/OpenBazaar.wiki.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)

renamek = "PATH_TO_GIT_CLONE/docs/01.-What-is-OpenBazaar.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/index")[0]
os.rename(renamek, base + ".md")

rename1 = "PATH_TO_GIT_CLONE/docs/Instrucciones-para-desarrollo.md"
base = os.path.splitext(rename1)[0]
os.rename(rename1, base + ".txt")

rename2 = "PATH_TO_GIT_CLONE/docs/_Footer.md"
base = os.path.splitext(rename2)[0]
os.rename(rename2, base + ".txt")

rename3 = "PATH_TO_GIT_CLONE/docs/_Sidebar.md"
base = os.path.splitext(rename3)[0]
os.rename(rename3, base + ".txt")

rename4 = "PATH_TO_GIT_CLONE/docs/_Español-Instrucciones.md"
base = os.path.splitext(rename4)[0]
os.rename(rename4, base + ".txt")

rename5 = "PATH_TO_GIT_CLONE/docs/Windows-support.md"
base = os.path.splitext(rename5)[0]
os.rename(rename5, base + ".txt")

rename6 = "PATH_TO_GIT_CLONE/docs/Home.md"
base = os.path.splitext(rename6)[0]
os.rename(rename6, base + ".txt")

rename7 = "PATH_TO_GIT_CLONE/docs/10.-Contact-Us.md"
base = os.path.splitext(rename7)[0]
os.rename(rename7, base + ".txt")


os.system("cd PATH_TO_GIT_CLONE && /usr/bin/python /usr/local/bin/obdocs build --clean")

print "---- DONE ----"