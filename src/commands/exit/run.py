import yaml
import readline
import signal
from prettytable import PrettyTable
from src import printcolors as pc
from src import utils as utils
from src import Command
import json
import sys
import time


class Command:

    def __init__(self, path, api):
        pc.printout("\nGoodbye!\n", pc.RED)
        sys.exit(0)