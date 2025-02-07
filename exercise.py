import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("ejercico1_opcional_MSR/exercise.urdf")

frictionId = p.addUserDebugParameter("friction", 0, 10, 0)
torqueID = p.addUserDebugParameter("torque",-10,10,0)

numJoints = p.getNumJoints(robotId)
print("NumJoints: {}".format(numJoints))
for j in range(numJoints):
     print("{} - {}".format(p.getJointInfo(robotId,j)[0], p.getJointInfo(robotId,j)[1].decode("utf-8")))


while(1):
    friction = p.readUserDebugParameter(frictionId)
    force = p.readUserDebugParameter(torqueID)

    p.setJointMotorControl2(robotId, 0, p.VELOCITY_CONTROL, targetVelocity=0)
    p.setJointMotorControl2(robotId, 1, p.TORQUE_CONTROL, force=force)
    p.setJointMotorControl2(robotId, 1, p.VELOCITY_CONTROL, targetVelocity=0, force=friction)
    
    p.stepSimulation()
    time.sleep(1./240.)
    
p.disconnect()
