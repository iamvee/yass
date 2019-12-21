class WalkDict(dict):
    """
    >>> sample_dct = {'a1': {'b1': {c1': { 'd1': 100 }}}}
    >>> sample_new = WalkDict(sample_dict)
    >>> # check values
    >>> sample_new['a1']['b1']['c1']
    {'d1': 100}
    >>> sample_dct['#/a1/b1/c1']
    {'d1': 100}
    """
    def __getitem__(self, item: str):
        if not item.startswith('#/'):
            return super().__getitem__(item)


        sects = item.replace('#/', '').split('/')
        temp = self
        for sect in sects:
            temp = temp[sect]
        
        return temp

