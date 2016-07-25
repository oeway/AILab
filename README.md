# Toolkits for DistributedAI platform

Python toolkits for connecting distributedAI platform, the following module are included:
## Worker
The worker for communicating with distributedAI platform and executing tasks defined by widget.
## taskProcessors
A set of predefined taskProcessor to exectue tasks, three type of taskProcessors are implemented:
 * TaskProcessor, the base class, implement a plain task processor
 * ThreadedTaskProcessor, a task process executed in a seperate thread
 * ProcessTaskProcessor, a task process executed as a subprocess, it can be any commandline program which support commandline arguments and print information as output.

# Installation
Run the following command to install:
```bash
pip install dai
```
That's it.

# Getting Start
You need to login to distributedAI platform and then goto "Widget Workers", create a new worker, and get the id and token.

As an example, we get a worker `id=iJX99fYEdfasigEAd` and `token=jguogvqlerkygcc`.

Then, to run the actual worker, you can open a python prompt session and type the following commands:

```python
import dai
d = dai.Worker(worker_id='iJX99fYEdfasigEAd',
               worker_token='jguogvqlerkygcc',
               server_url='ws://cabat.imod.pasteur.fr:3000/websocket',
               workdir='./dai-workdir',
               dev_mode=True)
d.start()
```
And you will see the worker running on the platform, now you are ready to go, try to create a widget and add the worker you just created.


