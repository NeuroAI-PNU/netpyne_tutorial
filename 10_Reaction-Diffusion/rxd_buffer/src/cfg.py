from netpyne import specs

cfg = specs.SimConfig()  # object of class cfg to store simulation configuration
cfg.duration = 500  # Duration of the simulation, in ms
cfg.recordTraces = {
    # "V_soma": {"sec": "soma", "loc": 0.5, "var": "v"},
    "ca": {"sec": "soma", "loc": 0.5, "var": "cai"},
    "buf": {"sec": "soma", "loc": 0.5, "var": "bufi"},
    "cabuf": {"sec": "soma", "loc": 0.5, "var": "cabufi"},
}

cfg.recordStep = 0.1  # Step size in ms to save data (eg. V traces, LFP, etc)


cfg.filename = "rxd_buffer"  # Set file output name
cfg.analysis["plotTraces"] = {
    "include": ["cell"],
    # "oneFigPer": "cell",
    "ylim": [0, 0.0001],
    "overlay": True,
    "saveFig": True,
}  # Plot recorded traces for this list of cells

# cfg.analysis["plotRxDConcentration"] = {"speciesLabel": "ca", "regionLabel": "cyt"}
