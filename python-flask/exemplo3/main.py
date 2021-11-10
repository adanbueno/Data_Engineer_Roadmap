from flask import Flask
from src.server.instance import server

from src.controllers.books import *

server.run()