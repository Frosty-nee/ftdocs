Propulsion
==========
.. py:function:: TellAiThatWeAreTakingControl()
   
   Will stop the Ai from issuing propulsion commands for the next second, after which it will assume control. This is exactly what happens when the player presses a control key on an AI controlled vehicle.

   :param:
   :return: 

.. py:function:: RequestControl(mode, type, drive)

   A generic propulsion / turning request. RequestControl(0,8,1) does the same as RequestWaterForward(1)

   :param int mode: Water=0, Land=1, Air=2
   :param int type: YawLeft=0, YawRight=1, RollLeft=2, RollRight=3, NoseUp=4, NoseDown=5, Increase=6, Decrease=7, MainPropulsion=8
   :param float drive: -1 to 1 for main propulsion, 0 to 1 for everything else 

.. py:function:: RequestThrustControl(type[,scale])

   Requests the vehicle's built in thrust controller to perform certain actions, exactly the same as the player using the Thrust Controller block. WARNING: this will override the drive fractions of your propulsion systems as it uses these to provide balanced torque-less thrust.

   :param int type: forwards=0, backwards=1, right=2, left=3, up=4, down=5, rollright=6, rollleft=7, yawright=8, yawleft=9, noseup=10, nosedown=11
   :param float scale: the force between 0 and 1
   :return: 

.. py:function:: RequestWaterForwards(drive)

   Requests forward propulsion for propellers and huge propellers for one time-step. Does not actually change water-drive. This is a function the Naval AI uses.

   :param float drive: a number between -5 and 5, values outside this range will be clamped

.. py:function:: RequestComplexControllerStimulus(stim)
   
   requests a stimuli as per the complex controller block

   :param int stim: none=0, T=1, G=2, Y=3, H=4, U=5, J=6, I=7, K=8, O=9, L=10, up=11, down=12, left=13, right=14
   :return:

.. py:function:: GetDrive(mode)

   get the main drive fraction for the specified mode

   :param int mode: water=0, air=1, Primary=2, Secondary=3, Tertiary=4
   :return: Drive Fraction
   :rtype: int

.. py:function:: GetInput(mode, type)

   Get the drive fraction for the specified mode and type.

   :param int mode: water=0, land=1, air=2
   :param ind type: YawLeft=0, YawRight=1, RollLeft=2, RollRight=3, NoseUp=4, NoseDown=5, Increase=6, Decrease=7, MainPropulsion=8
   :return: Drive Fraction
   :rtype: float

.. py:function:: MoveFortress(direction)

   Move fortress in any direction, limited to 1 meter

   :param Vector3 direction: direction to move the fortress in, limited to 1 meter
   :return:
