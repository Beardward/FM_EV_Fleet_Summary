import openpyxl
import vehicle_options
from vehicle_options import Vehicle

# Establish Excel data
path = "C:\\Users\\cejva\\Documents\\Work\\FM Fleet Vehicles from Interviews_FINAL.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook['ALL FM']

# Sheet column values
department = 1
VID = 3
year = 4
make_model = 5
awk_material = 8
weight = 9
size = 10
passengers = 19
add_passengers = 20
sharing = 21
outer_sharing = 22
outer_tasks = 23
tasks = 24
scheduled = 25
usage_percent = 26
drive_dist = 28
v_mods = 29

# Misc. Variables


# Define vehicle rec data objects
lightning = Vehicle(name="Ford F150 Lightning", sizes=["Medium", "Large"], weights=["Heavy", "Heavy Duty"], dists=["Any"], scheduling=["Any"], share_tasks="Any", use_low=60, use_high=100)
box = Vehicle(name="Peterbilt 220EV", sizes=["Heavy Duty"], weights=["Medium", "Heavy"], dists=["Any"], scheduling=["scheduled", "possible"], share_tasks="Any", use_low=0, use_high=60)
transit = Vehicle(name="Ford eTransit", sizes=["Medium", "Large"], weights=["Medium", "Heavy", "Heavy Duty"], dists=["Any"], scheduling=["unscheduled", "possible"], share_tasks="Any", use_low=60, use_high=100)
moto_truck = Vehicle(name="MotoEV Utility Truck", sizes=["Medium", "Large"], weights=["Medium", "Heavy", "Heavy Duty"], dists=["campus-bound", "between campuses"], scheduling=["Any"], share_tasks="Any", use_low=60, use_high=100)
utv = Vehicle(name="MotoEV UTV", sizes=["Small", "Medium"], weights=["Light", "Medium", "Heavy"], dists=["campus-bound", "between campuses"], scheduling=["Any"], share_tasks="Any", use_low=0, use_high=100)
trike = "Civilized Cycles Semi-Trike"

for x in range(1, 193):
    # variables
    options = [lightning, box, transit, moto_truck, utv, trike]
    shareable = 0
    
    # sheet data
    usage = sheet.cell(x, usage_percent).value
    out_sharing = sheet.cell(x, outer_sharing).value
    task_share = sheet.cell(x, outer_tasks).value
    sched = sheet.cell(x, scheduled).value
    curr_dist = sheet.cell(x, drive_dist).value
    curr_size = sheet.cell(x, size).value
    curr_weight = sheet.cell(x, weight).value
    
    # determine shareability/sharepool potential (0-3)
    if sched != "Unschduled":
        shareable += 1
    if task_share != "No":
        shareable += 1
    if out_sharing != "No":
        shareable += 1
    
    # refine vehicle options
    for v in options:
        # usage
        if not (v.use_low <= usage <= v.use_high):
            options.remove(v)
        # task sharing
        if not (v.share_tasks.contains(task_share) and v.share_tasks[0] == "Any"):
            options.remove(v)
        # scheduling
        if not (v.scheduling.contains(sched) and v.scheduling[0] == "Any"):
            options.remove(v)
        # distances
        if not (v.dists.contains(curr_dist) and v.dists[0] == "Any"):
            options.remove(v)
        # size
        if not (v.sizes.contains(curr_size)):
            options.remove(v)
        # weight
        if not (v.weights.contains(curr_weight)):
            options.remove(v)
            
    # write selection(s) to sheet
    
        

'''
for each row
    usage
        cycle each curr option - remove those with ranges not including
        if peterbilt range includes && NOT unscheduled
            sharepool flag (still recc smaller vehicle
    sizes
        
    weights
    
    
'''