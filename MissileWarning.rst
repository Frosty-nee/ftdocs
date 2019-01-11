Missle Warning
==============

.. py:function:: GetNumberOfWarnings()

   returns the number of warnings

   :param:
   :return: the number of warnings
   :rtype: int

.. py:function:: GetMissileWarning(mainframeIndex, missileIndex)

   Request information on a specific missile warning

   :param int mainframeIndex: the index of the mainframe
   :param int missileIndex: the index of the missile
   :return: information on the missile. missileWarningInfo.valid = false if you didn't request an existing missile index (or mainframe)
   :rtype: MissileWarningInfo
