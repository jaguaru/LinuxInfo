from flask import Flask, request, render_template
from config import Configuration

app = Flask(__name__, template_folder='template')
app.config.from_object(Configuration)


