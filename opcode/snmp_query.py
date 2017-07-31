import datetime
import time
import logging
import pymysql
#logging.basicConfig(level=logging.debug, format=' %(asctime)s - %(levelname)s - %(message)s')
from opcode.library import snmpget
from opcode.snmp_lib import *



# DB CONNECTIONS

db_CISNMS = pymysql.connect("DB_IP","DB_RW_USER","DB_PASS","DB_NAME")
cursor = db_CISNMS.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)


def xtreme_core(interval):

    SNMP_HOST = 'SNMP_AGENT_IP'
    SNMP_PORT = 161
    SNMP_COMMUNITY = 'SNMP_COMMUNITY'
    snmp_var = [SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY]
    try:
        #IN OCTET FETCH - PRE-SLEEP
                                                                                                                #inoctet_count_1_int1014 = snmpget('1.3.6.1.2.1.2.2.1.10.1014', snmp_var)
        inoctet_count_1_int1014 = snmp_inoctet(1014,snmp_var)
        logging.info("-----READING 1_1014- " + str(inoctet_count_1_int1014) + " OCTETS RECEIVED")

                                                                                                                #inoctet_count_1_int1016 = snmpget('1.3.6.1.2.1.2.2.1.10.1016', snmp_var)
        inoctet_count_1_int1016 = snmp_inoctet(1016, snmp_var)
        logging.info("-----READING 1_1016- " + str(inoctet_count_1_int1016) + " OCTETS RECEIVED")

        #OUT OCTET FETCH - PRE-SLEEP
                                                                                                                #outoctet_count_1_int1014 = snmpget('1.3.6.1.2.1.2.2.1.16.1014', snmp_var)
        outoctet_count_1_int1014 = snmp_outoctet(1014, snmp_var)
        logging.info("-----READING 1_1014- " + str(outoctet_count_1_int1014) + " OCTETS SENT")

                                                                                                                #outoctet_count_1_int1016 = snmpget('1.3.6.1.2.1.2.2.1.16.1016', snmp_var)
        outoctet_count_1_int1016 = snmp_outoctet(1016, snmp_var)
        logging.info("-----READING 1_1016- " + str(outoctet_count_1_int1016) + " OCTETS SENT")


        logging.info(str(interval) + " Sec, FOR SLEEP-----")
        time.sleep(interval)
        logging.info("-----INVOKING SLEEP------")

        #IN OCTET FETCH - POST-SLEEP
                                                                                                                #inoctet_count_2_int1014 = snmpget('1.3.6.1.2.1.2.2.1.10.1014',snmp_var)
        inoctet_count_2_int1014 = snmp_inoctet(1014, snmp_var)
        if inoctet_count_2_int1014 < inoctet_count_1_int1014:
            logging.info("-----32 Bit COUNTER JUMP READING-1014----")
            inoctet_count_2_int1014 = 4294967295 + int(inoctet_count_2_int1014)
        else:
             pass
        logging.info("-----READING 2_1014- " + str(inoctet_count_2_int1014) + " OCTETS RECEIVED")

                                                                                                                #inoctet_count_2_int1016 = snmpget('1.3.6.1.2.1.2.2.1.10.1016', snmp_var)
        inoctet_count_2_int1016 = snmp_inoctet(1016, snmp_var)
        if inoctet_count_2_int1016 < inoctet_count_1_int1016:
            logging.info("-----32 Bit COUNTER JUMP READING-1016----")
            inoctet_count_2_int1016 = 4294967295 + int(inoctet_count_2_int1016)
        else:
             pass
        logging.info("-----READING 2-1016- " + str(inoctet_count_2_int1016) + " OCTETS RECEIVED")

        #OUT OCTET FETCH - POST-SLEEP
                                                                                                                #outoctet_count_2_int1014 = snmpget('1.3.6.1.2.1.2.2.1.16.1014', snmp_var)
        outoctet_count_2_int1014 = snmp_outoctet(1014,snmp_var)
        if outoctet_count_2_int1014 < outoctet_count_1_int1014:
            logging.info("-----32 Bit COUNTER JUMP READING-1014--OUT ---")
            outoctet_count_2_int1014 = 4294967295 + int(outoctet_count_2_int1014)
        else:
             pass
        logging.info("-----READING 2_1014- " + str(outoctet_count_2_int1014) + " OCTETS SENT")

                                                                                                                #outoctet_count_2_int1016 = snmpget('1.3.6.1.2.1.2.2.1.16.1016', snmp_var)
        outoctet_count_2_int1016 = snmp_outoctet(1016,snmp_var)
        if outoctet_count_2_int1016 < outoctet_count_1_int1016:
            logging.info("-----32 Bit COUNTER JUMP READING-1016 --OUT ----")
            outoctet_count_2_int1016 = 4294967295 + int(outoctet_count_2_int1016)
        else:
             pass
        logging.info("-----READING 2-1016- " + str(outoctet_count_1_int1016) + " OCTETS SENT")



        ##IN BAND CALCULATIONS
        in_bw_calculate_1014 = (inoctet_count_2_int1014 - inoctet_count_1_int1014) / int(interval)
        in_bw_calculate_1016 = (inoctet_count_2_int1016 - inoctet_count_1_int1016) / int(interval)
        in_bw_calculate_1014 = in_bw_calculate_1014 / 131072
        in_bw_calculate_1016 = in_bw_calculate_1016 / 131072
        in_bw_calculate_1014 = round(in_bw_calculate_1014,3)
        logging.info("IN_Bandwidth Calculated_1014 ----------------------------" + str(in_bw_calculate_1014) + ' Mbps')
        in_bw_calculate_1016 = round(in_bw_calculate_1016, 3)
        logging.info("IN_Bandwidth Calculated_1016 ----------------------------" + str(in_bw_calculate_1016) + ' Mbps')

        #OUT BAND CALCULATIONS
        out_bw_calculate_1014 = (outoctet_count_2_int1014 - outoctet_count_1_int1014) / int(interval)
        out_bw_calculate_1016 = (outoctet_count_2_int1016 - outoctet_count_1_int1016) / int(interval)
        out_bw_calculate_1014 = out_bw_calculate_1014 / 131072
        out_bw_calculate_1016 = out_bw_calculate_1016 / 131072
        out_bw_calculate_1014 = round(out_bw_calculate_1014, 3)
        logging.info("OUT_Bandwidth Calculated_1014 ---------------------------" + str(out_bw_calculate_1014) + ' Mbps')
        out_bw_calculate_1016 = round(out_bw_calculate_1016, 3)
        logging.info("OUT_Bandwidth Calculated_1016 ---------------------------" + str(out_bw_calculate_1016) + ' Mbps')


        # ##STATIC ATTRIBUTES
        #Interface Description
                                                                                                                #int_desr_1014 = str(snmpget('1.3.6.1.2.1.2.2.1.2.1014', snmp_var))
        int_desr_1014 = snmp_intdesr(1014,snmp_var)
        logging.info("Interface Desr 1014 -------------------------------------" + str(int_desr_1014))

                                                                                                                #int_desr_1016 = str(snmpget('1.3.6.1.2.1.2.2.1.2.1016', snmp_var))
        int_desr_1016 = snmp_intdesr(1016,snmp_var)
        logging.info("Interface Desr 1016 -------------------------------------" + str(int_desr_1016))

        #Interface Status
                                                                                                                #int_status_1014 = snmpget('1.3.6.1.2.1.2.2.1.8.1014', snmp_var)
        int_status_1014 = snmp_intstatus(1014,snmp_var)
        if int_status_1014 == 1:
            int_status_1014 = True
        elif int_status_1014 == 2:
            int_status_1014 = False
        logging.info("Interface Status 1014 -----------------------------------" + str(int_status_1014))

                                                                                                                #int_status_1016 = snmpget('1.3.6.1.2.1.2.2.1.8.1016', snmp_var)
        int_status_1016 = snmp_intstatus(1016,snmp_var)
        if int_status_1016 == 1:
            int_status_1016 = True
        elif int_status_1016 == 2:
            int_status_1016 = False
        logging.info("Interface Status 1016 -----------------------------------" + str(int_status_1016))

        #Last Modification
                                                                                                                #int_modified_1014 = snmpget('1.3.6.1.2.1.2.2.1.9.1014', snmp_var)
        int_modified_1014 = snmp_intmodified(1014,snmp_var)
        int_modified_1014 = int(int_modified_1014)/ 8640000
        logging.info("Interface Modification 1014 -----------------------------HOURS---" + str(int_modified_1014))

                                                                                                                #int_modified_1016 = snmpget('1.3.6.1.2.1.2.2.1.9.1016', snmp_var)
        int_modified_1016 = snmp_intmodified(1016,snmp_var)
        int_modified_1016 = int(int_modified_1016) / 8640000
        logging.info("Interface Modification 1016 -----------------------------HOURS---" + str(int_modified_1016))


        # curnt_time = datetime.datetime.now()
        # year = curnt_time.year
        # month = curnt_time.month
        # date = curnt_time.day
        # hour = curnt_time.hour
        # minute = curnt_time.minute
        # second = curnt_time.second
        # logging.info(str(year) + str(month) + str(date) + str(hour) + str(minute) + str(second))

        data_1014 = (int_desr_1014,in_bw_calculate_1014,out_bw_calculate_1014,int_status_1014,int_modified_1014)
        print(data_1014)
        sql_insert_1014 = "INSERT INTO XTREME_CORE_1014(INT_DESR, OUT_TRAFFIC, IN_TRAFFIC, IF_STATUS, IF_LASTCHANGE) VALUES ('%s','%f','%f','%s','%d')" %(int_desr_1014, out_bw_calculate_1014, in_bw_calculate_1014, int_status_1014, int_modified_1014)
        sql_insert_1016 = "INSERT INTO XTREME_CORE_1016(INT_DESR, OUT_TRAFFIC, IN_TRAFFIC, IF_STATUS, IF_LASTCHANGE) VALUES ('%s','%f','%f','%s','%d')" %(int_desr_1016, out_bw_calculate_1016, in_bw_calculate_1016, int_status_1016, int_modified_1016)
        logging.info(sql_insert_1014)
        logging.info(sql_insert_1016)
        try:
            # Execute the SQL command
            cursor.execute(sql_insert_1014)
            cursor.execute(sql_insert_1016)
            # Commit your changes in the database
            db_CISNMS.commit()
        except:
            #print(e)
            # Rollback in case there is any error
            db_CISNMS.rollback()
            db_CISNMS.rollback()
    except Exception as error:
        print(error)
        print("DATA COLLECTION ERROR ENCOUNTERED")




