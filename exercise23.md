# Exercise 23 (Git)

As developers, we may want to have different versions of our software and keep them too. We may want to revert to a previous state of a file or even the whole project and a _Distributed Version Control System_ (DVCS) will do that job for us. One DVCS is [Git][git-site]. We shall look into how to use git minimally.

We would want to keep our projects on our local server, but our disk could corrupt. Thus we would need a remote server for keeping our software or scripts. Create a free [Github][github-site] account before we proceed any further, for the benefit and practice sake. With Github, we can share our project with other developers who may wish to see and review, share or contribute to our project. Git and Github bridge the gap between remote working.

## Install git

We shall install Git using [this website][git-site], depending on the OS. Afterwards, we do `git --version` on the command-line to check if git has been installed successfully.

## Configure git

Open the command-line - power shell for windows, after a successful installation of Git.

- Set user name: `git config --global user.name your_user_name`
- Set user email: `git config --global user.email your_user_email`

This actually can be changed for every software we want to create using git, else this configuration is the default.

For maybe a private project where the team have their emails and our emails are not required, then we can set local configurations for that particular project.

- Set user name: `git config --local user.name your_user_name`
- Set user email: `git config --local user.email your_user_email`

## Create repository

A repository is a folder that contains our code and any other file we may need for the development of our software.

There may be two or more instances where we would need to create (or use) a git repository:

- when we have already created the folder on our PC, local server, but not under version control.
- when our project is already online (remote) under version control.

### Local repository

When the project is or would be created on our local server and we want it under version control, we do the following:

- change directory into the folder of interest, `cd project_root_dir`
- then do, `git init` - to initialize git

A `.git` folder will be created at the root of the parent folder.

### Remote repository

When the project already exists online, say on [Github][github-site], do the following:

- Navigate to where we want to create (or put) the project
- do, `git clone https://...` - to have the same version of the remote project
- or we can do, `git clone https://... repo_name` - where repo_name is the name of the new folder we want to keep our files in instead of the original. This doesn't alter anything.
- then navigate into `repo_name` - this repository comes with the entire version history of the repository.

## Adding an existing project to a remote server

Here we already have the project or say we have finished developing it locally. We want to push it to the remote repository, do the following:

- initialize the git repo locally, `git init`, if not done already.
- add (let git track) the files in the local repository, `git add .`.
  - The `.` refers to the current directory. So we add all the content in the current directory to git.
  - The recommended approach will be to create a `.gitignore` file and then add the path of the files you do not want to be tracked by git.
  - We can also track individual files with, `git add path_to_file`.
- then stage (save) them, `git commit -m "some message"`

  - if you have a whole lot of message, do, `git commit`.
  - Your default editor (mostly vim) will open. Enter the message, making sure that the topic sentence is the first line and the next line is a newline. Your message starts on the third.
  - save and close the file to add a commit message and make a successful commit

- now copy the remote repository URL and do, `git remote add origin https://...`, where `https://../` is the remote URL
- now send it to the remote repository, `$ git push origin https://...`. A username and a password (token) might be required.

## Git status

Every file in a VCS has a status that tells us what has been done to the file thus what state the file is in.

### Table of file status

| Status       | Description                   |
| ------------ | ----------------------------- |
| `tracked`    | a file git knows about        |
| `untracked`  | a file git doesn't know about |
| `unmodified` | an unchanged tracked file     |
| `modified`   | a changed tracked file        |
| `staged`     | a saved tracked file          |

## Check file status

We do, `git status` to see the status of the files in the current repository.

## Track files

We do, `git add file_name` to track a single or `git add .` to track the entire files in this particular directory.

When we edit the file, the file status will become `modified`, then we do, `git add file_name` to track file by name, _file_name_ or `git add .` to track all the changes made.

There are a lot of ways to see the content of a folder and one is using `ls or dir` for Unix/Linux or windows respectively, depending on our OS. Git has a special command for this, `git status`. Every file when we clone or initial git, all the files will be `untracked` and `unmodified`. We often check the status as we write to our project.

## Stage files

After we track the files we have edited, we have to stage it - add the file to the VSC permanently, ready to be sent (pushed) to the remote server.

do `git commit -m "message"`, where `-m` flag means message and `message` is a text that describes what changes we made to the project or file.

do `git commit ` - to open our default editor to give a more descriptive message of what went down. Save the content and close the file to successfully stage it.

### Note

- we can only stage (save) files we have tracked or are tracked by git.
- make sure that there is always a commit message, a readable and meaningful commit message.

## Update the repository

- to update the local repo with the remote repo do, `git pull` or sometimes `git pull https://...`
- to update the remote repo with the local repo do, `git push` or sometimes `git push https://...`
- to download, all history from the repository from the remote repo do, `git fetch`

## Check the commits

do `git log` to see the commits we have made. Thus provides us with some information we may use to reset/revert the repo when there is an error.

## Reset

`git reset [commit]` where `commit` is the code we see when we made the commit. Use that code to reset the repository. It undoes all the commits but keeps the changes, `git reset --hard [commit]` does the same but discard all histories up to the particular commit.

## Branch

A branch is similar to versioning. We can diverge from the `main` code, work on the new version/branch without having to mess with the main code.

### Operations with branching

- `git branch` to list all the branches
- `git branch branch_name` to create or divert to a new branch, `branch_name`
- `git checkout branch_name` to switch to another branch, `branch_name`
- `git merge branch_name`, combines the current branch with the content of `branch_name`
- `git branch -d branch_name` to delete `branch_name` from the branches

## Practical

- push all your software written so far onto Github
- using git, create a todo app and push the final result to GitHub

## Summary

- read about git [here][git-site]
- Every command in git, starts with `git`
- Table of commads we'd use more often
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

- Learn git with [Traversy Media][brad-git-site]
- [w3school git][w3school-github-site]

- Git tutorial from [git-scm][git-scm-site]

#

[git-site]: https://git-scm.com
[github-site]: https://github.com
[bitbucket-site]: https://bitbucket.org
[brad-git-site]: https://www.youtube.com/watch?v=SWYqp7iY_Tc
[w3school-github-site]: https://www.w3schools.com/whatis/whatis_github.asp
[git-scm-site]: https://git-scm.com/docs/gittutorial
