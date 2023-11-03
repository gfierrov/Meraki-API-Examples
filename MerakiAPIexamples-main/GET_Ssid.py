import meraki
from prettytable import PrettyTable

def getSsid(api, network_id):
    dashboard = meraki.DashboardAPI(api, output_log=False, print_console=False)

    #Check if the network supports wireless
    responsecheck = dashboard.networks.getNetwork(network_id)
    if "wireless" in responsecheck["productTypes"]:

        response = dashboard.wireless.getNetworkWirelessSsids(network_id)

        list_data = []
        for ssidsInf in response:
            if ssidsInf["enabled"] == True:
                ssidsName = (ssidsInf["name"])
                ssidsAuth = (ssidsInf["authMode"])

                try:
                    ssidsEnc = (ssidsInf["encryptionMode"])
                except KeyError:
                    ssidsEnc = "-"

                try:
                    ssidsWpa = (ssidsInf["wpaEncryptionMode"])
                except KeyError:
                    ssidsWpa = '-'
                try:
                    ssidsIpAss = (ssidsInf["ipAssignmentMode"])
                except KeyError:
                    ssidsIpAss = '-'

                if ssidsInf["authMode"] == "8021x-radius":
                    for ssidsRadVar in ssidsInf["radiusServers"]:
                        ssidsRad = (ssidsRadVar["host"])
                        ssidsRadPort = (ssidsRadVar["port"])
                else:
                    ssidsRad = "None"
                    ssidsRadPort = "None"
                    listSsidsVar = [ssidsName, ssidsAuth, ssidsEnc, ssidsWpa, ssidsRad, ssidsRadPort, ssidsIpAss]
                    list_data.append(listSsidsVar)
        table = PrettyTable()
        table.title = "Network SSIDs"
        table.field_names = ["Name", "Auth", "Encryption", "WPA mode", "Radius", "Radius Port", "Ip Assignment"]
        for rows in list_data:
            table.add_row(rows)
        print(table)

    else:
        table = PrettyTable()
        table.title = "Network SSID"
        table.field_names = ["Feature", "Settings"]
        table.add_row(["Network Product", "This network does not support wireless"])
        print(table)

    return  (table)

def getSsidQuantity(api, network_id):
    dashboard = meraki.DashboardAPI(api, output_log=False, print_console=False)
    # Check if the network supports wireless
    responsecheck = dashboard.networks.getNetwork(network_id)
    if "wireless" in responsecheck["productTypes"]:
        count=0
        response = dashboard.wireless.getNetworkWirelessSsids(network_id)
        for key in response:
            if(key['enabled']==True):
                count+=1

        table = PrettyTable()
        table.title = "Number of SSIDs"
        table.field_names = ["Quantity", "Compliant"]

        if count>3:
            table.add_row([count, "NOT COMPLIANT"])

        else:
            table.add_row([count,"COMPLIANT"])
        print(table)

    else:
        table = PrettyTable()
        table.title = "Number of SSIDs"
        table.field_names = ["Description"]
        table.add_row(["This network does not support wireless"])
        print(table)

    return (table)

def getSsidMinBitrate(api, network_id):
    dashboard = meraki.DashboardAPI(api, output_log=False, print_console=False)
    # Check if the network supports wireless
    responsecheck = dashboard.networks.getNetwork(network_id)
    if "wireless" in responsecheck["productTypes"]:
        list_data = []
        response = dashboard.wireless.getNetworkWirelessSsids(network_id)
        for key in response:
            temp_list = []
            if (key['enabled'] == True):
                temp_list.append(key['name'])
                temp_list.append(key['minBitrate'])
                if key['minBitrate'] > 11:
                    temp_list.append('COMPLIANT')
                else:
                    temp_list.append('NOT COMPLIANT')
                list_data.append(temp_list)

        table = PrettyTable()
        table.title = "Minimum Bitrate"
        table.field_names = ["SSID", "Minimum Bitrate", "Compliant"]
        for rows in list_data:
            table.add_row(rows)
        print(table)

    else:
        table = PrettyTable()
        table.title = "Minimum Bitrate"
        table.field_names = ["Description"]
        table.add_row(["This network does not support wireless"])
        print(table)

    return (table)