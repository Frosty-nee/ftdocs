Missile Guidance
===============

.. py:function:: GetLuaTranscieverCount()

   Return the number of LuaTranscievers. Each transciever can have a number of missiles which are controllable

   :param: None
   :return: the number of LuaTranscievers
   :rtype: int

.. py:function:: GetLuaControlledMissileCount(luaTranscieverIndex)
      
   Returns the number of missiles which that LuaTransciever has communications link to

   :param int luaTranscieverIndex: the index of the LuaTransciever where 0 is the first one
   :return: the number of missiles associated with the specified lua transciever
   :rtype; int

.. py:function:: GetLuaControlledMissileInfo(luaTransceiverInfo)
   
