#from MerakiAPI import apiInit
from GET_orgs import getOrgs
from GET_NetworksBind import getNetworksBind
from GET_Templates import getTemplate
from GET_firmware import firmware
from GET_License import getLicence
from Get_WarmSpare import getWarmSpare
from GET_AlertsNetwork import getAlertsNetwork
from GET_NetworkDevices import getNetworkDevices
from Get_SwitchStacksNetwork import getSwitchStack
from GET_MS_mtu import mtu
from GET_MsDetails import getMsDetail
from GET_VpnBgp import getVpnBgp
from GET_Site2Site_VPN import getNetworkVpn
from GET_MxSetting import  getMxSettings
from GET_MxVlans import getNetMxVlan
from GET_snmp import getSnmp
from GET_Ssid import getSsid
from GET_Ssid import getSsidQuantity
from GET_Ssid import getSsidMinBitrate
from GET_rfProfiles import get_rfProfiles
from GET_l3Fw import getl3Fw
from GET_BWUplink import getUplinkBW
from GET_channelUtil import getChannelUtil

api = input("Enter your API key:")

# Your Organizations
orgId, table = getOrgs(api)

# Organization Networks
network_id, selected_option, table = getNetworksBind(api, orgId)

# Organization Licenses
table = getLicence(api,orgId)

# Organization Templates
table = getTemplate(api, orgId)

# SNMP
table = getSnmp(api, orgId)

# Network Devices
list_serial, table = getNetworkDevices(api, network_id, selected_option)

# Firmware
table = firmware(api, network_id)

# Network Alerts
table1, table = getAlertsNetwork(api, network_id)

# Network Switches info
table1, table = getMsDetail(api, list_serial)

# Network switch stack info
table = getSwitchStack(api, network_id)

# Network MTU configuration
table = mtu(api, network_id)
# Network MX settings
try:
    table = getMxSettings(api, network_id)
except:
    print("No MX support for this network")

# Network MX Vlans
table = getNetMxVlan(api, network_id)

# Network L3 Firewall Rules
table = getl3Fw(api, network_id)

# Network MX in warmspare
table = getWarmSpare(api, network_id)

# Network MX Hub BGP Configuration
table1, table = getVpnBgp(api, network_id)

# Network site-to-site VPN settings
table3, table2, table = getNetworkVpn(api, network_id)

# ssid's
table = getSsid(api, network_id)

# RF profiles
table = get_rfProfiles(api, network_id)

# Best Practices
#Number of SSIDs
table = getSsidQuantity(api, network_id)

#Minimum Bit rate per SSID
table = getSsidMinBitrate(api, network_id)

#BW Uplink
table = getUplinkBW(api, network_id)

#channel utilization
table = getChannelUtil(api, network_id)
