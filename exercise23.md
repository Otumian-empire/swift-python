# Exercise 23 (Git)
As developer, you may want to have different versions of your software and keep them too. You may want to revert to a previous state of a file or even the whole project and a Distributed Version Control System (DVCS) will do that job. One DVCS is [Git][git-site]. We shall look into how to use git minimally.
You would want to keep your projects on your local server, your disk may corrupt. So you'd need a remote server for keeping your softwares or scripts thus create a free [Github][github-site] account before you proceed, for your own good.

## Install git

Install Git from [here][git-site] depending on your OS. Do `git --verion` on the commandline to check if git is installed successfully.

## Configure git

Open the commandline - power shell for windows.

* Set user name: `git config --global user.name your_user_name` 
* Set user email: `git --global user.email your_user_email` 

## Create repository

A repository is basically a folder that contains your code and any other file needed for the proper functioning of your project.

There may be two or more instances where you'd need to create a git repository:

* when you have already created the folder on your PC - local server but not under version control.
* when the project is already on line under version control

### Local repository

When the project is already on your local server and you want it under version control do the following:

* change directory into the folder of interest, `cd ...` 
* do, `git init` - to start git

### Remote repository

When the project already exist online, say on [Github][github-site], do the following:

* Navigate to where you want to create the project
* do, `git clone https://...` - to have the same version of the remote project
* or you can do, `git clone https://... repo_name` - where repo name is the name of the new folder you want to keep you files in instead of the original. This doesn't alter naything.
* then navigate into `repo_name` - this repository comes with the enire version history of the repository.

## Adding an existing project to remote server

Here you already have the project or say you have finished developing it locally then you finally want to pppush it to the remote repository, do the following:

* initialize the git repo locally, `git init` 
* add the files in the local repository, `git add .` 
* then stage them, `git commit -m "some message"` 
* now copy the remote repository url and do, `git remote add origin https://...` , where `https://../` is the remote url
* now send it to the remote repository, `$ git remote add origin https://...` 

## Git status

Every file in a VCS has a status which tells you what has been done to the file thus what state the file is in.

### Table of file status

| Status        | Description |
| ------------- | ----------- |
| `tracked` | file git knows about |
| `untracked` | file git doesn't know about |
| `unmodified` | an unchanged tracked file |
| `modified` | a changed tracked file |
| `staged` | a saved tracked file |

## Check file status

do, `git status` to see the status of the files in the current repository.

## Track files

do, `git add file_name` to track a single or `git add .` to track the entire files in this particular directory.

When you edit the file, the file status will become `modified` , do 
There are a lot of ways to see the content of a folder and one is using `ls or dir` , depending on your OS. Git has a special command for this, `git status` . Every file when you clone or initial git, all the files will be `untracked` and `unmodified` .check the status as you write to your project.

## Stage files

After you track the files you have edited, you have to stage it - add the file to the VSC permanently, ready to be sent (pushed) to the remote server.

do `git commit -m "message"` , where `-m` flag means message and `message` is a text that describes what changes you made to the project or file.

do `git commit ` - to open your default editor to give a more decriptive message of what really went down. Save the content and close the file to successfully stage it.

### Note

* you can only stage (save) file you have tracked
* make sure that the message

## Update the repository

* to update the local repo with the remote repo do, `git pull` or sometimes `git pull https://...` 
* to update the remote repo with the local repo do, `git push` or sometimes `git push https://...` 
* to downloads all history from the repository from the remote repo do, `git fetch` 

## Check the commits

do `git log` to see the commits you have made. Thus provides you with some information you may use to reset/revert the repo when there is an error.

## Reset

`git reset [commit]` where commit is the code you see when you make a commit. Use that code to reset the repository. It undoes all the commits but keeps the changes, `git reset --hard [commit]` does the same but discard the all histories upto the particular commit.

## Branch

A branch is similar to a versioning. You can diverge from main code, work on the new version/branch without having to mess with the main code.

### Operations with branching

* `git branch` to list all the branches
* `git branch branch_name` to create or divert to a new branch, `branch_name` 
* `git checkout branch_name` to switch to another branch, `branch_name` 
* `git merge branch_name` , combines the current branch with the content of `branch_name` 
* `git branch -d branch_name` to delete `branch_name` from the branches

## Practical

* push all you softwares to github
* using git, create a todo app and push the final result to github

## Summary

* read about git [here][git-site]
* Every command in git, starts with `git` 
* Table of commads you'd use more often
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

#
[git-site]:https://git-scm.com
[github-site]:https://github.com
[bitbucket-site]:https://bitbucket.org

