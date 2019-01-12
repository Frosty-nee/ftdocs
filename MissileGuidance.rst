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
   :rtype: int

.. py:function:: GetLuaControlledMissileInfo(luaTransceiverIndex, missileIndex)
   
   returns a MissileWarningInfo structure for your missile. you can tell where it is and how fast it is going from this

   :param int luaTransceiverIndex: 0 is the first one
   :param int missileIndex: 0 is the first one
   :return: a MissileWarningInfo object for your missile
   :rtype: MissileWarningInfo

.. py:function:: SetLuaControlledMissileAimPoint(luaTransceiverInde, missileIndex, x, y, z)

   Sets the aim point. No guidance modules will help achieve this aim point so do your own predictive guidance. Needs a lua receiver component ON the missile to work

   :param int luaTransceiverIndex: 0 is the first one
   :param int missileIndex: 0 is the first one
   :param float x,y,z: global coordinates of the aim point
   :return:

.. py:function:: DetonateLuaControlledMissile(luaTranscieverIndex, missileIndex)

   Explodes the missile, needs a lua receiver component ON the missile to work

   :param int luaTransceiverIndex: 0 is the first one
   :param int missileIndex: 0 is the first one
   :return:

.. py:function:: IsLuaControlledMissileAnInterceptor(LuaTransceiverIndex, missileIndex)

   Find out if the missile has an interceptor capability.

   :param int luaTransceiverIndex: 0 is the first one
   :param int missileIndex: 0 is the first one
   :return: true means that the missile has an interceptor module, otherwise false is returned. If the missile has no lua receiver false will be returned.

.. py:function:: SetLuaControlledMissileInterceptorTarget(LuaTransceiverIndex, missileIndex, mainframeIndex, targetIndex)

   Set the target of an interceptor missile to be a specific missile for which a warning exists. This is enough to get the interceptor missile to behave normally but if you actually want to guide it yourself use SetLuaControlledMissileInterCeptorStandardGuidanceOnOff to turn the guidance off.

   :param int luaTransceiverIndex: 0 is the first one
   :param int missileIndex: 0 is the first one
   :param int mainframeIndex: 0 is the first one
   :param int targetIndex: 0 is the first missile for which that mainframe has a warning for

.. py:function:: SetLuaControlledMissileInterCeptorStandardGuidanceOnOff(luaTransceiver, missileIndex, onOff)

   turns standard guidance for the missile on and off. Turn it off if you're going to guide the missile in yourself.

   :param int luaTransceiverIndex: 0 is the first one
   :param int missileIndex: 0 is the first one
   :param bool onOff: True will use standard missile guidance to aim at the interceptor's target, false will rely on SetLuaControlledMissileAimPoint for aiming coordinates.
   :return:

