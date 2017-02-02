# Toolkits for AILab.AI platform (WIP)

Python toolkits for connecting AILab.AI platform, the following module are included:
## `dai.Worker`
The worker for communicating with AILab.AI platform and executing tasks defined by widget.
## `dai.taskProcessors`
A set of predefined taskProcessor to exectue tasks, three type of taskProcessors are implemented:
 * `TaskProcessor`, the base class, implement a plain task processor
 * `ThreadedTaskProcessor`, a task process executed in a seperate thread
 * `ProcessTaskProcessor`, a task process executed as a subprocess, it can be any commandline program which support commandline arguments and print information as output.

# Installation
Run the following command to install:
```bash
pip install dai
```
That's it.

# Getting Start
You need to login to AILab.AI platform and then goto "Widget Workers", create a new worker, and get the id and token.

As an example, we get a worker `id=iJX99fYEdfasigEAd` and `token=jguogvqlerkygcc`.

Then, to run the actual worker, you can open a python prompt session and type the following commands:

```python
import dai
d = dai.Worker(worker_id='iJX99fYEdfasigEAd',
               worker_token='jguogvqlerkygcc',
               server_url='ws://ai.pasteur.fr/websocket',
               workdir='./dai-workdir',
               dev_mode=True)
d.start()
```
And you will see the worker running on the platform, now you are ready to go, try to create a widget and add the worker you just created. In the "Code" tab in a widget editor, you can add one code file named "__init__.py" with the type "python" which will perform the actuall task on the worker node.

Here is an example of task processor code which uses Keras for training networks:
```python
from dai.kerasUtils import KerasProcess

class Process(KerasProcess):
    def task_arguments(self):
        x = self.task.get('input.x')
        return ['python', 'test.py', x]

if __name__ == "__worker__":
    TASK_PROCESSOR = Process(TASK, WIDGET, WORKER)
```

Another task processor code example:
```python
import time
from dai.taskProcessors import ThreadedTaskProcessor

def process_task(task, **kwargs):
    # start task
    task.set("status.stage", "started")

    # run your task code with config and input
    # get task config and input
    print(task.get("config"))
    print(task.get("input"))

    # use "set" for important information such as error and results
    task.set({"status.error":"this is a fake error",
              "status.info":"error"})

    # use "update" for fast updating intermediate status
    task.update({"status.info": "hello from worker",
                 "status.progress": 50})

    time.sleep(3)

    # save result in "output"
    task.set("output.result", 100)

    # finish task
    task.set("status.progress", 100)
    task.set("status.stage", "done")

if __name__ == "__worker__":
    TASK_PROCESSOR = ThreadedTaskProcessor(TASK, WIDGET, WORKER, process=process_task)
```

Just fill your code which does some job into `process_task` function. With self.task, you can get the dictionaries which stores the `config`, `input` and `output`. The basic guideline is you let the store the configurations or parameters in `config` dictionary, the file path or the url of your data you want to process in `input` dictionary, after executing your task, fill `output` dictionary with the output.

You may also want to use HTML and JS to create some awsome GUI for the user to interact, just try to fill PANEL.html and PANEL.js with some code, it uses [AngularJS](https://angularjs.org/) and [Angular-Material](https://material.angularjs.org/latest/) as its underlying implementation.

More examples and details to be continue...
