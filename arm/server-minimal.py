#Simple Python OPC-UA Server
#Sending out 2 data values
#Flo Pachinger / flopach, Cisco Systems, July 2020
#Script based on the server example https://github.com/FreeOpcUa/python-opcua
#LGPL-3.0 License

from itertools import count
import logging
import asyncio
from tokenize import Double, Floatnumber
import time
from asyncua import ua, Server
from asyncua.common.methods import uamethod

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')

@uamethod
def func(parent, value):
    return value * 2

async def main():
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint('opc.tcp://0.0.0.0:48401/opcua/')
    server.set_server_name("DevNet OPC-UA Test Server")

    
    # populating our address space
   # setup our own namespace, not really necessary but should as spec
    uri = 'http://devnetiot.com/opcua/'
    idx = await server.register_namespace(uri)

    # populating our address space
    # server.nodes, contains links to very common nodes like objects and root
    # obj_vplc = await server.nodes.objects.add_object(idx, 'vPLC1')
    # var_temperature = await obj_vplc.add_variable(idx, 'temperature', 0)
    # var_pressure = await obj_vplc.add_variable(idx, 'pressure', 0)
    # var_pumpsetting = await obj_vplc.add_variable(idx, 'pumpsetting', 0)

    objects = server.get_objects_node()

    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable() 

    _logger.info('Starting server!')
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
    # async with server:
    #     count = 0
    #     # run forever and iterate over the dataframe
    #     while True:
    #         count += 0.1
    #         await myvar.set_value(count)
    #         await asyncio.sleep(5)
            
if __name__ == '__main__':
    #python 3.6 or lower
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    #python 3.7 onwards (comment lines above)
    asyncio.run(main())