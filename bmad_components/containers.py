from happi.item import HappiItem, EntryInfo
from happi import Client
import re

class Base(HappiItem):
    S = EntryInfo('Longitudinal position at the downstream end', optional=False, enforce=float)
    S_start = EntryInfo('Longitudinal reference position at entrance end', optional=False, enforce=float)
    
class InstrumentalMeasurements(HappiItem):
    X_GAIN_ERR = EntryInfo('Horizontal gain error', optional=False, enforce=float)
    Y_GAIN_ERR = EntryInfo('V ertical gain error', optional=False, enforce=float)
    CRUNCH = EntryInfo('Crunch angle', optional=False, enforce=float)
    TILT_CALIB = EntryInfo('Tilt angle calibration', optional=False, enforce=float)
    X_OFFSET_CALIB = EntryInfo('Horizontal offset calibration', optional=False, enforce=float)
    Y_OFFSET_CALIB = EntryInfo('Vertical offset calibration', optional=False, enforce=float)
    X_GAIN_CALIB = EntryInfo('Horizontal gain calibration', optional=False, enforce=str)
    Y_GAIN_CALIB = EntryInfo('Vertical gain calibration', optional=False, enforce=float)
    CRUNCH_CALIB = EntryInfo('Crunch angle calibration', optional=False, enforce=float)
    NOISE = EntryInfo('Noise factor', optional=False, enforce=float)
    DE_ETA_MEAS = EntryInfo('Percent change in energy', optional=False, enforce=float)
    X_DISPERSION_ERR = EntryInfo('Horizontal dispersion error', optional=False, enforce=float)
    Y_DISPERSION_ERR = EntryInfo('Vertical dispersion error', optional=False, enforce=float)
    X_DISPERSION_CALIB = EntryInfo('Horizontal dispersion calibration', optional=False, enforce=float)
    Y_DISPERSION_CALIB = EntryInfo('Vertical dispersion calibration', optional=False, enforce=float)
    N_SAMPLE = EntryInfo('Number of sampling points', optional=False, enforce=float)
    OSC_AMPLITUDE = EntryInfo('Oscillation amplitude', optional=False, enforce=float)
    
    
class ApertureLimits(HappiItem):
    X1_LIMIT = EntryInfo('Horizontal, negative side, aperture limit', optional=False, enforce=float)
    X2_LIMIT = EntryInfo('Horizontal, positive side, aperture limit', optional=False, enforce=float)
    Y1_LIMIT = EntryInfo('Vertical, negative side, aperture limit', optional=False, enforce=float)
    Y2_LIMIT =  EntryInfo('Vertical, positive side, aperture limit', optional=False, enforce=float)
    
    # maybe
    APERTURE_AT = EntryInfo('What end is the aperture at', optional=False, enforce=str)
    APERTURE_TYPE = EntryInfo('What type of aperture is this', optional=False, enforce=str)


class Bend(HappiItem):
    ANGLE = EntryInfo('Design bend angle', optional=False, enforce=float)
    B_FIELD = EntryInfo('Design field strength', optional=False, enforce=float)
    DB_FIELD = EntryInfo('', optional=False, enforce=float)
    B1_GRADIENT = EntryInfo('Quadrupole field strength', optional=False, enforce=float)
    B2_GRADIENT = EntryInfo('Sextupole field strength', optional=False, enforce=float)
    E1 = EntryInfo('Entrance pole face angle', optional=False, enforce=float)
    E2 = EntryInfo('Exit pole face angle', optional=False, enforce=float)
    G = EntryInfo('Design bend strength', optional=False, enforce=float)
    DG = EntryInfo('Difference between actual and design bend strength', optional=False, enforce=float)
    #H1 = EntryInfo('Entrance face curvature', optional=False, enforce=float)
    #H2 = EntryInfo('Exit face curvature', optional=False, enforce=float)
    K1 = EntryInfo('Quadrupole strength', optional=False, enforce=float)
    K2 = EntryInfo('Sextupole strength', optional=False, enforce=float)
    L_CHORD = EntryInfo('Chord length', optional=False, enforce=float)
    L_SAGITTA = EntryInfo('Sagittal length', optional=False, enforce=float)
    RHO = EntryInfo('Design bend radius', optional=False, enforce=float)
    
    
class Kick(HappiItem):
    HKICK = EntryInfo('Integrated horizontal field kick', optional=False, enforce=float)
    VKICK = EntryInfo('Integrated vertical field kick', optional=False, enforce=float)
    BL_HKICK = EntryInfo('Integrated horizontal field kick in meters-Tesla', optional=False, enforce=float)
    BL_VKICK = EntryInfo('Integrated vertical field kick in meters-Tesla', optional=False, enforce=float)

class Length(HappiItem):
    L = EntryInfo('Length path of the reference particle', optional=False, enforce=float) # bend?

    
