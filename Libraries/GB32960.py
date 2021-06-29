

import struct
import ctypes
import datetime
from robot.api.deco import library, keyword



ROBOT_AUTO_KEYWORDS = False


@library(scope="GLOBAL")
class GB32960(object):
    
    def get_body_prefix_fields(self):
        now = datetime.datetime.now()
        return now.year // 100, now.month, now.day, now.hour, now.minute, now.second, self._serial
      
    def get_head_and_dummy_body(self, cmd):
        head = struct.Struct(">BBBB17sBH")
        body = struct.Struct(">BBBBBBH")
        buff = ctypes.create_string_buffer(head.size + body.size + 1)
        head_fields = (0x23, 0x23, cmd, 0xfe, self._vin, 0x01, body.size)
        body_fields = self.get_body_prefix_fields()
        head.pack_into(buff, 0, *head_fields)
        body.pack_into(buff, head.size, *body_fields)
        # TODO: bcc CHECK
        return buff.raw
      
      def get_dummy_head(self, cmd):
          head = struct.Struct(">BBBB17sBH")
          buff = ctypes.create_string_buffer(head.size + 1)
          head_fileds = (0x23, 0x23, cmd, 0xfe, self._vin, 0x01, 0x00)
          head.pack_into(buff, 0, *head_fields)
          # TODO: bcc check
          return buff.raw
        
      @keyword("GB32960 Codec Init")
      def init(self, vin):
          self._vin = bytes(vin, encoding="utf8")
          self._serial = 0
          
      @keyword("Encode GB32960 Vehicle Login")
      def gen_vehicle_login(self, iccid):
          head = struct.Struct(">BBBB17sBH")
          body_prefix = struct.Struct(">BBBBBBH")
          body_append = struct.Struct(">20sBB")
          buff = ctypes.create_string_buffer(head.size + body_prefix.size + body_append.size + 1)
          head_fields = (0x23, 0x23, 0x01, 0xfe, self._vin, 0x01, body_prefix.size + body_append.size)
          body_prefix_fields = self.get_body_prefix_fields()
          body_append_fields = (bytes(iccid, encoding="utf8"), 0x00, 0x00)
          head.pack_into(buff, 0, *head_fields)
          body_prefix.pack_into(buff, head.size, *body_prefix_fields)
          body_append.pack_into(buff, head.size + body_prefix.size, *body_append_fields)
          # TODO: bcc check
          return buff.raw
        
      @keyword("Encode GB32960 Vehicle Logout")
      def gen_vehicle_logout(self):
          return self.get_head_and_dummy_body(0x04)
        
      @keyword("Encode GB32960 Platform Login")
      def gen_platform_login(self, username, passwd):
          head = struct.Struct(">BBBB17sBH")
          body_prefix = struct.Struct(">BBBBBBH")
          body_append = struct.Struct("12s20sB")
          buff = ctypes.create_string_buffer(head.size + body_prefix.size + body_append.size + 1)
          head_fields = (0x23, 0x23, 0x01, 0xfe, self._vin, 0x05, body_prefix.size + body_append.size)
          body_prefix_fields = self.get_body_prefix_fields()
          body_append_fields = (usrname, passwd, 0x01)
          head.pack_into(buff, 0, *head_fields)
          body_prefix.pack_into(buff, head.size, *body_prefix_fields)
          body_append.pack_into(buff, head.size + body_prefix.size, *body_append_fields)
          # TODO: bcc check
          return buff.raw
        
        
      @keyword("Encode GB32960 Platform Logout")
      def gen_platform_logout(self):
          return self.get_head_and_dummy_body(0x06)
        
      @keyword("Encode GB32960 Vehicle Timing")
      def gen_vehicle_timing(self):
          return self.get_dummy_head()
        
        
      
