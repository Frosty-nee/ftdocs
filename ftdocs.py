#! python3

import sys

groups = {
        'Propulsion': [
            'TellAiThatWeAreTakingControl',
            'RequestControl',
            'RequestThrustControl',
            'RequestWaterForwards',
            'RequestComplexControllerStimulus',
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
            ],

        }

if __name__ == '__main__': 
    if len(sys.argv) > 1:
        arg = ' '.join(sys.argv[1:])
        if arg in groups:
            for command in groups[arg]:
                print(command)
        elif arg in commands:
            print(commands[arg])
        
        else: print('command or command group not found')
    else:
        print("command groups:")
        for line in groups.keys():
            print(line)