class StraightLineOrientation(HappiItem):
    #offsets, pitches, tilts 
    TILT = EntryInfo('Rotation of the element in the x,y plane', optional=False, enforce=float)
    X_PITCH = EntryInfo('Rotation about the element center s.t. exit face is diplaced in the corresponding x direction', optional=True, enforce=float)
    Y_PITCH = EntryInfo('Rotation about the element center s.t. exit face is diplaced in the corresponding y direction', optional=True, enforce=float)
    X_OFFSET = EntryInfo('Translation of element in the local x direction', optional=False, enforce=float)
    Y_OFFSET = EntryInfo('Translation of element in the local y direction', optional=False, enforce=float)
    Z_OFFSET = EntryInfo('Translation of element in the local z direction', optional=False, enforce=float)

    
class BendOrientation(StraightLineOrientation):
    REF_TILT = EntryInfo('Rotation of bend around the z axis', optional=False, enforce=float)
    ROLL  =EntryInfo('Vertical kick assigned to beam', optional=False, enforce=float)
    
class GirderExtension(HappiItem):
    X_PITCH_TOT = EntryInfo('Rotation about the element center s.t. exit face is diplaced in the corresponding x direction, including girder pitch', optional=False, enforce=float)
    Y_PITCH_TOT = EntryInfo('Rotation about the element center s.t. exit face is diplaced in the corresponding y direction, including girder pitch', optional=False, enforce=float)
    X_OFFSET_TOT = EntryInfo('Total translation of element in the x direction including Girder tilt', optional=False, enforce=float)
    Y_OFFSET_TOT = EntryInfo('Total translation of element in the y direction including Girder tilt', optional=False, enforce=float)
    Z_OFFSET_TOT = EntryInfo('Total translation of element in the z direction including Girder tilt', optional=False, enforce=float)
    
    
class GirderBendExtension(GirderExtension):
    TILT_TOT = EntryInfo('Rotation of bend around the z axis including Girder orientation', optional=False, enforce=float)

    
class Twiss(HappiItem):
    # Twiss elements
    Beta_A  = EntryInfo('A mode beta', optional=False, enforce=float)
    Beta_B  = EntryInfo('B mode beta', optional=False, enforce=float)
    Alpha_A = EntryInfo('A mode alpha', optional=False, enforce=float)
    Alpha_B = EntryInfo('B mode alpha', optional=False, enforce=float) 
    Gamma_A = EntryInfo('A mode gamma', optional=False, enforce=float)
    Gamma_B = EntryInfo('B mode gamma', optional=False, enforce=float)
    Phi_A = EntryInfo('A mode phase', optional=False, enforce=float)
    Phi_B = EntryInfo('B mode phase', optional=False, enforce=float)
    Eta_X = EntryInfo('x-axis dispersion', optional=False, enforce=float)
    Eta_Y = EntryInfo('y-axis dispersion', optional=False, enforce=float)
    Eta_Z = EntryInfo('z-axis dispersion', optional=False, enforce=float)
    Etap_X = EntryInfo('x-axis dispersion derivative', optional=False, enforce=float)
    Etap_Y = EntryInfo('y-axis dispersion derivative', optional=False, enforce=float)
    Etap_Z = EntryInfo('z-axis dispersion derivative', optional=False, enforce=float)
    
    
class Floor(HappiItem):
    # Global floor coords at end of element
    # reference
    Reference_X = EntryInfo('X offset from origin without misalignments',
                         optional=False, enforce=float)
    Reference_Y = EntryInfo('Y offset from origin without misalignments',
                         optional=False, enforce=float)
    Reference_Z = EntryInfo('Z offset from origin without misalignments',
                         optional=False, enforce=float)
    Reference_Theta = EntryInfo('Angle on floor without misalignments',
                         optional=False, enforce=float)
    Reference_Phi = EntryInfo('Angle of attack without misalignments',
                         optional=False, enforce=float)
    Reference_Psi = EntryInfo('Roll angle without misalignments',
                         optional=False, enforce=float)
    
    # actual
    Actual_X = EntryInfo('X offset from origin with offset/pitch/tilt misalignments',
                         optional=False, enforce=float)
    Actual_Y = EntryInfo('Y offset from origin with offset/pitch/tilt misalignments',
                         optional=False, enforce=float)
    Actual_Z = EntryInfo('Z offset from origin with offset/pitch/tilt misalignments',
                         optional=False, enforce=float)
    Actual_Theta = EntryInfo('Angle on floor with offset/pitch/tilt misalignments',
                         optional=False, enforce=float)
    Actual_Phi = EntryInfo('Angle of attack with offset/pitch/tilt misalignments',
                         optional=False, enforce=float)
    Actual_Psi = EntryInfo('Roll angle with offset/pitch/tilt misalignments',
                         optional=False, enforce=float)
    
    # delta ref
    delta_Ref_X = EntryInfo('X offset delta with respect to preceding element',
                         optional=False, enforce=float)
    delta_Ref_Y = EntryInfo('Y offset delta with respect to preceding element',
                         optional=False, enforce=float)
    delta_Ref_Z = EntryInfo('Z offset delta with respect to preceding element',
                         optional=False, enforce=float)
    delta_Ref_Theta = EntryInfo('Angle on floor delta with respect to preceding element',
                         optional=False, enforce=float)
    delta_Ref_Phi = EntryInfo('Angle of attack delta with respect to preceding element',
                         optional=False, enforce=float)
    delta_Ref_Psi = EntryInfo('Roll angle delta with respect to preceding element',
                         optional=False, enforce=float)
    
    
