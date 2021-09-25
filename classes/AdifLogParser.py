import datetime
import adif_io
from Qso import Qso


class AdifLogParser:
    def parse(filename: str):
        qso_list = []
        items, header = adif_io.read_from_file(filename)
        for item in items:
            qso_list.append(Qso(
                callsign=item.get('CALL'),
                datetime=datetime.datetime(
                    int(item.get('QSO_DATE')[:4]), int(item.get('QSO_DATE')[4:6]), int(item.get('QSO_DATE')[6:8]), int(item.get('TIME_ON')[:2]), int(item.get('TIME_ON')[2:4])),
                rst_sent=item.get('RST_SENT'),
                band=item.get('BAND'),
                mode=item.get('MODE'),
                comment=item.get('COMMENT') or '',
                frequency=item.get('FREQ') or '',
                my_antenna=item.get('MY_ANTENNA') or '',
                my_qth=item.get('MY_QTH') or '',
                my_cq_zone=item.get('MY_CQ_ZONE') or '',
                my_dxcc=item.get('MY_DXCC') or '',
                my_gridsquare=item.get('MY_GRIDSQUARE') or '',
                my_iota=item.get('MY_IOTA') or '',
                my_rig=item.get('MY_RIG') or ''
            ))
        return tuple(qso_list)