def FIREWALL_dc(interval):

    SNMP_HOST = '172.16.0.1'
    SNMP_PORT = 161
    SNMP_COMMUNITY = 'SNMP_COMMUNITY'
    snmp_var = [SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY]
    try:

        # IN OCTET FETCH - PRE-SLEEP


        inoctet_count_1_LAN_R = snmp_inoctet(6, snmp_var)
        logging.info("-----READING 1_LAN_R- " + str(inoctet_count_1_LAN_R) + " OCTETS RECEIVED")

        inoctet_count_1_WAN_Q = snmp_inoctet(5, snmp_var)
        logging.info("-----READING 1_WAN_Q- " + str(inoctet_count_1_WAN_Q) + " OCTETS RECEIVED")

        inoctet_count_1_DMZ_P = snmp_inoctet(24, snmp_var)
        logging.info("-----READING 1_DMZ_P- " + str(inoctet_count_1_DMZ_P) + " OCTETS RECEIVED")

        #OUT OCTET FETCH PRE SLEEP

        outoctet_count_1_LAN_R = snmp_outoctet(6, snmp_var)
        logging.info("-----READING 1_LAN_R- " + str(outoctet_count_1_LAN_R) + " OCTETS SENT")

        outoctet_count_1_WAN_Q = snmp_outoctet(5, snmp_var)
        logging.info("-----READING 1_WAN_Q- " + str(outoctet_count_1_WAN_Q) + " OCTETS SENT")

        outoctet_count_1_DMZ_P = snmp_outoctet(24, snmp_var)
        logging.info("-----READING 1_DMZ_P- " + str(outoctet_count_1_DMZ_P) + " OCTETS SENT")


        logging.info(str(interval) + " Sec, FOR SLEEP-----")
        time.sleep(interval)
        logging.info("-----INVOKING SLEEP------")

        # IN OCTET FETCH - POST-SLEEP

        inoctet_count_2_LAN_R = snmp_inoctet(6, snmp_var)
        if inoctet_count_2_LAN_R < inoctet_count_1_LAN_R:
            logging.info("-----32 Bit COUNTER JUMP READING-LAN_R----")
            inoctet_count_2_LAN_R = 4294967295 + int(inoctet_count_2_LAN_R)
        else:
            pass
        logging.info("-----READING 2_LAN_R- " + str(inoctet_count_2_LAN_R) + " OCTETS RECEIVED")

        inoctet_count_2_WAN_Q = snmp_inoctet(5, snmp_var)
        if inoctet_count_2_WAN_Q < inoctet_count_1_WAN_Q:
            logging.info("-----32 Bit COUNTER JUMP READING-WAN_Q----")
            inoctet_count_2_WAN_Q = 4294967295 + int(inoctet_count_2_WAN_Q)
        else:
            pass
        logging.info("-----READING 2_WAN_Q- " + str(inoctet_count_2_WAN_Q) + " OCTETS RECEIVED")

        inoctet_count_2_DMZ_P = snmp_inoctet(24, snmp_var)
        if inoctet_count_2_DMZ_P < inoctet_count_1_DMZ_P:
            logging.info("-----32 Bit COUNTER JUMP READING-DMZ_P----")
            inoctet_count_2_DMZ_P = 4294967295 + int(inoctet_count_2_DMZ_P)
        else:
            pass
        logging.info("-----READING 2_DMZ_P " + str(inoctet_count_2_DMZ_P) + " OCTETS RECEIVED")

        #OUT OCTET FETCH POST SLEEP

        outoctet_count_2_LAN_R = snmp_outoctet(6, snmp_var)
        if outoctet_count_2_LAN_R < outoctet_count_1_LAN_R:
            logging.info("-----32 Bit COUNTER JUMP READING- LAN_R--OUT ---")
            outoctet_count_2_LAN_R = 4294967295 + int(outoctet_count_2_LAN_R)
        else:
            pass
        logging.info("-----READING 2_LAN_R- " + str(outoctet_count_2_LAN_R) + " OCTETS SENT")

        outoctet_count_2_WAN_Q = snmp_outoctet(5, snmp_var)
        if outoctet_count_2_WAN_Q < outoctet_count_1_WAN_Q:
            logging.info("-----32 Bit COUNTER JUMP READING- WAN_Q--OUT ---")
            outoctet_count_2_WAN_Q = 4294967295 + int(outoctet_count_2_WAN_Q)
        else:
            pass
        logging.info("-----READING 2_WAN_Q- " + str(outoctet_count_2_WAN_Q) + " OCTETS SENT")

        outoctet_count_2_DMZ_P = snmp_outoctet(24, snmp_var)
        if outoctet_count_2_DMZ_P < outoctet_count_1_DMZ_P:
            logging.info("-----32 Bit COUNTER JUMP READING- DMZ_P--OUT ---")
            outoctet_count_2_DMZ_P = 4294967295 + int(outoctet_count_2_DMZ_P)
        else:
            pass
        logging.info("-----READING 2_DMZ_P- " + str(outoctet_count_2_DMZ_P) + " OCTETS SENT")

        ##IN BAND CALCULATIONS
        in_bw_calculate_LAN_R = (inoctet_count_2_LAN_R - inoctet_count_1_LAN_R) / int(interval)
        in_bw_calculate_LAN_R = in_bw_calculate_LAN_R / 131072
        in_bw_calculate_LAN_R = round(in_bw_calculate_LAN_R, 3)
        logging.info("IN_Bandwidth Calculated_LAN_R ----------------------------" + str(in_bw_calculate_LAN_R) + ' Mbps')

        in_bw_calculate_WAN_Q = (inoctet_count_2_WAN_Q - inoctet_count_1_WAN_Q) / int(interval)
        in_bw_calculate_WAN_Q = in_bw_calculate_WAN_Q / 131072
        in_bw_calculate_WAN_Q = round(in_bw_calculate_WAN_Q, 3)
        logging.info(
            "IN_Bandwidth Calculated_WAN_Q ----------------------------" + str(in_bw_calculate_WAN_Q) + ' Mbps')

        in_bw_calculate_DMZ_P = (inoctet_count_2_DMZ_P - inoctet_count_1_DMZ_P) / int(interval)
        in_bw_calculate_DMZ_P = in_bw_calculate_DMZ_P / 131072
        in_bw_calculate_DMZ_P = round(in_bw_calculate_DMZ_P, 3)
        logging.info(
            "IN_Bandwidth Calculated_DMZ_P ----------------------------" + str(in_bw_calculate_DMZ_P) + ' Mbps')

        # OUT BAND CALCULATIONS
        out_bw_calculate_LAN_R = (outoctet_count_2_LAN_R - outoctet_count_1_LAN_R) / int(interval)
        out_bw_calculate_LAN_R = out_bw_calculate_LAN_R / 131072
        out_bw_calculate_LAN_R = round(out_bw_calculate_LAN_R, 3)
        logging.info(
            "OUT_Bandwidth Calculated_LAN_R ---------------------------" + str(out_bw_calculate_LAN_R) + ' Mbps')


        out_bw_calculate_WAN_Q = (outoctet_count_2_WAN_Q - outoctet_count_1_WAN_Q) / int(interval)
        out_bw_calculate_WAN_Q = out_bw_calculate_WAN_Q / 131072
        out_bw_calculate_WAN_Q = round(out_bw_calculate_WAN_Q, 3)
        logging.info("OUT_Bandwidth Calculated_WAN_Q ---------------------------" + str(out_bw_calculate_WAN_Q) + ' Mbps')

        out_bw_calculate_DMZ_P = (outoctet_count_2_DMZ_P - outoctet_count_1_DMZ_P) / int(interval)
        out_bw_calculate_DMZ_P = out_bw_calculate_DMZ_P / 131072
        out_bw_calculate_DMZ_P = round(out_bw_calculate_DMZ_P, 3)
        logging.info("OUT_Bandwidth Calculated_DMZ_P ---------------------------" + str(out_bw_calculate_DMZ_P) + ' Mbps')

        #STATIC ATTRIBUTES
        # CPU USAGE IN PERCENTAGE
        cpuusage_percent = snmp_cpupercent_FIREWALL(snmp_var)
        logging.info("CPU USAGE % = " + str(cpuusage_percent))

        diskusage_percent = snmp_diskpercent_FIREWALL(snmp_var)
        logging.info("DISK USAGE % = " + str(diskusage_percent))

        memoryusage_percent = snmp_memorypercent_FIREWALL(snmp_var)
        logging.info("RAM USAGE % = " + str(memoryusage_percent))

        live_users = snmp_liveusers_FIREWALL(snmp_var)
        logging.info("Live Users = " + str(live_users))



        data_FIREWALL_dc = (in_bw_calculate_LAN_R, out_bw_calculate_LAN_R,in_bw_calculate_WAN_Q, out_bw_calculate_WAN_Q,in_bw_calculate_DMZ_P, out_bw_calculate_DMZ_P,
                          cpuusage_percent, diskusage_percent, memoryusage_percent, live_users)
        print(data_FIREWALL_dc)
        sql_insert_FIREWALL_dc = "INSERT INTO FIREWALL_DC(LAN_IN, LAN_OUT, WAN_IN, WAN_OUT, DMZ_IN, DMZ_OUT, CPU, DISK, MEMORY, LIVE_USERS) VALUES ('%f','%f','%f','%f','%f','%f','%d','%d','%d','%d')" % (in_bw_calculate_LAN_R, out_bw_calculate_LAN_R,in_bw_calculate_WAN_Q, out_bw_calculate_WAN_Q,in_bw_calculate_DMZ_P, out_bw_calculate_DMZ_P, cpuusage_percent, diskusage_percent, memoryusage_percent, live_users)
        logging.info(sql_insert_FIREWALL_dc)

        try:
            # Execute the SQL command
            cursor.execute(sql_insert_FIREWALL_dc)
            # Commit your changes in the database
            db_CISNMS.commit()
        except:
            # print(e)
            # Rollback in case there is any error
            db_CISNMS.rollback()
    except Exception as error:
        print(error)
        print("FIREWALL_DC DATA COLLECTION ERROR ENCOUNTERED")


