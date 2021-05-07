# Exercise 26 (Starting a project)

A project idea can make you procrastinate, do you believe that?

Do you also know that it is better to have a broad view of the project you want to build before you start coding? Of course, having a broad view of the project doesn't mean implement it at once.

Do you know that it is not, sometimes, the code that makes the project but the idea and documentation? Yes, what is an idea if it is just a paper project?

Do you know that your project does not have to necessarily rock the world? I mean, if you want to do something. Your project can be function implementations of some mathematical concepts. Your projects can just be the solutions (implementations) of some algorithm and data structure course.

We are telling you that, having an understanding of the programming concepts we have discussed so far and can use them is the whole purpose of this journey.

A project may fit into one file. It depends. You should know when to separate concerns (functionalities) and when to use a class. You can separate some functions in a new file. If some of these functions and data required can fit into a class, do that.

Get the project idea and write a story on it. This story will guide you on how you should implement the idea.

## Virtual environment

Whenever we want to start a project, it is recommended that we use a virtual environment. A virtual environment separates the requirements we need for our particular project from the modules on our local system. With this approach, we can choose a version of a module that is unique to our project.

This will not affect the version of the local module if it exists. We recommend you use pipenv.

<!-- pipenv, pyenv, pip -->

## Project management

[Github][github] is one of the free servers that can host our project. You will have to create a Github repo for your project. This will allow others to contribute to your project. Again, if the unfortunate happens when you lose your PC, you still have the remote code available on [Github][github].

[Trello][trello] can be used as a management tool for your project. It is a very great tool for managing projects for a small number of devs also.

<!-- github and trello -->

## Unit test

There are instances whereby we have to take another step to develop an interface for some functionalities. There is no need for these extra step when is not needed. Write a unit test instead. Try and break your code and fix it.

<!-- Add unit test to your code -->

## Documentation

Every project must have a story. This story tells onlookers and stakeholders what your project does and sometimes the benefit it comes with. It tells users and other devs how to use your application and sometimes how to extend it.

<!-- The project story and technical details -->

## Where to go from here

From here, try going through the resources below. (It is not compulsory). It is good for your programming health. The more you understand the better.

### How to structure a project

- [The Hitchhiker's guide to python - Structuring Your Project][project-structure-py-doc]
- [Julien Danjou - Starting your first Python project][project-structure-julien]

### More on virtual environments

- [The Hitchhiker's guide to python - Pipenv & Virtual Environments][py-guide-virtualenvs]
- [Pipenv - Python Dev Workflow for Humans][pipenv]
- [Real Python - Pipenv: A Guide to the New Python Packaging Tool][real-python-pipenv]

### More Projects for your elbow

- [42 Exciting Python Project Ideas & Topics for Beginners by Rohit Sharma ][upgrad-project-ideas]
- [Python projects for beginners][beginnerpythonprojects]
- [10 Easy Python Programming Project Ideas by Mikke][python-projects-for-beginners]
- [DATAQUEST - 45 Fun (and Unique) Python Project Ideas for Easy Learning][dataquest-project-for-beginners]

#

<!-- Starting a python project -->

[github]: https://github.com
[trello]: https://trello.com

<!-- project structure -->

[project-structure-py-doc]: https://docs.python-guide.org/writing/structure/
[project-structure-julien]: https://julien.danjou.info/starting-your-first-python-project/

<!-- projects -->

[upgrad-project-ideas]: https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
[beginnerpythonprojects]: https://beginnerpythonprojects.com/
[python-projects-for-beginners]: https://mikkegoes.com/python-projects-for-beginners/
[dataquest-project-for-beginners]: https://www.dataquest.io/blog/python-projects-for-beginners/

<!-- virtual environment -->

[py-guide-virtualenvs]: https://docs.python-guide.org/dev/virtualenvs/
[pipenv]: https://pipenv.pypa.io/en/latest/
[real-python-pipenv]: https://realpython.com/pipenv-guide/
