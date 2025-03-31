class Vehicle:
        def __init__(self, name, sizes: list, weights: list, dists: list, scheduling: list, share_tasks, use_low, use_high):
            self.name = name
            # Vehicle sizing communicated dozens of times over to be most vital attribute to consider when right-sizing a vehicle for specific work.
            # Many trades require large storage and hauling capacity for particularly long, awkward-dimensioned, and voluminous material/tools.
            self.sizes = sizes
            # Vehicle weight considered secondary, still often vital attribute to work/trade-specific vehicles. Weight capacity can be absolutely
            # necessary for those hauling large assortments/packages of materials or trades using very heavy,dense materials.
            self.weights = weights
            # Major recommended EV transition options include LSVs (Low-Speed Vehicles) that would effectively be bound to local, slower roads near campus.
            # Many FM (trades) vehicles specifically require capability for metro-area travel.
            self.dists = dists
            # Vehicles that more closely follow usage schedules would prove far easier to implement in sharepools, allowing for precise, organized
            # usage of shared vehicles in planned time blocks.
            self.scheduling = scheduling
            # 
            self.share_tasks = share_tasks
            # Many FM vehicles were provided with anecdotal evidence detailing vehicle usage undermining the full capabilities of a vehicle. Such values
            # and estimates of "% intended usage" can highlight opportunities for outright downsizing or a mixture of downsizing in addition to an 
            # implemented sharepool vehicle, fulfilling remaining, less-frequent requirements of original vehicle.
            self.use_low = float(use_low)
            self.use_high = float(use_high)