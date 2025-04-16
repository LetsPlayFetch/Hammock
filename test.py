# Built-in (should be ignored)
import os
import sys
import math
import random
import datetime
import json
import pathlib

# Real third-party packages (should install fine)
import requests
import numpy
import pandas
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import rich
import tqdm
import seaborn
import flask

# Try nested import
from urllib.parse import quote

# These next ones are likely NOT installed
# One should fail, just to test error handling
try:
    import notarealpackage123  # should cause a pip failure
except ImportError:
    print("✅ Failed gracefully on notarealpackage123")

try:
    import ultrafunkymodule
except ImportError:
    print("✅ Failed gracefully on ultrafunkymodule")
