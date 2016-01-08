import jsonpickle
class Gateway():
    def __init__(self, sn, status, collectors):
        self.sn = sn
        self.status = status
        self.collectors = collectors

class Collector():
    def __init__(self,sn,status,circuits):
        self.sn = sn
        self.status = status
        self.circuits = circuits

class GatewayDecoder(json.JSONDecoder):
	def decode(self,json_string):
		gateway_dict = super(GatewayDecoder,self).decode(json_string)
		map(json.loads())
		return Gateway(gateway_dict['sn'],gateway_dict['status'],gateway_dict['collectors'])




gateway_string = "{\"sn\":\"GATEWAY_S__NO_g1234\",\"status\":\"1\",\"collectors\":[{\"sn\":\"COLLECTOR_S__NO_co_234\",\"status\":\"1\",\"circuits\":[{\"status\":\"1\",\"port\":\"1\",\"ct\":\"2\",\"i\":\"2.222\"}]}]}"

hardware_full_data_json = "{\"isPartial\":\"0\",\"gateway\":{\"sn\":\"GATEWAY_S__NO_g1234\",\"status\":\"1\",\"collectors\":[{\"sn\":\"COLLECTOR_S__NO_co_234\",\"status\":\"1\",\"circuits\":[{\"status\":\"1\",\"port\":\"1\",\"ct\":\"2\",\"i\":\"2.222\"}]}]}}"




