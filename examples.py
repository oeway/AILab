import dai
d = dai.Worker(worker_id='Xkzx4atx6auuxXGfX',
                worker_token='qjygopwdoqvqkzu',
                server_url='ws://ailab.ai/websocket',
                workdir='./dai-workdir',
                dev_mode=True)
d.start()
