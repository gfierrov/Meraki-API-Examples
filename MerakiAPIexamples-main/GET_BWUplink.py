import meraki
from prettytable import PrettyTable

def getUplinkBW(api, network_id):
    dashboard = meraki.DashboardAPI(api, output_log=False, print_console=False)
    try:
        response = dashboard.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(network_id)
        bwlimits = response['bandwidthLimits']
    except:
        table = PrettyTable()
        table.title = "Bandwidth Uplink"
        table.field_names = ["Description"]
        table.add_row(["This network does not support MX networks"])
        print(table)
        return table

    list_data=[]
    connections=[]
    for rows in bwlimits:
        connections = []
        connections.append(rows)
        for limit in bwlimits[rows]:
            connections.append(bwlimits[rows][limit])
        list_data.append(connections)
    print(connections)

    table = PrettyTable()
    table.title = "Bandwidth Uplink"
    table.field_names = ["Connection", "Limit Up", "Limit Down"]
    for rows in list_data:
        table.add_row(rows)
    print(table)
    return (table)