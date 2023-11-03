import meraki
from prettytable import PrettyTable


def getChannelUtil(api, network_id):
    dashboard = meraki.DashboardAPI(api, output_log=False, print_console=False)
    #Check if the network supports wireless
    responsecheck = dashboard.networks.getNetwork(network_id)
    if "wireless" in responsecheck["productTypes"]:

        try:
            response = dashboard.networks.getNetworkNetworkHealthChannelUtilization(network_id, total_pages='all')
        except Exception as e:
            table = PrettyTable()
            table.title = "Channel Utilization"
            table.field_names = ["Description"]
            table.add_row(["This endpoint is only available for networks on MR 27.0 or above."])
            print(e)
            return table

        bandera = 0
        flotantes24 = 0.0
        flotantes50 = 0.0
        list_data = []

        for apInfo in response:
            apSerial = apInfo["serial"]
            apModel = apInfo["model"]
            apUtil24 = apInfo["wifi0"]
            apUtil50 = apInfo["wifi1"]

            for apUtil in apUtil24:
                flotantes24 = flotantes24 + apUtil["utilization"]

            total24 = flotantes24 / 144

            for apUtil in apUtil50:
                flotantes50 += apUtil["utilization"]

            total50 = flotantes50 / 144

            compliant24 = "COMPLIANT"
            compliant50 = "COMPLIANT"

            if total24 > 60:
                compliant24 = "NON COMPLIANT"

            if total50 > 40:
                compliant50 = "NON COMPLIANT"

            listChannelVar = [apSerial, apModel, total24, total50, compliant24, compliant50]
            list_data.append(listChannelVar)
            table = PrettyTable()
            table.title = "Channel Utilization"
            table.field_names = ["Serial", "Model", "2.4 GHz Utilization 1 DAY","5.0 GHz Utilization 1 DAY", "2.4 GHz COMPLIANT", "5.0 GHz COMPLIANT" ]

            for rows in list_data:
                table.add_row(rows)

        print(table)

    return (table)