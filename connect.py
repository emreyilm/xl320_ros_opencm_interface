#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import numpy as np

class Struct:
   pass

class xl320():

   def __init__(self):

      self.servo1 = Float32()
      self.servo1_pub = rospy.Publisher('/servo1', Float32, queue_size=10)

      self.servo2 = Float32()
      self.servo2_pub = rospy.Publisher('/servo2', Float32, queue_size=10)

      self.servo3 = Float32()
      self.servo3_pub = rospy.Publisher('/servo3', Float32, queue_size=10)

   def iteration(self, event):
         
      self.servo1 = np.float32(3.14*40/180)#0 .. 80!!!
      self.servo2 = np.float32(3.14*60/180)#10 ... 180!!
      self.servo3 = np.float32(3.14*90/180)# 25 .. 90!!!!
         
      #rospy.loginfo("Joint data published %f, %f, %f", (float)self.servo1, (float)self.servo2, (float)self.servo3)
      print "Joint data published"
      self.servo1_pub.publish(self.servo1)
      self.servo2_pub.publish(self.servo2)
      self.servo3_pub.publish(self.servo3)

if __name__ == '__main__':

   rospy.init_node('xl320', anonymous=True)

   try:
      xl320joints   = xl320()
      rospy.Timer(rospy.Duration(1.0/10.0), xl320joints.iteration)   
      rospy.spin()                  # keep process alive

   except rospy.ROSInterruptException:
      rospy.loginfo("xl320 joint node is terminated.")

