#! python3

import sys

groups = {
    'Fleet Awareness': [
        'FleetIndex',
        'Fleet',
        'IsFlagship',
        ],
    'Resources': [
        'ResourceZones', 
        'Resources', 
        ],
    'AI': [
        'AIMode',
        'ConstructType',
        ],
    
    'Propulsion': [
        'TellAiThatWeAreTakingControl',
        'RequestControl',
        'RequestThrustControl',
        'RequestWaterForwards',
        'RequestComplexControllerStimulus',
        'GetDrive',
        'GetInput',
        'MoveFortress',
        ],
    'Target Info': [
        'GetNumberOfMainframes',
        'GetNumberOfTargets',
        'GetTargetInfo',
        'GetTargetPositionInfo',
        'GetTargetPositionInfoForPosition',
        ],
    'Misc': [
        'GetTerrainAltitudeForPosition',
        'GetTerrainAltitudeForLocalPosition',
        'GetGravityForAltitude',
        'GetTime',
        'GetTimeSinceSpawn',
        'GetGameTime',
        'GetWindDirectionAndMagnitude',
        ],
    'Self Awareness': [
        'GetConstructPosition',
        'GetConstructForwardVector',
        'GetConstructRightVector',
        'GetConstructUpVector',
        'GetConstructMaxDimensions',
        'GetConstructMinDimensions',
        'GetConstructRoll',
        'GetConstructPitch',
        'GetConstructYaw',
        'GetConstructCenterOfMass',
        'GetAiPosition',
        'GetVelocityMagnitude',
        'GetForwardsVelocityMagnitude',
        'GetVelocityVector',
        'GetVelocityVectorNormalized',
        'GetAngularVelocity',
        'GetLocalAngularVelocity',
        'GetAmmoFraction',
        'GetFuelFraction',
        'GetSparesFraction',
        'GetEnergyFraction',
        'GetHealthFraction',
        'IsDocked',
        'GeatHealthFractionDifference',
        'GetBlueprintName',
        'GetUniqueId',
        ],
    'Components': [
        'Component_GetCount',
        'Component_GetLocalPosition',
        'Component_GetBlockInfo',
        'Component_GetBoolLogic',
        'Component_SetBoolLogic',
        'Component_GetFloatLogic',
        'Component_SetFloatLogic',
        'Component_GetIntLogic',
        'Component_SetIntLogic',
        'Component_SetBoolLogicAll',
        'Component_SetFloatLogicAll',
        'Component_SetIntLogicAll',
        ],
    'Weapon': [
        'GetWeaponCount',
        'GetWeaponInfo',
        'GetWeaponConstraints',
        'GetWeaponBlockInfo',
        'AimWeaponInDirection',
        'FireWeapon',
        'GetTurretSpinnerCount',
        'GetWeaponCountOnTurretOrSpinner',
        'GetWeaponInfoOnTurretOrSpinner',
        'AimWeaponInDirectionOnTurretOrSpinner',
        'FireWeaponOnTurretOrSpinner',
        'GetWeaponCountOnSubConstruct',
        'GetWeaponInfoOnSubConstruct',
        'GetWeaponConstraintsOnSubConstruct',
        'GetWeaponBlockInfoOnSubConstruct',
        'AimWeaponInDirectionOnSubConstruct',
        'FireWeaponOnSubConstruct',
        ],
    'Missile Warning': [
        'GetNumberOfWarnings',
        'GetMissileWarning',
        ],
    'Missile Guidance': [
        'GetLuaTransceiverCount',
        'GetLuaControlledMissileCount',
        'GetLuaTransceiverInfo',
        'GetLuaControlledMissileInfo',
        'SetLuaControlledMissileAimPoint',
        'DetonateLuaControlledMissile',
        'IsLuaControlledMissileAnInterceptor',
        'SetLuaControlledMissileInterceptorTarget',
        'SetLuaControlledMissileInterceptorStandardGuidanceOnOff',
        ],
    'Spin Blocks': [
        'SetSpinBlockSpeedFactor',
        'SetSpinBlockPowerDrive',
        'SetSpinBlockRotationAngle',
        'SetSpinBlockContinuousSpeed',
        'SetSpinBlockInstaSpin',
        'GetPistonExtension',
        'GetPistonVelocity',
        'SetPistonExtension',
        'SetPistonVelocity',
        'GetDedibladeCount',
        'GetDedibladeInfo',
        'IsDedibladeOnHull',
        'SetDedibladeSpeedFactor',
        'SetDedibladePowerDrive',
        'SetDedibladeContinuousSpeed',
        'SetDedibladeInstaSpin',
        'SetDedibladeUpFraction',
        'GetSpinnerCount',
        'GetSpinnerInfo',
        'SetSpinnerSpeedFactor',
        'SetSpinnerPowerDrive',
        'SetSpinnerRotationAngle',
        'SetSpinnerContinuousSpeed',
        'SetSpinnerInstaSpin',
        'IsSpinnerDedicatedHelispinner',
        'IsSpinnerOnHull',
        'SetDedicatedHelispinnerUpFraction',
        ],
    'SubConstructs': [
        'GetAllSubConstructs',
        'GetAsllSubConstructChildren',
        'GetParent',
        'IsTurret',
        'IsSpinBlock',
        'IsPiston',
        'IsAlive',
        'IsSubConstructOnHull',
        'GetSubConstructInfo',
        'GetSubConstructIdleRotation',
        ],
    'Friendlies': [
        'GetFriendlyCount',
        'GetFriendlyInfo',
        'GetFriendlyInfoById',
        ],
}