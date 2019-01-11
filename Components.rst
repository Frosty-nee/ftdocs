Components
==========

.. py:function:: Component_GetCount(type)

   returns the number of compoents of this type

   :param int type: the type of component you want the count of
   :return: the number of components of this type
   :rtype: int

.. py:function:: Component_GetLocalPosition(type, index)

   returns the local position in the vehicle of this component

   :param int type: the type of component you want the local position of
   :param int index: the index of the component you want 
   :return: a vector3i is a Vector3 where x, y, and z are integers
   :rtype: Vector3i

.. py:function:: Component_GetBlockInfo(type, index)

   returns an extensive BlockInfo structure relating to the component

   :param int type: the type of component you want information on
   :param int index: the index of the component you want information on
   :return: a BlockInfo structure relating to the component
   :rtype: BlockInfo

.. py:function:: Component_GetBoolLogic(type, blockIndex)
   
   returns a boolean (true/false) for a component. Depending on the type of this component this means different things (or nothing at all). Default return is false

   :param int type: The type of component you want boolean logic for
   :param int blockIndex: The index of the component you want boolean logic for
   :return: the first boolean logic for this component. For a complnent without boolean logic or a block index that doesn't exist, false is returned.
   :rtype: bool

.. py:function:: Component_GetBoolLogic_1(type, blockIndex, propertyIndex)

   returns a boolean (true/false) for a component. Depending on the type of this component this means different things (or nothing at all). Default return is false

   :param int type: the type of component you want boolean logic for
   :param int blockIndex: the index of the component you want boolean logic for
   :param int propertyIndex: the index of the index of the boolean logic you want
   :return: the specified boolean logic for this component. for a component without boolean logic, or an index that doesn't exist, false is returned.
   :rtype: bool

.. py:function:: Component_SetBoolLogic(type, index, bool)

   sets the first boolean logic for a component, depending on the type of this component this means different things (or nothing at all)

   :param int type: the type of component you want to set boolean logic for
   :param int index: the index of the component you want to set boolean logic for
   :param bool bool: the True/False you want to set

.. py:function:: Component_SetBoolLogic_[1,2,3](type, blockIndex, propertyIndex1, bool1[, propertyIndex2, bool2[, propertyIndex3, bool3]])

   sets the specified boolean logics for a component, depending on the type of this component this means different things (or nothing at all). This is three separate functions numbered 1-3 which take the corresponding number of propertyIndex and bool arguments, condensed for readability's sake.

   :param int type: the type of component you want to set boolean logic for
   :param int blockIndex: the index of the component you want to set boolean logic for
   :param int propertyIndex[1-3]: The index of the property you want to set to the corresponding value
   :param bool bool[1-3]: the True/False you want to set
   :return: 


.. py:function:: Component_GetFloatLogic(type, index)

   returns a floating point value for a component. Depending on the type of component this means different things (or nothing at all). Default return is 0

   :param int type: the type of component you want float logic for
   :param int index: the index of the component you want float logic for
   :return: the first float logic for this component. for a component without float logic or a block index that doesn't exist, 0 is returned.
   :rtype: float

.. py:function:: Component_GetFloatLogic_1(type, blockIndex, propertyIndex)

   returns a floating point value for a component. Depending on the type of this component this means different things ( or nothing at all). Default return is 0

   :param int type: the type of component you want float logic for
   :param int blockIndex: the index of the component you want float logic for
   :param int propertyIndex: the index of the index of the float logic you want.
   :return: the specified float logic for this component. For a component without float logic or an index that doesn't exist, 0 is returned.
   :rtype: float

.. py:function:: Component_SetFloatLogic(type, index, float)

   sets the first float logic for a component. Depending on the type of this component this means differet things (or nothing at all)

   :param int type: the type of component you want to set float logic for
   :param int index: the index of the component you want to set float logic for
   :param float float: the floating point value you want to set
   :return:

.. py:function:: Component_SetFloatLogic_[1,2,3](type, blockIndex, propertyIndex1, float1[, propertyIndex2, float2[, propertyIndex3, float3]])

   sets the specified float logics for a component. depending on the type of this component this means different things or nothing at all. This is three separate functions number 1-3 which take the corresponding number of propertyIndex and float arguments, condensed for readability's sake.

   :param int type: the type of component you want to set float logic for.
   :param int blockIndex: the index of the component you want to set float logic for
   :param int propertyIndex[1-3]: the index of the property you want to set to the corresponding value
   :param float float[1-3]: the floating point value you want to set.
   :return:

