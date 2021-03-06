#===========================================================================
#
# Tests for: insteont_mqtt/message/InpAllLinkStatus.py
#
#===========================================================================
import insteon_mqtt.message as Msg


class Test_InpAllLinkStatus:
    #-----------------------------------------------------------------------
    def test_ack(self):
        b = bytes([0x02, 0x58, 0x06])
        obj = Msg.InpAllLinkStatus.from_bytes(b)

        assert obj.is_ack is True

        str(obj)

    #-----------------------------------------------------------------------
    def test_nak(self):
        b = bytes([0x02, 0x58, 0xff])
        obj = Msg.InpAllLinkStatus.from_bytes(b)

        assert obj.is_ack is False

        str(obj)

    #-----------------------------------------------------------------------


#===========================================================================
