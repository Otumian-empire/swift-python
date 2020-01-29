# Exercise 23 (Git)
As developers, we may want to have different versions of our software and keep them too. We may want to revert to a previous state of a file or even the whole project and a Distributed Version Control System (DVCS) will do that job. One DVCS is [Git][git-site]. We shall look into how to use git minimally.

We would want to keep our projects on our local server, our disk could corrupt. Thus we would need a remote server for keeping our softwares or scripts thus we create a free [Github][github-site] account before we proceed any further, for our own good as developers who may wish other developers see and review or even share.

## Install git

We shall install Git using [this website][git-site], depending on the OS. Afterwards, we do `git --verion` on the commandline to check if git has been installed successfully.

## Configure git

Open the commandline - power shell for windows.

* Set user name: `git config --global user.name your_user_name` 
* Set user email: `git --global user.email your_user_email` 

This actually can be changed for every software we want to create using git, else this configuration is default.

## Create repository

A repository is basically a folder that contains our code and any other file we may need for the development of our software.

There may be two or more instances where we would need to create a git repository:

* when we have already created the folder on our PC, local server, but not under version control.
* when our project is already online ( remote) under version control.

### Local repository

When the project is created on our local server and we want it under version control, we do the following:

* change directory into the folder of interest, `cd ...` 
* do, `git init` - to start git

### Remote repository

When the project already exist online, say on [Github][github-site], do the following:

* Navigate to where we want to create the project
* do, `git clone https://...` - to have the same version of the remote project
* or we can do, `git clone https://... repo_name` - where repo name is the name of the new folder we want to keep we files in instead of the original. This doesn't alter naything.
* then navigate into `repo_name` - this repository comes with the enire version history of the repository.

## Adding an existing project to remote server

Here we already have the project or say we have finished developing it locally then we want to push it to the remote repository, do the following:

* initialize the git repo locally, `git init` 
* add the files in the local repository, `git add .` 
* then stage them, `git commit -m "some message"` 
* now copy the remote repository url and do, `git remote add origin https://...` , where `https://../` is the remote url
* now send it to the remote repository, `$ git push origin https://...` 

## Git status

Every file in a VCS has a status which tells we what has been done to the file thus what state the file is in.

### Table of file status

| Status        | Description |
| ------------- | ----------- |
| `tracked` | file git knows about |
| `untracked` | file git doesn't know about |
| `unmodified` | an unchanged tracked file |
| `modified` | a changed tracked file |
| `staged` | a saved tracked file |

## Check file status

we do, `git status` to see the status of the files in the current repository.

## Track files

we do, `git add file_name` to track a single or `git add .` to track the entire files in this particular directory.

When we edit the file, the file status will become `modified` , then we do, `git add file_name` to track file by name, *file_name* or `git add .` to track all the changes made.

There are a lot of ways to see the content of a folder and one is using `ls or dir` for unix/linux or windows respectively, depending on our OS. Git has a special command for this, `git status` . Every file when we clone or initial git, all the files will be `untracked` and `unmodified` . We often check the status as we write to our project.

## Stage files

After we track the files we have edited, we have to stage it - add the file to the VSC permanently, ready to be sent (pushed) to the remote server.

do `git commit -m "message"` , where `-m` flag means message and `message` is a text that describes what changes we made to the project or file.

do `git commit ` - to open our default editor to give a more decriptive message of what really went down. Save the content and close the file to successfully stage it.

### Note

* we can only stage ( save) files we have tracked
* make sure that there is always a commit message

## Update the repository

* to update the local repo with the remote repo do, `git pull` or sometimes `git pull https://...` 
* to update the remote repo with the local repo do, `git push` or sometimes `git push https://...` 
* to downloads all history from the repository from the remote repo do, `git fetch` 

## Check the commits

do `git log` to see the commits we have made. Thus provides we with some information we may use to reset/revert the repo when there is an error.

## Reset

`git reset [commit]` where commit is the code we see when we make a commit. Use that code to reset the repository. It undoes all the commits but keeps the changes, `git reset --hard [commit]` does the same but discard the all histories upto the particular commit.

## Branch

A branch is similar to a versioning. We can diverge from main code, work on the new version/branch without having to mess with the main code.

### Operations with branching

* `git branch` to list all the branches
* `git branch branch_name` to create or divert to a new branch, `branch_name` 
* `git checkout branch_name` to switch to another branch, `branch_name` 
* `git merge branch_name` , combines the current branch with the content of `branch_name` 
* `git branch -d branch_name` to delete `branch_name` from the branches

## Practical

* push all we softwares to github
* using git, create a todo app and push the final result to github

## Summary

* read about git [here][git-site]
* Every command in git, starts with `git` 
* Table of commads we'd use more often
    - `git add file_name` 
    - `git add --all` or `git add .` 
    - `git commit -m "commit message"` 
    - `git pull` 
    - `git push` 
    - `git log` 
    - `git status` 
    - `git fetch` 
    - `git branch` 
    - `git checkout branch` 

## Resource

* Learn git with [Traversy Media][brad-git-site]
* [w3school git][w3school-github-site]

* Git tutorial from [git-scm][git-scm-site]

#
[git-site]:https://git-scm.com
[github-site]:https://github.com
[bitbucket-site]:https://bitbucket.org
[brad-git-site]:https://www.youtube.com/watch?v=SWYqp7iY_Tc
[w3school-github-site]:https://www.w3schools.com/whatis/whatis_github.asp
[git-scm-site]:https://git-scm.com/docs/gittutorial

