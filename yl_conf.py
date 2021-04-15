#!/usr/bin/env python
# author:yl

import os
from yl_configparser import MyConfigParser


class rcf(object):
    def __init__(self, configfile=None):
        self.configfile = configfile if configfile != None else "test.conf"
        with open('template.ini', encoding='utf-8', mode='r') as f:
            result = f.readlines()
            result = "\n".join(result)
        if not os.path.isfile(self.configfile):
            with open(self.configfile, "w", encoding='utf-8') as f:
                f.write(result)
        self.fob = MyConfigParser()
        self.fob.read(self.configfile, encoding="utf-8")
        self.session = self.fob.sections()
        self.items = [dict(self.fob.items(s)) for s in self.session]
        self.metadata = dict(map(lambda x, y: [x, y], self.session, self.items))

    def get_medate(self):
        fob = MyConfigParser()
        fob.read(self.configfile, encoding="utf-8")
        session = fob.sections()
        items = [dict(fob.items(s)) for s in session]
        metadata = dict(map(lambda x, y: [x, y], session, items))
        return metadata

    def add_conf(self, s, **kwargs):
        if s and s not in self.session:
            self.fob.add_section(s)
            for k, v in kwargs.items():
                self.fob.set(s, k, v)
            with open(self.configfile, "w", encoding="utf-8") as f:
                self.fob.write(f)
        if s in self.session:
            for k, v in kwargs.items():
                self.fob.set(s, k, v)
            with open(self.configfile, "w", encoding="utf-8") as f:
                self.fob.write(f)
        return self.get_medate()

    def update_conf(self, s, k, new):
        data = self.get_medate()
        data[s][k] = new
        config = MyConfigParser()
        config.read(self.configfile)
        if s in config.sections():
            for x, y in data.items():
                config[x] = y
            with open(self.configfile, "w", encoding='utf-8') as f:
                config.write(f)
            return self.get_medate()
        elif s not in config.sections():
            print("not support update the session already exists")
            __import__('sys').exit(100)

    def delete_conf(self, s):
        config = MyConfigParser()
        config.read(self.configfile)
        config.remove_section(s)
        old = config.sections()
        if s in old:
            with open(self.configfile, "w", encoding='utf-8') as f:
                config.write(f)
            return self.get_medate()
        else:
            return "%s not in %s" % (s, old)


if __name__ == "__main__":
    pass
