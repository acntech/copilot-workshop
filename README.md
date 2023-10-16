# GitHub Copilot Workshop

Welcome to this workshop on GitHub Copilot. In this workshop, you will create a running application with the help of GitHub Copilot. The workshop consists of several parts, each with a different task that you need to complete. You can find the tasks below, and for each task, you need to switch to the branch given on the task to start from.

Prerequisites:

- Python3 installed on your machine
- A GitHub account with Copilot activated
- VSCode installed with the Copilot extension
- Some of the tasks will use external libraries that Copilot will suggest, such as requests. You can install them on the fly with _pip_

Unless otherwise specified, you should only have the target file open in VSCode. You should also close this README file.

## Task 1 - Setup and basic query

In this task, you will create your own pokedex from scratch. You should start from the branch *task/setup*.

Your goal is to write a simple app that can query the pokeapi with a given pokemon name. You should be able to display the pokemon’s name, type and number in the terminal like this:

```Name: Charmander, Type: Fire, Number: 4```

*Hint:* Try to set the context at the beginning of your code. Copilot will find the API for you.

## Task 2 - Extend code without code base

In this task, you will print the whole evolution chain of a pokemon given its name as input to your application.

Open up main.py and use Copilot to generate code that can print out the entire evolution chain of the pokemon, along with their types. Here is an example:

```
Name: Charmander, Type: Fire
Name: Charmeleon, Type: Fire
Name: Charizard, Type: Fire/Flying
```

*Hint:* There are two other APIs that needs to be called to make this work

## Task 3 - Extend code with existing code base

In this task, you will start from scratch and use Copilot’s ability to read other open files. To begin, switch to the branch *task/expand-api*.

Your goal is the same as in *task 2*, but you want to keep *api.py* open to let Copilot read the context from that file.

## Task 3 - Unit tests

We want some unit tests for our evolution chain code. Add unit tests based on pytest or the testing library of your choice to the evolution chain function. Ask Copilot to provide test data based on the external api.

Use your existing branch with your existing code to achieve this.

## Task 4 - Expand the code

We want to expand the API we have created with new fields. You can check out the api or let Copilot suggest fields for you to make the API more detailed.

Some examples of fields to include are the criteria for evolution, size, egg groups and more.

## Bonus Task 1 - Classes

Refactor the code using an object oriented paradigm with the help of classes and objects. You can use Copilot to assist you with this task.

## Bonus Task 2 - Rest API

Create a REST API based on your existing code.

## Bonus Task 3 - Enhance your app

Enhance the app as much as you want and use Copilot as your guide for coding.