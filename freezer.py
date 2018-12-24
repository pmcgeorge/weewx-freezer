import syslog
import weewx
from weewx.wxengine import StdService

class FreezerService(StdService):
    def __init__(self, engine, config_dict):
        super(FreezerService, self).__init__(engine, config_dict)      
        d = config_dict.get('FreezerService', {})
        self.filename = d.get('filename', '/home/paul/sensordata/freezertemp.txt')
        syslog.syslog(syslog.LOG_INFO, "freezer: using %s" % self.filename)
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.read_file)
    
    def read_file(self, event):
        try:
            with open(self.filename) as f:
                value = f.read()
            syslog.syslog(syslog.LOG_DEBUG, "freezer: found value of %s" % value)
            event.record['extraTemp1'] = float(value)
        except Exception, e:
            syslog.syslog(syslog.LOG_ERR, "freezer: cannot read value: %s" % e)