.. py:function:: Component_GetIntLogic(type, blockIndex)

   returns an int for a component, depending on the type of this componenet this means different things (or nothing at all). Default return is 0

   :param int type: the type of component you want int logic for
   :param int index: the index of the component you want int logic for
   :return: the first int logic for this component. for a component without int logic or a block index that doesn't exist, 0 is returned.
   :rtype: int

.. py:function:: Component_GetIntLogic_1(type, blockIndex, propertyIndex)

   returns an integer number for a component. depending on the type of this component this means different things (or nothing at all) . Default return is 0

   :param int type: the type of component you want int logic for.
   :param int blockIndex: the index of the component you want int logic for
   :param int propertyIndex: the index of the index of the int logic you want
   :return: the specified int logic for this component, for a component without int logic or an index that doesn't exist, 0 is returned.
   :rtype: int

.. py:function:: Component_SetIntLogic(type, blockIndex, int)

   sets the first int logic for a component. depending on the type of this component this means different things (or nothing at all)
   :param int type: the type of component you want to set int logic for
   :param int blockIndex: the index of the component you want to set int logic for
   :param int int: the integer you want to set
   :return:

.. py:function:: Component_SetIntLogic_[1,2,3](type, blockIndex, propertyIndex1, int1[, propertyIndex2, int2[,propertyIndex3, int3]])

   sets the specified int logics for a component. Depending on the type of this component this means different things, (or nothing at all).

   :param int type: the type of component you want to set int logic for
   :param int blockIndex: the index of the component you want to set int logic for
   :param propertyIndex: the index of the int logic you want to set
   :param int int: the int that you want to set
   :return:

.. py:function:: Component_SetBoolLogicAll(type, bool)

   sets the first boolean logic for all components of a specific type. Depending on the type of component this means different things (or nothing at all).
   
   :param int type: the type of component you want to set boolean logic for
   :param bool bool: boolean you want to set

.. py:function:: Component_SetBoolLogicAll_[1,2,3](type, propertyIndex1, bool1[, propertyIndex2, bool2[, propertyIndex3, bool3]])

   sets the specified boolean logics for all components of a specific type, depending on the type of this component this means different things (or nothing at all)   

   :param int type: the type of component that you want to set boolean logic for
   :param int propertyIndex: the index of the boolean logic you want to set
   :param bool bool: the bool you want to set.

.. py:function:: Component_SetFloatLogicAll(type, float)

   sets the first float logic for all components of a specific type. Depending on the type of component this means different things (or nothing at all).

   :param int type: the type of componenet you want to set floating point logic for
   :param float float: the floating point number you want to set
   :return:

.. py:function:: Component_SetFloatLogicAll_[1,2,3](type, propertyIndex1, float1[, propertyIndex2, float2[, propertyIndex3, float3]])

   Sets the specified floating point logics for all components of a specific type. Depending on the type of this component this means different things (or nothing at all)

   :param int type: the type of component you want to set float logic for
   :param int propertyIndex: the index of the float you want to set
   :param float float: the float you want to set.
   :return:

.. py:function:: Component_SetIntLogicAll(type, int)

   sets the first integer logic for all components of a specific type. Depending on the type of this component this means different things ( or nothing at all)
   
   :param int type: the type of component you want to set integer logic for
   :param int int: the integer you want to set

.. py:function:: Component_SetIntLogicAll_[1,2,3](type, propertyIndex1, int1[, propertyIndex2, int2[, propertyIndex3, int3]])

   sets the specified integer logics for all components of the specified type.

   :param int type: the type of component you want to set ingeger logic for
   :param int propertyIndex: the index of the integer logic you want to set
   :param int int: the int you want to set
   :return:

.. py:function:: SetHologramProjectorURL(index, url)

   sets the url of the specified hologram projector

   :param int index: the index of the hologram projector
   :param string url: the url to set the hologram projector to
   :return:

.. py:function:: SetPosterHolderURL(index, url)

   Sets the url of the specified poster holder

   :param int index: the index of the poster holder
   :param string url: the url to set the poster holder to
   :return:

