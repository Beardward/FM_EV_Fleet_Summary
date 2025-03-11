class Vehicle:
        def __init__(self, name, sizes: list, weights: list, dists: list, scheduling: list, share_tasks, use_low, use_high):
            self.name = name
            self.sizes = sizes
            self.weights = weights
            self.dists = dists
            self.scheduling = scheduling
            self.share_tasks =share_tasks
            self.use_low = use_low
            self.use_high = use_high