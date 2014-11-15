import numpy as np
import cv2
import sys
import libardrone.libardrone as libardrone
import time

TARGET_COLOR_MIN = np.array([0,100,100], np.uint8)
TARGET_COLOR_MAX = np.array([5,255,255], np.uint8)

def main():
	W, H = 640, 360
	screenMidX = W/2
	screenMidY = H/2
	speedCirclesDiff = H/12
					
	drone = libardrone.ARDrone(True, False)
	time.sleep(0.5)
	drone.reset()
	time.sleep(0.5)
	#drone.set_camera_view(True) # False for bottom camera
	#sleep(0.5)
	drone.set_speed(0.3)
	time.sleep(0.5)
	drone.takeoff()
	print "take off"
	time.sleep(0.5)
	drone.hover()
	time.sleep(0.5)
	
	running = True
	while running:
		try:
			# This should be an numpy image array
			pixelarray = drone.get_image()
			if pixelarray != None:
				# Convert RGB to BGR & make OpenCV Image
				frame = pixelarray[:, :, ::-1].copy()
				
				_frame = np.asarray(frame)
				frameHSV = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)
				frameThreshold = cv2.inRange(frameHSV, TARGET_COLOR_MIN, TARGET_COLOR_MAX)
				
				element = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
				frameThreshold = cv2.erode(frameThreshold,element, iterations=1)
				frameThreshold = cv2.dilate(frameThreshold,element, iterations=1)
				frameThreshold = cv2.erode(frameThreshold,element)
				
				# Blurs to smoothen frame
				frameThreshold = cv2.GaussianBlur(frameThreshold,(9,9),2,2)
				frameThreshold = cv2.medianBlur(frameThreshold,5)
				
				# Find Contours
				contours, hierarchy = cv2.findContours(frameThreshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
				
				showingCNTs = [] # Contours that are visible
				areas = [] # The areas of the contours
				
				# Find Specific contours
				for cnt in contours:
					approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
					#if len(approx)==4:
					area = cv2.contourArea(cnt)
					if area > 300:
						areas.append(area)
						showingCNTs.append(cnt)
				
				# Only Highlight the largest object
				if len(areas)>0:
					m = max(areas)
					maxIndex = 0
					for i in range(0, len(areas)):
						if areas[i] == m:
							maxIndex = i
					cnt = showingCNTs[maxIndex]
					
					# Highlight the Object Red
					#cv2.drawContours(frame,[cnt],0,(0,0,255),-1)
					
					# Draw a bounding rectangle
					x,y,w,h = cv2.boundingRect(cnt)
					cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
					
					# Draw a rotated bounding rectangle
					rect = cv2.minAreaRect(cnt)
					box = cv2.cv.BoxPoints(rect)
					box = np.int0(box)
					cv2.drawContours(frame,[box],0,(0,255,255),2)
					
					# Draw a circumcircle
					(x,y),radius = cv2.minEnclosingCircle(cnt)
					center = (int(x),int(y))
					radius = int(radius)
					cv2.circle(frame,center,radius,(255,0,255),2)
					
					# Draw line to center of screen
					cv2.line(frame, (screenMidX, screenMidY), center, (0,0,255),2)
					
					# Draw Speed Limit Circles and Determine Speed
					diff = speedCirclesDiff # Increment of radius of the Speed Limit Circles
					
					# Loop for drawing speed circles
					for i in range(1, 10):
						cv2.circle(frame, (screenMidX, screenMidY), diff*i,(0,0,255),2)
					
					# Center of the object	
					x = center[0]
					y = center[1]	
					'''
					hor_speed = 0.0
					vert_speed = 0.0
					
					# Loop for checking speed
					for i in range(1, 10):
						_diff = diff*i
						if (640-_diff)<x<(640+_diff): # On the x axis
							hor_speed = (i-1)/10
							break
							
					for i in range(1, 10):
						if (360-_diff)<y<(360+_diff): # On the y axis
							vert_speed = (i-1)/10
							break
					'''
					# Check direction of the ball
					centerThresh = 50 # The 'centre' threshold for the ball
					# On the X axis -> Note: Inverse
					if (screenMidX-x) < -centerThresh: # To the left to the left
						drone.turn_right()
						#print "Left"
					if (screenMidX-x) > centerThresh: # To the right to the right
						drone.turn_left()
						#print "right"
					if -centerThresh < (screenMidX-x) < centerThresh:
						#drone.hover()
						pass
						#print "Stop Rotating"
						
					# On the Y axis
					if (screenMidY-y) < -centerThresh: # Down!
						drone.move_down()
					if (screenMidY-y) > centerThresh: # Up!
						drone.move_up()
					if -centerThresh < (screenMidY-y) < centerThresh:
						#drone.hover()
						pass
						#print "Stop Moving up or down"
						
				# Get battery status of the drone
				bat = drone.navdata.get(0, dict()).get('battery', 0)
				#print str(bat)
				if bat < 20:
					running = False
					print "Low Battery: "+str(bat)
								
				# Display the Image
				cv2.imshow('Drone', frame)
		except:
			print "Failed"
		'''
		if cv2.waitKey(1) & 0xFF == ord('w'):
			print "Take OFF!!"
			drone.reset()
			drone.takeoff()
			drone.hover()
		'''
		# Listen for Q Key Press
		if cv2.waitKey(1) & 0xFF == ord('q'):
			running = False
	
	# Shutdown
	print "Shutting Down..."
	drone.land()
	drone.halt()
	print "Ok."
	
if __name__ == '__main__':
	main()