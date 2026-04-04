
# Thoughs ravel


## frontend

### Move to Folder
1. cd /frontend

### Install 
1. bun install 

### How to start app 
1. bun start

### Broblem to see app Arch X11 B
1. WEBKIT_DISABLE_COMPOSITING_MODE=1 bun start

## backend
0. 1. cd  backend
0. pip poetry install
1. poetry install
2. poetry run uvicorn main:app --reload --port 8080




# Futures ideeas

## chatting room and / or / vs / with  artific 
application to send text messanges like: text, link 
like chatting room 
without any registration , or with the simplest authorization 

## Must have
- servers rooms 
- can store data in local Zero server

## How to make it self-contained (For music format changer in python)

Bundle Vue with Vite → dist/.

Python is included in your app folder or installed as part of the package.

Electrobun runs a small script that:

Starts Python backend (e.g., bun.spawn("python", ["backend/main.py"]))

Opens the WebView pointing to the local dist/index.html or Python URL

When the app closes → you can terminate Python automatically.