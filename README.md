# Boilerplate web GUI with Python backend

Prototype implementation of a simple web HTML with a little Bootstrap frontend working with Python based web server with websocket.


## Components:

* `index.html`: simple webpage with Bootstrap. No css.
* `main.js`: javascript that handles the GUI update and websocket communication with backend
* `server.py`: simple Python backend that handles websocket server (no http server)
* `README.md`: this information file

## Execution:

All commands should be invoked from the source folder.

 * Launch http server on one terminal (default port 8000):

    `python -m http.server`

   Or:

    `python -m http.server <port number>`


* On the second terminal, launch Python backend websocket server (running on port 8081):

    `python server.py`

 * launch front end through browser **http://localhost:8000** (default), or the non-default `<port number>` specified in  `python -m http.server <port number>`.

## Interactions of components:

Sequence diagrams on how the components interact on a sample execution:

```mermaid
sequenceDiagram
   participant browser
   participant server
   note over server: start HTTP server on port 8000 and websocket server on port 8081 (hardcoded in code now)
   note over browser: User visits localhost:8000
   browser->>server: HTTP GET request towards server
   server->>browser: send over index.html and main.js to browser
   note over browser: render the page from index.html (invoke main.js)
   browser->>server: websocket connect
   server->>browser: websocket connect accept
   loop
      note over browser: user interacts with HTML page
      browser->>server: JSON message over websocket (when SUBMIT button is clicked)
      note over server: process JSON message from browser
      server->>browser: JSON message over websocket
   end
   note over browser: user closes web page or tab
   browser-->server: websocket closes

```     
 
## Issues:

* In python there is no easy way for a single server to serve as HTTP and websocket server at the same time

* Never got Bootstrap dropdown list working

* How to do incrementally increase rows in `Results` table

