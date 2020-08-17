#!/usr/bin/python3

import flask
from flask import request
from src import rpc_request
from src import block_extract

app = flask.Flask(__name__)
app.config["DEBUG"] = True
rpc = rpc_request.rpc()

@app.route('/api/v1/gobject', methods=['GET'])
def gobject_API():
    cmd = request.args.get('cmd')
    arg = request.args.get('arg')
    return rpc.gobject(cmd, arg)

@app.route('/api/v1/masternodelist', methods=['GET'])
def masternodelist_API():
    mode = request.args.get('mode')
    filter = request.args.get('filter')
    return rpc.masternodelist(mode, filter)

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)

    chain = block_extract.scrape_chain()
    chain.process_blocks()