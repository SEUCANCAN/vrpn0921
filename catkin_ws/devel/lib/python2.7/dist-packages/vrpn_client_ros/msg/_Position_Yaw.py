# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vrpn_client_ros/Position_Yaw.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Position_Yaw(genpy.Message):
  _md5sum = "d6985a552da7cb642a5610ccf637ea1f"
  _type = "vrpn_client_ros/Position_Yaw"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 Position_x
float32 Position_y
float32 Yaw
float32 Speed_v_ms


"""
  __slots__ = ['Position_x','Position_y','Yaw','Speed_v_ms']
  _slot_types = ['float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Position_x,Position_y,Yaw,Speed_v_ms

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Position_Yaw, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Position_x is None:
        self.Position_x = 0.
      if self.Position_y is None:
        self.Position_y = 0.
      if self.Yaw is None:
        self.Yaw = 0.
      if self.Speed_v_ms is None:
        self.Speed_v_ms = 0.
    else:
      self.Position_x = 0.
      self.Position_y = 0.
      self.Yaw = 0.
      self.Speed_v_ms = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4f().pack(_x.Position_x, _x.Position_y, _x.Yaw, _x.Speed_v_ms))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.Position_x, _x.Position_y, _x.Yaw, _x.Speed_v_ms,) = _get_struct_4f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4f().pack(_x.Position_x, _x.Position_y, _x.Yaw, _x.Speed_v_ms))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.Position_x, _x.Position_y, _x.Yaw, _x.Speed_v_ms,) = _get_struct_4f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
