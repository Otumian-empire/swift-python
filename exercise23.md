# Exercise 23 (Git)
As developer, you may want to have different versions of your software and keep them too. You may want to revert to a previous state of a file or even the whole project and a Distributed Version Control System (DVCS) will do that job. One DVCS is [Git][git-site]. We shall look into how to use git minimally.
You would want to keep your projects on your local server, your disk may corrupt. So you'd need a remote server for keeping your softwares or scripts thus create a free [Github][github-site] account before you proceed, for your own good.

## Install git

Install [git][git-site] depending on your OS. Do `git --verion` on the commandline to check if git is installed successfully.

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

## Git status

Every file in a VCS has a status which tells you what has been done to the file thus what state the file is in.

### Table of file status

| Status        | Description |
| ------------- | ----------- |
| `tracked` | file git knows about |
| `untracked` | file git doesn't know about |
| `unmodified` | is an unchanged tracked file |
| `modified` | is a changed tracked file |
| `staged` | is a saved tracked file |

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

## Example

## Practical

* push all you softwares to github
* using git, create a todo app and push the final result to github

## Summary

* read about git [here][git-site]
* Every command in git, starts with `git` 

#
[git-site]:https://git-scm.com
[github-site]:https://github.com
[bitbucket-site]:https://bitbucket.org

