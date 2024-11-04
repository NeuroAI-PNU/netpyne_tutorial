from neuron import h
from netpyne import sim

# ------------------------------------------------------------------------------
# RUN MODEL
# ------------------------------------------------------------------------------
cfg, netParams = sim.loadFromIndexFile("index.npjson")

sim.create(netParams, cfg)
h.finitialize()

# sim.net.createPops()  # instantiate network populations
# sim.net.createCells()  # instantiate network cells based on defined populations
# sim.net.connectCells()  # create connections between cells based on params
# sim.net.addStims()  # add external stimulation to cells (IClamps etc)
# sim.net.addRxD()  # add reaction-diffusion (RxD)
# sim.setupRecording()  # setup variables to record for each cell (spikes, V traces, etc)
sim.simulate()
sim.analyze()

# print(sim.net.params["rxdParams"])