class Quadrupole(Base, ApertureLimits, Kick, StraightLineOrientation, Twiss, Length, Floor):
    B1_GRADIENT = EntryInfo('Field strength', optional=False, enforce=float)
    #K1 = EntryInfo('Quadrupole field strength', optional=False, enforce=float)
    FQ1 = EntryInfo('Soft edge fringe parameter', optional=False, enforce=float)
    FQ2 = EntryInfo('Soft edge fringe parameter', optional=False, enforce=float)
    
    
class Monitor(Base, Length, ApertureLimits, Kick, InstrumentalMeasurements, StraightLineOrientation, Floor):
    pass


class Drift(Base, Length, ApertureLimits, StraightLineOrientation, Floor):
    pass


class HKicker(Base, Length, ApertureLimits, Kick, StraightLineOrientation, Floor):
    KICK = EntryInfo('Integrated kick', optional=True, enforce=float)


class VKicker(Base, Length, ApertureLimits, Kick, StraightLineOrientation, Floor):
    KICK = EntryInfo('Integrated kick', optional=True, enforce=float)



class RBend(Base, ApertureLimits, Kick, Bend, BendOrientation, Floor):
    L_ARC = EntryInfo('Arc length', optional=False, enforce=str) # r bends only
    L = EntryInfo('Chord length of bend', optional=False, enforce=float)

    
class SBend(Base, ApertureLimits, Kick, Bend, BendOrientation, Floor):
    L = EntryInfo('Length of bend', optional=False, enforce=float)
    
    
class Wiggler(Base, Length, StraightLineOrientation, Kick, ApertureLimits, Floor):
    B_MAX = EntryInfo('Maximum magnetic field on the wiggler centerline', optional=False, enforce=float)
    L_PERIOD = EntryInfo('Length over which field vector returns to the same orientation', optional=False, enforce=float)
    N_PERIOD = EntryInfo('The number of periods', optional=False, enforce=float)
    POLARITY = EntryInfo('For scaling the field', optional=False, enforce=float)
    #KX = EntryInfo('Planar wiggler horizontal wave number', optional=False, enforce=float)
    #K1X = EntryInfo('Planar wiggler horizontal defocusing strength', optional=False, enforce=float)
    #k1y = EntryInfo('Planar wiggler vertical focusing strength', optional=False, enforce=float)
    G_MAX = EntryInfo('Maximum bending strength', optional=False, enforce=float)
    OSC_AMPLITUDE = EntryInfo('Amplitude of the particle oscillations', optional=False, enforce=float)
    
    
class Solenoid(Base, Length, ApertureLimits, StraightLineOrientation, Kick, Floor, GirderBendExtension):
    #KS = EntryInfo('Solenoid strength', optional=False, enforce=float)
    BS_FIELD = EntryInfo('Field strength', optional=False, enforce=float)
    L_SOFT_EDGE = EntryInfo('For modeling a soft fringe', optional=False, enforce=float)
    R_SOLENOID = EntryInfo('Solenoid radius', optional=False, enforce=float)

    
class Lcavity(Base, Twiss, Length, ApertureLimits, StraightLineOrientation, Kick, Floor):
    CAVITY_TYPE = EntryInfo('Solenoid strength', optional=False, enforce=float)
    GRADIENT =EntryInfo('Accelerating gradient', optional=False, enforce=float)
    GRADIENT_ERR = EntryInfo('Accelerating gradient error', optional=False, enforce=float)
    PHI0 = EntryInfo('Phase of the reference particle with respect to RF', optional=False, enforce=float)
    PHI0_MULTIPASS = EntryInfo('Phase with respect to a multipass lord', optional=False, enforce=float)
    PHI0_ERR = EntryInfo('Phase error', optional=False, enforce=float)
    E_LOSS = EntryInfo('Loss parameter for short range wakefields', optional=False, enforce=float)
    RF_FREQUENCY = EntryInfo('RF frequence', optional=False, enforce=float)
    VOLTAGE = EntryInfo('Cavity voltage', optional=False, enforce=float)
    L_ACTIVE = EntryInfo('Active region length', optional=False, enforce=float)
    N_CELL = EntryInfo('Number of cavity cells', optional=False, enforce=float)
    LONGITUDINAL_MODE  = EntryInfo('Longitudinal mode', optional=False, enforce=float)
    
                        
class Instrument(Base, Length, ApertureLimits, Kick, InstrumentalMeasurements, StraightLineOrientation, Twiss, Floor):
    pass

                        
class Marker(Base, Length, Twiss, ApertureLimits, StraightLineOrientation, Floor, GirderExtension):
    pass
    

class Multipole(Base, Length, Twiss, ApertureLimits, StraightLineOrientation, Floor,):
    #did not include mutlipole attributes
    pass