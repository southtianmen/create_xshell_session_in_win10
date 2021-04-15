import configparser


class MyConfigParser(configparser.RawConfigParser):
    """
    set ConfigParser options for case sensitive.
    """

    def __init__(self, defaults=None):
        configparser.RawConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

    def write(self, fp, space_around_delimiters=True):
        """Write an .ini-format representation of the configuration state.

        If `space_around_delimiters' is True (the default), delimiters
        between keys and values are surrounded by spaces.
        """
        if space_around_delimiters:
            d = "{}".format(self._delimiters[0])
            # d = " {} ".format(self._delimiters[0])
        else:
            d = self._delimiters[0]
        if self._defaults:
            self._write_section(fp, self.default_section,
                                self._defaults.items(), d)
        for section in self._sections:
            self._write_section(fp, section,
                                self._sections[section].items(), d)
