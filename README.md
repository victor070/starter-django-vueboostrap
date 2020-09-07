Before you dive into anything, see for yourself how easy you can setup a full workflow framework for your `development` and `deployment` for your real world project.

Step 1: Clone this repo

Step 2: Create a virtualenv with python3

- **IMPORTANT!** Before creating the virtual env, 
make sure the Python 3 version is 3.6 or higher.

```
mkvirtualenv -p python3 starter

```

Step 3: Install the backend requirements

```
pip install -r requirements.txt
```

Step 4: Run the migrations

```
./manage.py migrate
```

Step 5: Start the backend

```
./manage.py runserver
```

Step 6: Start the frontend

cd fronted
npm i
npm run dev

```
cd frontend
npm i
npm start
```

And Done, as easy as 123!!

# Basic

## Installation

### Prerequisite

You need to have Node.js installed.

[Instruction for installing NodeJS in Mac](http://lmgtfy.com/?q=install+nodejs+mac)

[Instruction for installing NodeJS in Window](http://lmgtfy.com/?q=install+nodejs+window)

you need to have Vue.js

sudo npm install -g @vue/cli-init

[Documentacion](https://vuejs-templates.github.io/webpack/)


### Post Installation
you need to have vue tools

npm install vue-devtools --save-dev

## Initialize your project

Now run the following commands in your terminal

**NOTE: You only need to run this once!**

```sh
$ npm install # This will install the necessary packages to use the app
```

**That's it!**


### To run the app in Development Mode

```sh
$ npm run dev
```

Wait about 30 seconds for your development environment to initialize.

When it finishes, open your browser and go to `http://localhost:8080/`

If you see the landing page, it means you have set up everything successfully.
