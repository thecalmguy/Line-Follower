#!/usr/bin/env python
# license removed for brevity
#import rospy
import cv2 
import numpy as np 
#from geometry_msgs.msg import Twist

def show(img):
	cv2.imshow('FRAME', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main_func():
	#read from camera
	#cap = cv2.VideoCapture('line_vid2.h264')
	#pub = rospy.Publisher('vel_control_topic', Twist, queue_size=10)
	#rospy.init_node('line_follower_node', anonymous=True)
	#rate = rospy.Rate(20) # 10hz
	# Check if camera opened successfully
	#if (cap.isOpened()== False): 
	#	print("Error opening video stream or file")
	
	#Twist control_msg
	# Read until video is completed
	#while cap.isOpened(): #and (not rospy.is_shutdown()):
		# Capture frame-by-frame
	#	ret, frame = cap.read()
	#	if ret == True:
			# Convert the img to grayscale 
			frame = cv2.imread("defective frame.jpg")
			#show(frame)
			gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			#kernel = 9
			#show(gray)
			#gray_blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
			#show(gray_blur)
			kernel2 = np.ones((30,30),np.uint8)
			erosion = cv2.dilate(gray,kernel2,iterations = 3)
			show(erosion)
			# Apply edge detection method on the image 
			edges = cv2.Canny(erosion,50,70,apertureSize = 3)
			show(edges)
			# This returns an array of r and theta values  
			lines = cv2.HoughLines(edges,1,np.pi/180, 100)
			#print(lines)
			#print(lines.shape)
			if lines is not None:
				print(lines)
				for r,theta in lines[0]:
					print('check')
					
					# Stores the value of cos(theta) in a 
					a = np.cos(theta) 

					# Stores the value of sin(theta) in b 
					b = np.sin(theta) 
					
					# x0 stores the value rcos(theta) 
					x0 = a*r 
					
					# y0 stores the value rsin(theta) 
					y0 = b*r 
					
					# x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
					x1 = int(x0 + 1000*(-b)) 
					
					# y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
					y1 = int(y0 + 1000*(a)) 

					# x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
					x2 = int(x0 - 1000*(-b)) 
					
					# y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
					y2 = int(y0 - 1000*(a)) 
					
					# cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
					# (0,0,255) denotes the colour of the line to be 
					#drawn. In this case, it is red. 
					cv2.line(frame,(x1,y1), (x2,y2), (0,0,255),5)

			# Display the resulting frame
			cv2.imshow('Frame',frame)
			print("frame processed")
		
			# Press Q on keyboard to  exit
			if cv2.waitKey(0) & 0xFF == ord('q'):
				cv2.destroyAllWindows()
				#cv2.imwrite("defective frame.jpg", frame)
				#break
			
			'''control_msg.linear.x =
			control_msg.linear.y =
			control_msg.linear.z =
			control_msg.angular.x =
			control_msg.angular.y =
			control_msg.angular.z =
			
			pub.publish(control_msg)
			'''
			
		#else: 
		#	break
		#rate.sleep()
	

	# When everything done, release the video capture object
	#cap.release()
	 
	# Closes all the frames
	
		
main_func()
'''if __name__ == '__main__':
    try:
        main_func()
    except #rospy.ROSInterruptException:
        pass'''
	
	
	

# Reading the required image in 
# which operations are to be done. 
# Make sure that the image is in the same 
# directory in which this python program is 
#img = cv2.imread('7.jpg') 



# The below for loop runs till r and theta values 
# are in the range of the 2d array 
		 
	
# All the changes made in the input image are finally 
# written on a new image houghlines.jpg 
#cv2.imwrite('linesDetected.jpg', img) 