def FIREWALL_campus(interval):

    SNMP_HOST = '192.168.100.2'
    SNMP_PORT = 161
    SNMP_COMMUNITY = 'SNMP_COMMUNITY'
    snmp_var = [SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY]
    try:

        # IN OCTET FETCH - PRE-SLEEP


        inoctet_count_1_LAN_D1 = snmp_inoctet(8, snmp_var)
        logging.info("-----READING 1_LAN_D1- " + str(inoctet_count_1_LAN_D1) + " OCTETS RECEIVED")

        inoctet_count_1_WAN_D2 = snmp_inoctet(7, snmp_var)
        logging.info("-----READING 1_WAN_D2- " + str(inoctet_count_1_WAN_D2) + " OCTETS RECEIVED")

        inoctet_count_1_DMZ_A2 = snmp_inoctet(9, snmp_var)
        logging.info("-----READING 1_DMZ_A2- " + str(inoctet_count_1_DMZ_A2) + " OCTETS RECEIVED")

        #OUT OCTET FETCH PRE SLEEP

        outoctet_count_1_LAN_D1 = snmp_outoctet(8, snmp_var)
        logging.info("-----READING 1_LAN_D1- " + str(outoctet_count_1_LAN_D1) + " OCTETS SENT")

        outoctet_count_1_WAN_D2 = snmp_outoctet(7, snmp_var)
        logging.info("-----READING 1_WAN_D2- " + str(outoctet_count_1_WAN_D2) + " OCTETS SENT")

        outoctet_count_1_DMZ_A2 = snmp_outoctet(9, snmp_var)
        logging.info("-----READING 1_DMZ_A2- " + str(outoctet_count_1_DMZ_A2) + " OCTETS SENT")


        logging.info(str(interval) + " Sec, FOR SLEEP-----")
        time.sleep(interval)
        logging.info("-----INVOKING SLEEP------")

        # IN OCTET FETCH - POST-SLEEP

        inoctet_count_2_LAN_D1 = snmp_inoctet(8, snmp_var)
        if inoctet_count_2_LAN_D1 < inoctet_count_1_LAN_D1:
            logging.info("-----32 Bit COUNTER JUMP READING-LAN_D1----")
            inoctet_count_2_LAN_D1 = 4294967295 + int(inoctet_count_2_LAN_D1)
        else:
            pass
        logging.info("-----READING 2_LAN_D1- " + str(inoctet_count_2_LAN_D1) + " OCTETS RECEIVED")

        inoctet_count_2_WAN_D2 = snmp_inoctet(7, snmp_var)
        if inoctet_count_2_WAN_D2 < inoctet_count_1_WAN_D2:
            logging.info("-----32 Bit COUNTER JUMP READING-WAN_D2----")
            inoctet_count_2_WAN_D2 = 4294967295 + int(inoctet_count_2_WAN_D2)
        else:
            pass
        logging.info("-----READING 2_WAN_D2- " + str(inoctet_count_2_WAN_D2) + " OCTETS RECEIVED")

        inoctet_count_2_DMZ_A2 = snmp_inoctet(9, snmp_var)
        if inoctet_count_2_DMZ_A2 < inoctet_count_1_DMZ_A2:
            logging.info("-----32 Bit COUNTER JUMP READING-DMZ_A2----")
            inoctet_count_2_DMZ_A2 = 4294967295 + int(inoctet_count_2_DMZ_A2)
        else:
            pass
        logging.info("-----READING 2_DMZ_A2 " + str(inoctet_count_2_DMZ_A2) + " OCTETS RECEIVED")

        #OUT OCTET FETCH POST SLEEP

        outoctet_count_2_LAN_D1 = snmp_outoctet(8, snmp_var)
        if outoctet_count_2_LAN_D1 < outoctet_count_1_LAN_D1:
            logging.info("-----32 Bit COUNTER JUMP READING- LAN_D1--OUT ---")
            outoctet_count_2_LAN_D1 = 4294967295 + int(outoctet_count_2_LAN_D1)
        else:
            pass
        logging.info("-----READING 2_LAN_D1- " + str(outoctet_count_2_LAN_D1) + " OCTETS SENT")

        outoctet_count_2_WAN_D2 = snmp_outoctet(7, snmp_var)
        if outoctet_count_2_WAN_D2 < outoctet_count_1_WAN_D2:
            logging.info("-----32 Bit COUNTER JUMP READING- WAN_D2--OUT ---")
            outoctet_count_2_WAN_D2 = 4294967295 + int(outoctet_count_2_WAN_D2)
        else:
            pass
        logging.info("-----READING 2_WAN_D2- " + str(outoctet_count_2_WAN_D2) + " OCTETS SENT")

        outoctet_count_2_DMZ_A2 = snmp_outoctet(9, snmp_var)
        if outoctet_count_2_DMZ_A2 < outoctet_count_1_DMZ_A2:
            logging.info("-----32 Bit COUNTER JUMP READING- DMZ_A2--OUT ---")
            outoctet_count_2_DMZ_A2 = 4294967295 + int(outoctet_count_2_DMZ_A2)
        else:
            pass
        logging.info("-----READING 2_DMZ_A2- " + str(outoctet_count_2_DMZ_A2) + " OCTETS SENT")

        ##IN BAND CALCULATIONS
        in_bw_calculate_LAN_D1 = (inoctet_count_2_LAN_D1 - inoctet_count_1_LAN_D1) / int(interval)
        in_bw_calculate_LAN_D1 = in_bw_calculate_LAN_D1 / 131072
        in_bw_calculate_LAN_D1 = round(in_bw_calculate_LAN_D1, 3)
        logging.info("IN_Bandwidth Calculated_LAN_D1 ----------------------------" + str(in_bw_calculate_LAN_D1) + ' Mbps')

        in_bw_calculate_WAN_D2 = (inoctet_count_2_WAN_D2 - inoctet_count_1_WAN_D2) / int(interval)
        in_bw_calculate_WAN_D2 = in_bw_calculate_WAN_D2 / 131072
        in_bw_calculate_WAN_D2 = round(in_bw_calculate_WAN_D2, 3)
        logging.info(
            "IN_Bandwidth Calculated_WAN_D2 ----------------------------" + str(in_bw_calculate_WAN_D2) + ' Mbps')

        in_bw_calculate_DMZ_A2 = (inoctet_count_2_DMZ_A2 - inoctet_count_1_DMZ_A2) / int(interval)
        in_bw_calculate_DMZ_A2 = in_bw_calculate_DMZ_A2 / 131072
        #print(in_bw_calculate_DMZ_A2)
        in_bw_calculate_DMZ_A2 = round(in_bw_calculate_DMZ_A2, 3)
        logging.info("IN_Bandwidth Calculated_DMZ_A2 ----------------------------" + str(in_bw_calculate_DMZ_A2) + ' Mbps')

        # OUT BAND CALCULATIONS
        out_bw_calculate_LAN_D1 = (outoctet_count_2_LAN_D1 - outoctet_count_1_LAN_D1) / int(interval)
        out_bw_calculate_LAN_D1 = out_bw_calculate_LAN_D1 / 131072
        out_bw_calculate_LAN_D1 = round(out_bw_calculate_LAN_D1, 3)
        logging.info(
            "OUT_Bandwidth Calculated_LAN_D1 ---------------------------" + str(out_bw_calculate_LAN_D1) + ' Mbps')


        out_bw_calculate_WAN_D2 = (outoctet_count_2_WAN_D2 - outoctet_count_1_WAN_D2) / int(interval)
        out_bw_calculate_WAN_D2 = out_bw_calculate_WAN_D2 / 131072
        out_bw_calculate_WAN_D2 = round(out_bw_calculate_WAN_D2, 3)
        logging.info("OUT_Bandwidth Calculated_WAN_D2 ---------------------------" + str(out_bw_calculate_WAN_D2) + ' Mbps')

        out_bw_calculate_DMZ_A2 = (outoctet_count_2_DMZ_A2 - outoctet_count_1_DMZ_A2) / int(interval)
        out_bw_calculate_DMZ_A2 = out_bw_calculate_DMZ_A2 / 131072
        out_bw_calculate_DMZ_A2 = round(out_bw_calculate_DMZ_A2, 3)
        logging.info("OUT_Bandwidth Calculated_DMZ_A2 ---------------------------" + str(out_bw_calculate_DMZ_A2) + ' Mbps')

        #STATIC ATTRIBUTES
        # CPU USAGE IN PERCENTAGE
        cpuusage_percent = snmp_cpupercent_FIREWALL(snmp_var)
        logging.info("CPU USAGE % = " + str(cpuusage_percent))

        diskusage_percent = snmp_diskpercent_FIREWALL(snmp_var)
        logging.info("DISK USAGE % = " + str(diskusage_percent))

        memoryusage_percent = snmp_memorypercent_FIREWALL(snmp_var)
        logging.info("RAM USAGE % = " + str(memoryusage_percent))

        live_users = snmp_liveusers_FIREWALL(snmp_var)
        logging.info("Live Users = " + str(live_users))



        data_FIREWALL_campus = (in_bw_calculate_LAN_D1, out_bw_calculate_LAN_D1,in_bw_calculate_WAN_D2, out_bw_calculate_WAN_D2,in_bw_calculate_DMZ_A2, out_bw_calculate_DMZ_A2,
                          cpuusage_percent, diskusage_percent, memoryusage_percent, live_users)
        print(data_FIREWALL_campus)
        sql_insert_FIREWALL_campus = "INSERT INTO FIREWALL_CAMPUS(LAN_IN, LAN_OUT, WAN_IN, WAN_OUT, DMZ_IN, DMZ_OUT, CPU, DISK, MEMORY, LIVE_USERS) VALUES ('%f','%f','%f','%f','%f','%f','%d','%d','%d','%d')" % (in_bw_calculate_LAN_D1, out_bw_calculate_LAN_D1,in_bw_calculate_WAN_D2, out_bw_calculate_WAN_D2,in_bw_calculate_DMZ_A2, out_bw_calculate_DMZ_A2, cpuusage_percent, diskusage_percent, memoryusage_percent, live_users)
        logging.info(sql_insert_FIREWALL_campus)

        try:
            # Execute the SQL command
            cursor.execute(sql_insert_FIREWALL_campus)
            # Commit your changes in the database
            db_CISNMS.commit()
        except:
            # print(e)
            # Rollback in case there is any error
            db_CISNMS.rollback()
    except Exception as error:
        print(error)
        print("FIREWALL_CAMPUS DATA COLLECTION ERROR ENCOUNTERED")


def FIREWALL_academic(interval):

    SNMP_HOST = '192.168.200.2'
    SNMP_PORT = 161
    SNMP_COMMUNITY = 'SNMP_COMMUNITY'
    snmp_var = [SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY]
    try:

        # IN OCTET FETCH - PRE-SLEEP


        inoctet_count_1_LAN_D1 = snmp_inoctet(8, snmp_var)
        logging.info("-----READING 1_LAN_D1- " + str(inoctet_count_1_LAN_D1) + " OCTETS RECEIVED")

        inoctet_count_1_WAN_D2 = snmp_inoctet(7, snmp_var)
        logging.info("-----READING 1_WAN_D2- " + str(inoctet_count_1_WAN_D2) + " OCTETS RECEIVED")

        inoctet_count_1_DMZ_A2 = snmp_inoctet(10, snmp_var)
        logging.info("-----READING 1_DMZ_A2- " + str(inoctet_count_1_DMZ_A2) + " OCTETS RECEIVED")

        #OUT OCTET FETCH PRE SLEEP

        outoctet_count_1_LAN_D1 = snmp_outoctet(8, snmp_var)
        logging.info("-----READING 1_LAN_D1- " + str(outoctet_count_1_LAN_D1) + " OCTETS SENT")

        outoctet_count_1_WAN_D2 = snmp_outoctet(7, snmp_var)
        logging.info("-----READING 1_WAN_D2- " + str(outoctet_count_1_WAN_D2) + " OCTETS SENT")

        outoctet_count_1_DMZ_A2 = snmp_outoctet(10, snmp_var)
        logging.info("-----READING 1_DMZ_A2- " + str(outoctet_count_1_DMZ_A2) + " OCTETS SENT")


        logging.info(str(interval) + " Sec, FOR SLEEP-----")
        time.sleep(interval)
        logging.info("-----INVOKING SLEEP------")

        # IN OCTET FETCH - POST-SLEEP

        inoctet_count_2_LAN_D1 = snmp_inoctet(8, snmp_var)
        if inoctet_count_2_LAN_D1 < inoctet_count_1_LAN_D1:
            logging.info("-----32 Bit COUNTER JUMP READING-LAN_D1----")
            inoctet_count_2_LAN_D1 = 4294967295 + int(inoctet_count_2_LAN_D1)
        else:
            pass
        logging.info("-----READING 2_LAN_D1- " + str(inoctet_count_2_LAN_D1) + " OCTETS RECEIVED")

        inoctet_count_2_WAN_D2 = snmp_inoctet(7, snmp_var)
        if inoctet_count_2_WAN_D2 < inoctet_count_1_WAN_D2:
            logging.info("-----32 Bit COUNTER JUMP READING-WAN_D2----")
            inoctet_count_2_WAN_D2 = 4294967295 + int(inoctet_count_2_WAN_D2)
        else:
            pass
        logging.info("-----READING 2_WAN_D2- " + str(inoctet_count_2_WAN_D2) + " OCTETS RECEIVED")

        inoctet_count_2_DMZ_A2 = snmp_inoctet(10, snmp_var)
        if inoctet_count_2_DMZ_A2 < inoctet_count_1_DMZ_A2:
            logging.info("-----32 Bit COUNTER JUMP READING-DMZ_A2----")
            inoctet_count_2_DMZ_A2 = 4294967295 + int(inoctet_count_2_DMZ_A2)
        else:
            pass
        logging.info("-----READING 2_DMZ_A2 " + str(inoctet_count_2_DMZ_A2) + " OCTETS RECEIVED")

        #OUT OCTET FETCH POST SLEEP

        outoctet_count_2_LAN_D1 = snmp_outoctet(8, snmp_var)
        if outoctet_count_2_LAN_D1 < outoctet_count_1_LAN_D1:
            logging.info("-----32 Bit COUNTER JUMP READING- LAN_D1--OUT ---")
            outoctet_count_2_LAN_D1 = 4294967295 + int(outoctet_count_2_LAN_D1)
        else:
            pass
        logging.info("-----READING 2_LAN_D1- " + str(outoctet_count_2_LAN_D1) + " OCTETS SENT")

        outoctet_count_2_WAN_D2 = snmp_outoctet(7, snmp_var)
        if outoctet_count_2_WAN_D2 < outoctet_count_1_WAN_D2:
            logging.info("-----32 Bit COUNTER JUMP READING- WAN_D2--OUT ---")
            outoctet_count_2_WAN_D2 = 4294967295 + int(outoctet_count_2_WAN_D2)
        else:
            pass
        logging.info("-----READING 2_WAN_D2- " + str(outoctet_count_2_WAN_D2) + " OCTETS SENT")

        outoctet_count_2_DMZ_A2 = snmp_outoctet(10, snmp_var)
        if outoctet_count_2_DMZ_A2 < outoctet_count_1_DMZ_A2:
            logging.info("-----32 Bit COUNTER JUMP READING- DMZ_A2--OUT ---")
            outoctet_count_2_DMZ_A2 = 4294967295 + int(outoctet_count_2_DMZ_A2)
        else:
            pass
        logging.info("-----READING 2_DMZ_A2- " + str(outoctet_count_2_DMZ_A2) + " OCTETS SENT")

        ##IN BAND CALCULATIONS
        in_bw_calculate_LAN_D1 = (inoctet_count_2_LAN_D1 - inoctet_count_1_LAN_D1) / int(interval)
        in_bw_calculate_LAN_D1 = in_bw_calculate_LAN_D1 / 131072
        in_bw_calculate_LAN_D1 = round(in_bw_calculate_LAN_D1, 3)
        logging.info("IN_Bandwidth Calculated_LAN_D1 ----------------------------" + str(in_bw_calculate_LAN_D1) + ' Mbps')

        in_bw_calculate_WAN_D2 = (inoctet_count_2_WAN_D2 - inoctet_count_1_WAN_D2) / int(interval)
        in_bw_calculate_WAN_D2 = in_bw_calculate_WAN_D2 / 131072
        in_bw_calculate_WAN_D2 = round(in_bw_calculate_WAN_D2, 3)
        logging.info(
            "IN_Bandwidth Calculated_WAN_D2 ----------------------------" + str(in_bw_calculate_WAN_D2) + ' Mbps')

        in_bw_calculate_DMZ_A2 = (inoctet_count_2_DMZ_A2 - inoctet_count_1_DMZ_A2) / int(interval)
        in_bw_calculate_DMZ_A2 = int(in_bw_calculate_DMZ_A2 / 131072)
        #logging.info("IN_Bandwidth Calculated_DMZ_A2- UNROUNDED **************   " + str(in_bw_calculate_DMZ_A2))
        in_bw_calculate_DMZ_A2 = round(in_bw_calculate_DMZ_A2, 3)
        logging.info(
            "IN_Bandwidth Calculated_DMZ_A2 ----------------------------" + str(in_bw_calculate_DMZ_A2) + ' Mbps')

        # OUT BAND CALCULATIONS
        out_bw_calculate_LAN_D1 = (outoctet_count_2_LAN_D1 - outoctet_count_1_LAN_D1) / int(interval)
        out_bw_calculate_LAN_D1 = out_bw_calculate_LAN_D1 / 131072
        out_bw_calculate_LAN_D1 = round(out_bw_calculate_LAN_D1, 3)
        logging.info("OUT_Bandwidth Calculated_LAN_D1 ---------------------------" + str(out_bw_calculate_LAN_D1) + ' Mbps')


        out_bw_calculate_WAN_D2 = (outoctet_count_2_WAN_D2 - outoctet_count_1_WAN_D2) / int(interval)
        out_bw_calculate_WAN_D2 = out_bw_calculate_WAN_D2 / 131072
        out_bw_calculate_WAN_D2 = round(out_bw_calculate_WAN_D2, 3)
        logging.info("OUT_Bandwidth Calculated_WAN_D2 ---------------------------" + str(out_bw_calculate_WAN_D2) + ' Mbps')

        out_bw_calculate_DMZ_A2 = (outoctet_count_2_DMZ_A2 - outoctet_count_1_DMZ_A2) / int(interval)
        out_bw_calculate_DMZ_A2 = out_bw_calculate_DMZ_A2 / 131072
        out_bw_calculate_DMZ_A2 = round(out_bw_calculate_DMZ_A2, 3)
        logging.info("OUT_Bandwidth Calculated_DMZ_A2 ---------------------------" + str(out_bw_calculate_DMZ_A2) + ' Mbps')

        #STATIC ATTRIBUTES
        # CPU USAGE IN PERCENTAGE
        cpuusage_percent = snmp_cpupercent_FIREWALL(snmp_var)
        logging.info("CPU USAGE % = " + str(cpuusage_percent))

        diskusage_percent = snmp_diskpercent_FIREWALL(snmp_var)
        logging.info("DISK USAGE % = " + str(diskusage_percent))

        memoryusage_percent = snmp_memorypercent_FIREWALL(snmp_var)
        logging.info("RAM USAGE % = " + str(memoryusage_percent))

        live_users = snmp_liveusers_FIREWALL(snmp_var)
        logging.info("Live Users = " + str(live_users))



        data_FIREWALL_academic = (in_bw_calculate_LAN_D1, out_bw_calculate_LAN_D1,in_bw_calculate_WAN_D2, out_bw_calculate_WAN_D2,in_bw_calculate_DMZ_A2, out_bw_calculate_DMZ_A2,
                          cpuusage_percent, diskusage_percent, memoryusage_percent, live_users)
        print(data_FIREWALL_academic)
        sql_insert_FIREWALL_academic = "INSERT INTO FIREWALL_ACADEMIC(LAN_IN, LAN_OUT, WAN_IN, WAN_OUT, DMZ_IN, DMZ_OUT, CPU, DISK, MEMORY, LIVE_USERS) VALUES ('%f','%f','%f','%f','%f','%f','%d','%d','%d','%d')" % (in_bw_calculate_LAN_D1, out_bw_calculate_LAN_D1,in_bw_calculate_WAN_D2, out_bw_calculate_WAN_D2,in_bw_calculate_DMZ_A2, out_bw_calculate_DMZ_A2, cpuusage_percent, diskusage_percent, memoryusage_percent, live_users)
        logging.info(sql_insert_FIREWALL_academic)

        try:
            # Execute the SQL command
            cursor.execute(sql_insert_FIREWALL_academic)
            # Commit your changes in the database
            db_CISNMS.commit()
        except:
            # print(e)
            # Rollback in case there is any error
            db_CISNMS.rollback()
    except Exception as error:
        print(error)
        print("FIREWALL_ACADEMIC DATA COLLECTION ERROR ENCOUNTERED")




