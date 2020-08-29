from flask import Flask
from flask_apschedular import APSchedular

app = Flask(__name__)

@app.route('/')
def index():
    return "welcome to the schedular"

def schedular_task():
    print('this task is running every 5 seconds')

if __name__ == '__main__':
    schedular.add_job(id = 'Scheduled_task', func = schedular_task, trigger = 'interval', seconds = 5)
    schedular.start()
    app.run(debug = True)
