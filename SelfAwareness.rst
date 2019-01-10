Self Awareness
==============

.. py:function:: GetConstructPosition()

   Returns the position of the construct, the construct's position is essentially the position of the first ever block placed, or the centre of the starting raft it was built from.

   :param:
   :return: The position (Vector3 has members x, y, and z)
   :rtype: Vector3

.. py:function:: GetConstructForwardVector()

   Return the forward pointing vector of the construct

   :param:
   :return: the forward pointing vector of the construct (it has length 1)
   :rtype: Vector3

.. py:function:: GetConstructUpVector()

   returns the up pointing vector of the construct

   :param:
   :return: the up pointing vector of the construct (it has length1)
   :rtype: Vector3

.. py:function:: GetConstructMaxDimensions()

   returns the 'positive' size of the vehicle (right up forwards) relative to it's origin (GetConstructPosition()). The coordinates are in local space. This minus GetConstructMinDimensions provides the full size of the vehicle

   :param:
   :return: the size of the vehicle right, up, forwards of its origin
   :rtype: Vector3

.. py:function:: GetConstructMinDimensions()

   Returns the negative size of the vehicle (left, down, back) relative to its origin (GetConstructPosition()). The coordinates are in local space.

   :param:
   :return: the size of the vehicle left, down, and back of its origin
   :rtype: Vector3

.. py:function:: GetConstructRoll()
   
   Return the roll angle in degrees

   :param:
   :return: the roll angle in degrees
   :rtype: float

.. py:function:: GetConstructPitch()

   Return the pitch angle in degrees

   :param:
   :return: the pitch angle in degrees
   :rtype: float

.. py:function:: GetConstructYaw()

   Return the yaw angle in degrees

   :param:
   :return: the yaw angle in degrees
   :rtype: float

.. py:function:: GetConstructCenterOfMass():

   returns the position of the Construct's center of mass in the world

   :param:
   :return: The position (Vector3 has members x, y, z)
   :rtype: Vector3

.. py:function:: GetAiPosition(mainframeIndex)

   Returns the position of the mainframe in the world. Returns Vector3(0,0,0) if no such mainframe exists.

   :param int mainframeIndex: 0 is the first mainframe
   :return: The position (Vector3 has members x, y, z)
   :rtype: Vector3

.. py:function:: GetVelocityMagnitude()

   Returns the magnitude of your velocity in meters per second

   :param:
   :return: magnitude of your velocity in meters per second
   :rtype: float

.. py:function:: GetForwardsVelocityMagnitude()

   Returns the magnitude of your velocity in the forward direction in meters per second. A negative value means you're going predominantly backwards.

   :param:
   :return: magnitude of your forwards velocity in meters per second
   :rtype: float

.. py:function:: GetVelocityVector()
   
   Returns your construct's velocity vector in world space in meters per second. x is east/west, y is up/down, z is north/south.

   :param:
   :return: your construct's velocity vector in meters per second
   :rtype: Vector3

.. py:function:: GetVelocityVectorNormalized()

   returns your construct's velocity vector in world space in meters per second, x is east/west, y is up/down, z is north/south. It's normalized to have a length of 1

   :param:
   :return: your construct's velocity vector in meters per second. normalized to have a length of 1
   :rtype: Vector3

.. py:function:: GetAngularVelocity()

   returns your angular velocity, x is speed of turn around the east->west axis, y is around the verticle, and z is around the north south axis. You're probably going to want the next function instead of this one.

   :param:
   :return: Your construct's angular velocity in world space
   :rtype: Vector3

.. py:function:: GetLocalAngularVelocity()

   returns your angular velocity. x is pitch, y is yaw, z is roll

   :param:
   :return: your construct's angular velocity in local space
   :rtype: Vector3

.. py:function:: GetAmmoFraction()

   returns the fraction of ammo that your construct has left

   :param:
   :return: fraction. 0 to 1. 1 if no ammo storage is available
   :rtype: float

.. py:function:: GetFuelFraction()

   returns the fraction of fuel your construct has left

   :param:
   :return: fraction. 0 to 1. 1 if no fuel storage is available
   :rtype: float

.. py:function:: GetSparesFraction()

   returns the fraction of spares your construct has left

   :param:
   :return: fraction. 0 to 1. 1 if no spares storage is available
   :rtype: float

.. py:function:: GetEnergyFraction()

   Returns the fraction of energy your construct has left

   :param:
   :return: fraction. 0 to 1. 1 if no batteries are available
   :rtype: float

.. py:function:: GetHealthFraction()

   returns the fraction of health your construct has (including turrets etc)

   :param:
   :return: fraction. 0 to 1. 1 if full health
   :rtype: float

.. py:function:: IsDocked()

   returns true if the vehicle is docked

   :param:
   :return: Docked? true for yes
   :rtype: bool

.. py:function:: GetHealthFractionDifference(time)

   Returns health difference over specified measurement time

   :param float time: the time you want the difference measured over. Time will be limited to be between 1 and 30.
   :return: health difference as a fraction (0 to 1)
   :rtype: float

.. py:function:: GetBlueprintName()

   returns the name of this blueprint

   :param:
   :return: name of the blueprint
   :rtype:

.. py:function:: GetUniqueId()

   returns the unique Id of the construct. No other construct has the same id

   :param:
   :return: the unique Id
   :rtype: int
