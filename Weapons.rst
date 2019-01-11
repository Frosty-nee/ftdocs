Weapons
======

.. py:function:: GetWeaponCount()

   gets the number of weapons on the hull. Knowing this number is useful for when you call GetWeaponInfo(i) to find out weapon information

   :param:
   :return: the number of weapons on the hull. 

.. py:function:: GetWeaponInfo(weaponIndex)

   gets weapon information for a specific weapon

   :param int weaponIndex: the index of the weapon you want information on. 0 is the first weapon
   :return: information on the weapon
   :rtype: WeaponInfo

.. py:function:: GetWeaponConstraints(weaponIndex)

   Gets field-of-fire constraints for a specific weapon

   :param int weaponIndex: the index of the weapon you want the constraints of, 0 is the first weapon
   :return: information on the field-of-fire constraints of the weapon
   :rtype: WeaponConstraints

.. py:function:: GetWeaponBlockInfo(weaponIndex)

   Gets the block information for a specific weapon

   :param int weaponIndex: the index of the weapon you want information on. 0 is the first weapon
   :return: the block information of the main component of the weapon. See 'Components' for information on BlockInfo
   :rtype: BlockInfo

.. py:function:: AimWeaponInDirection(weaponIndex, x, y, z, weaponSlot)

   Aims a weapon in a specific direction. For a turret this will aim all weapons on the turret as well as the turret itself.

   :param int weaponIndex: 0 is the first weapon
   :param float x,y,z: the world coordinate scheme direction components to point in. They don't need to be normalized.
   :param int weaponSlot: 0 for all, otherwise 1-5
   :return: the number of weapons that can fire in this direction. 0 for none
   :rtype: int

.. py:function:: FireWeapon(weaponIndex, weaponSlot)

   Fires a specific weapon. IT's important for most weapons that you aim them first as they won't fire if they can't fire in the direction they aimed.

   :param int weaponIndex: 0 is the first weapon
   :param int weaponSlot: 0 will control all weapons
   :return: has any weapon fired? will be true if so.
   :rtype: bool

.. py:function:: GetWeaponCountOnSubConstruct(SubConstructIdentifier)
   
   return the number of weapons on the turret or spinner. If you wanted to control the turret itself then note that it is treated as a hull-mounted weapon

   :param int SubConstructIdentifier: this identifier never changes in the blueprint, use the subconstructs-related functions to get it
   :return: the number of weapons on this turret 
   :rtype: int

.. py:function:: GetWeaponInfoOnSubConstruct(SubConstructIdentifier, weaponIndex)
   
   Get weapon info of a weapon on a turret or spinner

   :param int SubConstructIdentifier: This identifier never changes in the blueprint, use the SubConstructs related functions to get it.
   :param int weaponIndex: the index of the weapon, 0 is the first one
   :return: a WeaponInfo object, see above for the definition of this structure. Note that changes to thsi structure in LUA do not affect the weapon itself.
   :rtype: WeaponInfo

.. py:function:: GetWeaponConstraintsOnSubConstruct(SubConstructIdentifier, weaponIndex)

   gets field-of-fire information for a specific weapon

   :param int SubConstructIdentifier: This identifier never changes in the blueprint, use the SubConstructs-related functions to get it
   :param int weaponIndex: the index of the weapon, 0 is the first one
   :return: information on the field-of-fire constraints of the weapon
   :rtype: WeaponConstraints

.. py:function:: GetWeaponBlockInfoOnSubConstruct(SubConstructIdentifier, weaponIndex)

   Gets the block information of a specific weapon

   :param int SubConstructIdentifier: This identifier never changes in the blueprint, use the SubConstructs-related functions to get it 
   :param in weaponIndex: the index of the weapon, 0 is the first one
   :return: the block information of the main component of the weapon. See Components for more information on BlockInfo
   :rtype: BlockInfo

.. py:function:: AimWeaponInDirectionOnSubConstruct(SubConstructIdentifier, weaponIndex, x,y,z, weaponSlot)

   Aims a specific weapon on the turret without aiming the turret

   :param int SubConstructIdentifier: the subconstruct identifier
   :param int weaponIndex: 0 is the first weapon
   :param float x,y,z: the world coordinate scheme direction components to point in. they don't need to be normalized
   :param in weaponSlot: 0 for all, otherwise 1-5
   :return: the number of weapons that can fire in this direction, 0 for none
   :rtype: int

.. py:function:: FireWeaponOnSubConstruct(SubConstructIdentifier, weaponIndex, weaponSlot)

   Fires a specific weapon. It's important for most weapons that you aim them first as they won't fire if they can't fire in the direction they are aimed

   :param int SubConstructIdentifier: the identifier of the subconstruct
   :param int weaponIndex: 0 is the first weapon
   :param int weaponSlot: 0 will control all weapons
   :return: has any weapon fired? will be true if so.
   :rtype: bool

