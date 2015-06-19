# -*- coding: utf-8 -*-
import git, os, shutil
 
DIR_NAME = "PATH_TO_GIT_CLONE/docs"
REMOTE_URL = "https://github.com/drwasho/openbazaar-documentation.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)

renameReadme = "PATH_TO_GIT_CLONE/docs/README.md"
base = os.path.splitext(renameReadme)[0]
os.rename(renameReadme, base + ".txt")

renameDex = "PATH_TO_GIT_CLONE/docs/01 About.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/index")[0]
os.rename(renameDex, base + ".md")

renameStart = "PATH_TO_GIT_CLONE/docs/02 Getting Started.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/Getting Started")[0]
os.rename(renameStart, base + ".md")

renameProto = "PATH_TO_GIT_CLONE/docs/03 Protocol.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/Protocol")[0]
os.rename(renameProto, base + ".md")

renameMarket = "PATH_TO_GIT_CLONE/docs/04 Marketplaces.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/Marketplaces")[0]
os.rename(renameMarket, base + ".md")

renameRoad = "PATH_TO_GIT_CLONE/docs/05 Roadmap.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/Roadmap")[0]
os.rename(renameRoad, base + ".md")

renameDev = "PATH_TO_GIT_CLONE/docs/06 Developers.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/Developers")[0]
os.rename(renameDev, base + ".md")

renameArticles = "PATH_TO_GIT_CLONE/docs/07 Articles.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/Articles")[0]
os.rename(renameArticles, base + ".md")

renameReference = "PATH_TO_GIT_CLONE/docs/08 References.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/References")[0]
os.rename(renameReference, base + ".md")

renameFAQ = "PATH_TO_GIT_CLONE/docs/09 FAQ.md"
base = os.path.splitext("PATH_TO_GIT_CLONE/docs/FAQ")[0]
os.rename(renameFAQ, base + ".md")

os.system("cd PATH_TO_GIT_CLONE && /usr/bin/python /usr/local/bin/obdocs build --clean")

print "---- DONE ----"