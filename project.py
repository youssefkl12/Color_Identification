import argparse
import pandas as pd
import cv2
#double click on the point to show the color name and hex
b=g=r=xLoc=yLoc=clicked=0
#implemnt the function that will calculate the rgb values for the location clicked

def onClickFunction(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xLoc,yLoc,clicked
        clicked=True
        xLoc=x
        yLoc=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
#this function wiil return the closest color name matching the values from the data set 
def colorName(r,g,b):
    mini=100000
    for i in range(len(csv)):
        temp=abs(r-int(csv.loc[i,"r"]))+abs(g-int(csv.loc[i,"g"]))+abs(b-int(csv.loc[i,"b"]))
        if (temp<=mini):
            mini=temp
            foundName=csv.loc[i,"name"]
    return foundName




   
#we will enter the image path through the terminal 
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
#reading the image and the csv file 
img = cv2.imread(img_path)
index=['color','name','hex','r','g','b']
csv=pd.read_csv('colors.csv',names=index,header=None)
#display the input image and call the mouse function 
cv2.namedWindow('image')
cv2.setMouseCallback('image',onClickFunction)

while(1):
    cv2.imshow("image",img)
    if(clicked):
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text=colorName(r,g,b)+"r="+str(r)+"g="+str(g)+"b="+str(b)
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    #press esc to exit the image 
    if cv2.waitKey(20) & 0xFF ==27:
        break    
cv2.destroyAllWindows()