def wlc_controller(interval):

    SNMP_HOST = '10.101.0.101'
    SNMP_PORT = 161
    SNMP_COMMUNITY = 'SNMP_COMMUNITY'
    snmp_var = [SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY]
    try:
        wlc_ap_adopted = snmp_ap_adopted(snmp_var)
        logging.info("-----TOTAL AP ADOPTED-- " + str(wlc_ap_adopted))

        wlc_clients_connected = snmp_total_clients(snmp_var)
        logging.info("-----TOTAL CLIENTS CONNECTED-- " + str(wlc_clients_connected))

        wlc_campus_clients = snmp_wlan_clients(1, snmp_var)
        logging.info("-----CAMPUS CLIENTS CONNECTED-- " + str(wlc_campus_clients))

        wlc_academic_clients = snmp_wlan_clients(6, snmp_var)
        logging.info("-----ACADEMIC CLIENTS CONNECTED-- " + str(wlc_academic_clients))

        wlc_hotspot_clients = snmp_wlan_clients(4, snmp_var)
        logging.info("-----HOTSPOT CLIENTS CONNECTED-- " + str(wlc_hotspot_clients))

        wlc_temprature = snmp_wlc_temprature(snmp_var)
        logging.info("CURRENT WLC IN-SUCTION TEMPRATURE---------" + str(wlc_temprature) + ' ^C')

        wlc_uptime = snmp_wlc_uptime(snmp_var)
        wlc_uptime = round((wlc_uptime / 8640000), 3)
        logging.info("CURRENT WLC UPTIME---------" + str(wlc_uptime))


        ########PORT BANDWIDTH CALCULATIONS

        inoctet_count_1_int4 = snmp_inoctet(4, snmp_var)
        logging.info("-----READING-IN WLC PORT_4- " + str(inoctet_count_1_int4) + " OCTETS RECEIVED")

        outoctet_count_1_int4 = snmp_outoctet(4, snmp_var)
        logging.info("-----READING-OUT WLC PORT_4- " + str(outoctet_count_1_int4) + " OCTETS SENT")

        logging.info(str(interval) + " Sec, FOR SLEEP-----")
        time.sleep(interval)
        logging.info("-----INVOKING SLEEP-WLC-----")

        inoctet_count_2_int4 = snmp_inoctet(4, snmp_var)
        if inoctet_count_2_int4 < inoctet_count_1_int4:
            logging.info("-----32 Bit COUNTER JUMP READING-1014----")
            inoctet_count_2_int4 = 4294967295 + int(inoctet_count_2_int4)
        else:
            pass
        logging.info("-----READING-IN 2_WLC PORT 4 " + str(inoctet_count_2_int4) + " OCTETS RECEIVED")


        outoctet_count_2_int4 = snmp_outoctet(4, snmp_var)
        if outoctet_count_2_int4 < outoctet_count_1_int4:
            logging.info("-----32 Bit COUNTER JUMP READING-1014----")
            outoctet_count_2_int4 = 4294967295 + int(outoctet_count_2_int4)
        else:
            pass
        logging.info("-----READING-OUT 2_WLC PORT 4 " + str(outoctet_count_2_int4) + " OCTETS SENT")

        ##IN BAND CALCULATIONS
        in_bw_calculate_int4 = (inoctet_count_2_int4 - inoctet_count_1_int4) / int(interval)
        in_bw_calculate_int4 = in_bw_calculate_int4 / 131072
        wlc_in_bw_calculate_int4 = round(in_bw_calculate_int4, 3)
        logging.info("IN_Bandwidth Calculated_WLC PORT 4 ----------------------------" + str(wlc_in_bw_calculate_int4) + ' Mbps')

        ##OUT BAND CALCULATIONS
        out_bw_calculate_int4 = (outoctet_count_2_int4 - outoctet_count_1_int4) / int(interval)
        out_bw_calculate_int4 = out_bw_calculate_int4 / 131072
        wlc_out_bw_calculate_int4 = round(out_bw_calculate_int4, 3)
        logging.info("OUT_Bandwidth Calculated_WLC PORT 4 ----------------------------" + str(wlc_out_bw_calculate_int4) + ' Mbps')

        #data_wlc_controller = (wlc_ap_adopted,wlc_clients_connected,wlc_campus_clients,wlc_academic_clients,wlc_hotspot_clients,wlc_temprature,wlc_uptime,wlc_in_bw_calculate_int4,wlc_out_bw_calculate_int4)
        sql_insert_wlc_controller = "INSERT INTO WLC_controller(AP_ADOPTION, TOTAL_CLIENTS, CAMPUS_CLIENTS, ACADEMIC_CLIENTS, HOTSPOT_CLIENTS, WLC_TEMPRATURE, WLC_UPTIME, WLC_IN_BW, WLC_OUT_BW) VALUES ('%d','%d','%d','%d','%d','%f','%s','%f','%f')" %(wlc_ap_adopted, wlc_clients_connected,wlc_campus_clients, wlc_academic_clients, wlc_hotspot_clients, wlc_temprature, wlc_uptime, wlc_in_bw_calculate_int4, wlc_out_bw_calculate_int4)
        logging.info(sql_insert_wlc_controller)

        try:
            # Execute the SQL command
            cursor.execute(sql_insert_wlc_controller)
            # Commit your changes in the database
            db_CISNMS.commit()
        except:
            # print(e)
            # Rollback in case there is any error
            db_CISNMS.rollback()


    except Exception as error:
        print(error)
        print("WLC controller DATA COLLECTION ERROR ENCOUNTERED")
