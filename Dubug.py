Command to change EN7581 GT board mode from GPON to EPON. 

sys onumode xepon_sym
-------------------------------------------------------

Command to read the BOB file data on the CLI. 

echo flash_dump >/proc/pon_phy/debug
echo show_BoB_information > /proc/pon_phy/debug

tftp -gr 7570_bob.conf 

ecnt_mtd writeflash /tmp/7570_bob.conf 160 393216 art

--------------------------------------------------------

Command to Check which ports are up on JCOW4032.

cat proc/tc3162/gsw_link_st

--------------------------------------------------------

Process To Update Mesh Binaries 

RIL> ps | grep mesh
17197 root     12736 S    /userfs/bin/svchost -c /etc/mesh.svc
18467 root      2096 S    grep mesh
kill 17197
rm -f /tmp/wapp_ctrl
killall -15 mapd
killall -15 p1905_managerd
killall -15 wapp
tftp to /tmp folder and upload mapd binaries 
chmod 777 /tmp/mapd
/bin/sh /usr/etc/mesh_core_dump_start.sh agent 
/userfs/bin/svchost -c /etc/mesh.svc&

----------------------------------------------------------

uci show network 

show all the network interfaces in an openwrt device. 

--------------------------------------------------------------

Command for EN7523/EN7529/EN7562 to enable PLOAM Messages 

echo msg oam 1 > /proc/gpon/debug   
echo msg act 1 > /proc/gpon/debug     
echo msg int 1 > /proc/gpon/debug      

-------------------------------------------------------------

tcapti show InfoEther


sys memrl 1fa85930 
programming guide - register map 

-------------------------------------------------------------
TO default reset the device
prolinecmd clear 1 
prolinecmd restore default. 

tcapi show wlan 
tcapi show wlan11ac 

BSSIDNUM = 1 
there will be only 1 ssid supported. 

---------------------------------------------------------------------------------------------------------------------------------------

Get pon optical information 

echo show_BoB_information > /proc/pon_phy/debug

----------------------------------------------------------------------------------------------------------------------------------------

Command to change FrontHaul BSS from Hidden to Non Hidden 

2G:

tcapi set wlan_entry0 HideSSID 1

tcapi save

tcapi commit wlan

 

5G:

tcapi set wlan11ac_entry0 HideSSID 1

tcapi save

tcapi commit wlan11ac

This is the cmd for modifying one BSS, if the device is the 4032/407 then you can modify the entry number

vi /etc/wts_bss_info_config

----------------------------------------------------------------------------------------------------------------------------------------\

 cat /proc/tc3162/eth_port_status
 
 ---------------------------------------------------------------------------------------------------------------------------------------
 
Enable sniffer to capture Dying Gasp packets:
sys memwl 1fb66400 80080000

For example, we use software to send 3 dying gasp messages and capture them:
sys memwl 1fb66400 80080000     // enable sniffer
sys memwl 1fb662ac 10300            // software send dying gasp num[3]
sys memwl 1fb66400 0                    // disable sniffer


---------------------------------------------------------------------------------------------------------------------------------------\
Command to Change the serial number 

prolinecmd xponsn set ECNT00067112
tcapi set GPON_ONU SerialNumber ECNT00067112
tcapi save
reboot
------------------------------------------------------------------------------------------------------------------------------------------\

 cat /userfs/profile.cfg |Ether
 # cat /userfs/profile.cfg |grep ETHER
WAN_ETHER=y
TCSUPPORT_WAN_ETHER=y
# TCSUPPORT_QDMA_WAN_FOR_ETHER is not set
# TCSUPPORT_ETHER_DOWNVLAN is not set
# TCSUPPORT_ACTIVE_ETHERNET_WAN is not set
# RA_ETHERMEDIATYPE is not set
# TCSUPPORT_ETHER_ALL_LED is not set
# TCSUPPORT_WAN_ETHER_LED is not set
# TCSUPPORT_MANUAL_ETHERNET_PORTMAP is not set

--------------------------------------------------------------------------------------------------------------------------------------------\

IGMP Proxy 

To check IGMP Proxy and snooping support in EN7529

echo quickleave > /etc/igmpproxy.conf
echo phyint br-lan downstream ratelimit 0 threshold 1 >> /etc/igmpproxy.conf
echo phyint pon.323 upstream ratelimit 0 threshold 1 >> /etc/igmpproxy.conf
igmpproxy  /etc/igmpproxy.conf -d &

---------------------------------------------------------------------------------------------------------------------------------------------\

Show TR069 config:

tcapi show cwmp
Wan2lan wireshark capture wan side packets to lan ports:
sys wan2lan on
Enable TR069 serial log :
tcapi set Cwmp_Entry dbgflag 3
