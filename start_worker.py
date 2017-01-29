import dai
d = dai.Worker(worker_id='pMahGyXopLwrZWCQk',
                worker_token='3RpKCIN#1Z1',
                server_url='wss://ai.pasteur.fr/websocket',
                workdir='./dai-workdir',
                dev_mode=True)
d.start()
