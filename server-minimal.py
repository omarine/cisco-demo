#Simple Python OPC-UA Server
#Sending out 2 data values
#Flo Pachinger / flopach, Cisco Systems, July 2020
#Script based on the server example https://github.com/FreeOpcUa/python-opcua
#LGPL-3.0 License

from itertools import count
import logging
import asyncio
from tokenize import Double, Floatnumber

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
    server.set_endpoint('opc.tcp://0.0.0.0:48405/opcua/')
    server.set_server_name("DevNet OPC-UA Test Server")

    # setup our own namespace, not really necessary but should as spec
    uri = 'http://devnetiot.com/opcua/'
    idx = await server.register_namespace(uri)
    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()
    # populating our address space
    myobj = await objects.add_object(idx, "MyObject")
    myvar = await myobj.add_variable(idx, "MyVariable", 6.7)
    await myvar.set_writable()    # Set MyVariable to be writable by clients

    _logger.info('Starting server!')
    
    async with server:
        count = 0
        # run forever and iterate over the dataframe
        while True:
            count += 0.1
            await myvar.set_value(count)
            await asyncio.sleep(5)
            
if __name__ == '__main__':
    #python 3.6 or lower
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    #python 3.7 onwards (comment lines above)
    asyncio.run(main())