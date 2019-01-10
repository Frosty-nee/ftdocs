Misc
====

.. py:function:: GetTerrainAltitudeForPosition(x,y,z)

   returns altitude of the terrain at a position in the world, can be overloaded with a single Vector3 rather than X, Y, Z components

   :param float x: Game world east west position in meters
   :param float y: Game world vertical (not important)
   :param float z: Game world north south position in meters
   :return: the terrain altitude in meters where 0 is sea level
   :rtype: float

.. py:function:: GetGravityforAltitude(alt)

   Returns gravity vector for an altitude. gravity.y is the component of interest

   :param float alt: altitude (0 is sea level)
   :return: gravity vector
   :rtype: Vector3

.. py:function:: GetTime()
   
   returns the time with an arbitrary offset (ie, the time will seldom be 0)

   :param:
   :return: the time in seconds
   :rtype: float

.. py:function:: GetTimeSinceSpawn()
   
   Returns time since construct spawned in seconds

   :param:
   :return: the time in seconds
   :rtype: float

.. py:function:: GetGameTime()

   returns the time since the instance started in seconds

   :param:
   :return: the time since the instance started in seconds
   :rtype: float

.. py:function:: GetWindDirectionAndMagnitude()

   Get the direction and magnitude of the wind

   :param:
   :return: Vector representing the direction and magnitude of the wind
   :rtype: Vector3
