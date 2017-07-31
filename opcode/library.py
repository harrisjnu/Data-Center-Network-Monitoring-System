
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