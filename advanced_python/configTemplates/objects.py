class L2Interface(object):
    def __init__(self, intname, trunk_description="<===Trunk Port===>", host_description="<===User Port===>", vlan=10, voice_vlan=20):
        self.trunk_description = trunk_description
        self.intname = intname
        self.host_description = host_description
        self.vlan = vlan
        self.voice_vlan = voice_vlan