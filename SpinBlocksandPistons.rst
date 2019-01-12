Spin Blocks and Pistons
============================

.. py:function:: SetSpinBlockSpeedFactor(SubConstructIdentifier, speedFactor)

   Set the speed factor. In continuous mode spinners this allows some blades to spin slower than others, in insta-spin blades this is related to the speed they are spinning at (1 is max speed, 0 is no speed), and in rotation spinners this does nothing
   :param int SubConstructIdentifier: the persistent identifier of the subconstruct
   :param float speedFactor: 0 to 1, the fractional power output
   :return:

.. py:function:: SetSpinBlockPowerDrive(SubConstructIdentifier, drive)

   Sets the power drive. This allows heliblades to produce more force. Requires engine power. 0 removes engine use. 10 is maximum power use

   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :param float drive: the relative power use of the spinner (0 to 10)
   :return:

.. py:function:: SetSpinBlockRotationAngle(SubConstructIdentifier, angle)

   sets the angle of rotation. Changes the spinner into Rotate mode. 'RotateBackwards' is not available through this interface but you shouldn't need it.

   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :param float angle: the angle in degrees to turn to
   :return:

.. py:function:: SetSinBlockInstaSpin(SubConstructIdentifier, magnitudeAndDirection)

   Spins the blades in a direction and speed determined by magnitudeAndDirection. Will set the spinner into  instaspin forwards mode and will affect speed factor variable of the spinner

   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :param float magnitudeAndDirection: -1 means spin backwards full speed, 1 is spin forwards full speed
   :return:

.. py:function:: GetPistonExtension(SubConstructIdentifier)

   Gets the extenion of the piston, -1 if not found
      
   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :return: the extension distance of the piston in meters
   :rtype: float

.. py:function:: GetPistonVelocity(SubConstructIdentifier)

   get the velocity of the piston (always positive), -1 if not found

   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :return: the velocity of the piston in meters per second
   :rtype: float

.. py:function:: SetPistonExtension(SubConstructIdentifier, ExtensionDistance)

   Set the extension of the piston

   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :param float ExtensionDistance: the extension distance of the piston in meters. Will be clamped if necessary.
   :return:

.. py:function:: SetPistonVelocity(SubConstructIdentifier, ExtensionVelocity)

   Set the velocity of the piston.

   :param int SubConstructIdentifier: the persistent identifier of the SubConstruct
   :param float ExtensionVelocity: the velocity of the piston in meters per second (between 0.1 and 2)
   :return:

.. py:function:: GetDedibladeCount()

   returns the number of dedicated helicopter spinners

   :param:
   :return: the number of dedicated helicopter spinners
   :rtype: int

.. py:function:: GetDedibladeInfo(DedibladeIndex)

   returns block info for the dedicated helicopter spinner

   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner
   :return: a block info object for the dedicated helicopter spinner
   :rtype: BlockInfo

.. py:function:: IsDedibladeOnHull(DedibladeIndex)

   returns whether the dedicated helicopter spinner is on the hull or on a SubConstruct

   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner
   :return: true if on hull
   :rtype: bool

.. py:function:: SetDedibladeSpeedFactor(DedibladeIndex, speedFactor)
   
   Set the speed factor, in continuous mode spinners this allows some blades to spin slower than others, in insta-spin blades this is related to the speed they are spinning at (1 is max speed 0 is no speed) and in rotation spinners this does nothing
   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner
   :param float speedFactor: 0 to 1, the fractional power output
   :return:

.. py:function:: SetDedibladePowerDrive(DedibladeIndex, drive)
   
   sets the power drive. This allows heliblades to produce more force. requires engine power. 0 removes engine use. 10 is maximum power use.

   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner.
   :param float drive: the relative power use of the dedicated helicopter spinner (0 to 10).
   :return: 

.. py:function:: SetDedibladeContinuousSpeed(DedibladeIndex, speed)

   Sets the speed of rotation. Changed the dedicated helicopter spinner into continuous mode. 'ContinuousReverse' mode is not available through this interface so set the speed negative to facilitate reverse spinning

   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner
   :param float speed: speed to rotate at. 30 is the maximum so values from -30 to 30 work
   :return:

.. py:function:: SetDedibladeInstaSpin(DedibladeIndex, magnitudeAndDirection)

   spins the blades in a direction and speed determined by magnitudeAndDirection. Will set the dedicated helicopter spinner into instaspin forwards mode and will affect speed factor variable of the spinner.

   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner
   :param float magnitudeAndDirection: -1 means spin backwards full speed, 1 is spin forwards full speed
   :return:

.. py:function:: SetDedibladeUpFraction(DedibladeIndex, upFraction)

   sets the fraction of the force that will be applied directly upwards, regardless of blade orientation.

   :param int DedibladeIndex: 0 is the first dedicated helicopter spinner
   :param float upFraction: 0 to 1
   :return:



