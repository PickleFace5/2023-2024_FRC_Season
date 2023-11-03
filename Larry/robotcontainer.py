import wpilib
from wpilib import XboxController

import commands2
import constants
# import commands
from commands.drive_with_controller import DriveWithController
from commands.charge_station import ChargeStation
# import subsystems
from subsystems.swerve_drive import SwerveDrive

"""
LARRY BUT WITH TRIG FUNCTIONS

The old version used angle weirdness to control the robot, but as of 11/2/2023, it has NOT been going well.
This test repo uses simple vertex math to attempt to easily create swerve drive.
"""
class RobotContainer:
    def __init__(self) -> None:
        # init controllers
        self.driverController = XboxController(constants.kdriverControllerPort)

        # init drive motors (may not be necessary)

        self.timer = wpilib.Timer

        # init subsystems
        self.swerveDrive = SwerveDrive()
        # auto chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to auto command chooser
        self.chargeStation = ChargeStation(self.swerveDrive)
        """
        self.simple_auto = SimpleAuto(self.drive)
        self.complex_auto = ComplexAuto(self.drive)
        #set a default option
        #add options
        #show autonomous on the driver station
        """

        self.chooser.addOption("Charge Station", self.chargeStation)

        self.configureButtonBindings()

        self.swerveDrive.setDefaultCommand(
            DriveWithController(self.swerveDrive, lambda: self.driverController.getLeftX(),
                                lambda: self.driverController.getLeftY(), lambda: self.driverController.getRightX()
                                ))

    def configureButtonBindings(self):
        """This is where our trigger bindings for commands go"""

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()