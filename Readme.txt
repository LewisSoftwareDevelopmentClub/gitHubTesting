For public github repository you do not have to invite in order to clone.


# When there are file clashes between the local and github repository you will the message :


The following untracked working tree files would be overwritten by merge:
        newFile.py
Please move or remove them before you merge.


# If you did not add newFile.py  , you can delete it , then the pull will go through

# if you did a git add newFile.py  then removed newFile.py then performed a git pull
the will still be a conflict

In order to remove this conflict   
git rm --cached newFile.py
git commit -m " updat message"
git push

NOTE THIS WILL NOT DELETE newFile.py from the github repository



-- YOU CAN NOT DO A GIT PUSH IF THERE ARE THINGS IN THE GIT HUB REPOSITORY THAT NEED A GIT PULL
-- TIP - DO A GIT PULL FIRST BEFORE YOU START WORKING



------- Creating a branch  -----------
git branch < Branch name >


