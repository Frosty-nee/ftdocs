Target Info
===========

.. py:function:: GetNumberOfMainframes()
   
   The mainframe count of your vehicle is useful for requesting targets

   :param:
   :return: The number of mainframes on your vehicle
   :rtype: int

.. py:function:: GetNumberOfTargets(mainframeIndex)
   
   The target count is important when calling GetTarget(mainframeIndex, targetIndex).

   :param int mainframeIndex: 0 being the first mainframe. Use GetNumberOfMainframes() to find out how many there are
   :return: The number of targets in this particular mainframe. Returns0 if such a mainframe does not exist.
   :rtype: int

.. py:function:: GetTargetInfo(mainframeIndex, targetIndex)

   The TargetInfo object contains many interesting variables relating to the target. Valid will be false if the target has died but the AI has not cleared it yet.

   :param int mainframeIndex: 0 being the first mainframe. Use GetNumberOfMainframes() to find out how many there are.
   :param int targetIndex: 0 being the first target. If target prioritization card is in use, 0 is the highest priority target.
   :return: A TargetInfo object
   :rtype: TargetInfo

.. py:function:: GetTargetPositionInfo(mainframeIndex, targetIndex)

   The TargetPositionInfo object contains many interesting variables relating to the target. Valid will be false if the target has died but the AI has not cleared it yet.

   :param int mainframeIndex: 0 being the first mainframe. Use GetNumberOfMainframes() to find out how many there are.
   :param int targetIndex: 0 being the first target. If target prioritization card is in use, 0 is the highest priority target.
   :return: A TargetPositionInfo object
   :rtype: TargetPositionInfo

.. py:function:: GetTargetPositionInfoForPosition(mainframeIndex, targetIndex)

   The TargetPositionInfo object contains many interesting variables relating to the target

   :param int mainframeIndex: 0 being the first mainframe. Use GetNumberOfMainframes() to find out how many there are.
   :param float x: east west in meters
   :param float y: up down in meters (0 is sea level)
   :param float z: north south in meters
   :return: A TargetPositionInfo object for this point in space, velocity will be 0
   :rtype: TargetPositionInfo

