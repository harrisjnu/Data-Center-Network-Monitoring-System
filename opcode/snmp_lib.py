
import sys
##SNMP OID INFORMATION FETCH ## PYSNMP DOCS
def snmpget(oid, snmp_var):
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_var

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_inoctet(ifindex, snmp_access):
    oid = str('1.3.6.1.2.1.2.2.1.10.') + str(ifindex)
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_outoctet(ifindex, snmp_access):
    oid = str('1.3.6.1.2.1.2.2.1.16.') + str(ifindex)
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_intdesr(ifindex, snmp_access):
    #oid = str('1.3.6.1.2.1.2.2.1.2.') + str(ifindex)
    oid = str('1.3.6.1.2.1.31.1.1.1.18.') + str(ifindex)
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


def snmp_intstatus(ifindex, snmp_access):
    oid = str('1.3.6.1.2.1.2.2.1.8.') + str(ifindex)
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_intmodified(ifindex, snmp_access):
    oid = str('1.3.6.1.2.1.2.2.1.9.') + str(ifindex)
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_cpupercent_sophos(snmp_access):
    #oid = str('1.3.6.1.2.1.2.2.1.9.') + str(ifindex)
    oid = str('1.3.6.1.4.1.21067.2.1.2.2.1')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_diskpercent_sophos(snmp_access):

    oid = str('1.3.6.1.4.1.21067.2.1.2.3.2')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


def snmp_memorypercent_sophos(snmp_access):

    oid = str('1.3.6.1.4.1.21067.2.1.2.4.2')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


def snmp_liveusers_sophos(snmp_access):

    oid = str('1.3.6.1.4.1.21067.2.1.2.6')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


def snmp_ap_adopted(snmp_access):

    oid = str('1.3.6.1.4.1.9.9.618.1.8.4.0')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


def snmp_total_clients(snmp_access):

    oid = str('1.3.6.1.4.1.9.9.618.1.8.12.0')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_wlan_clients(wlanIndex,snmp_access):

    oid = str('1.3.6.1.4.1.14179.2.1.1.1.38.') + str(wlanIndex)
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


def snmp_wlc_temprature(snmp_access):

    oid = str('1.3.6.1.4.1.14179.2.3.1.13.0')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val

def snmp_wlc_uptime(snmp_access):

    oid = str('1.3.6.1.2.1.1.3.0')
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY = snmp_access

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val