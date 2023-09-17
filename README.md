# Motion2Music

Created by Nitin Mathew, Marwan Ali, Mona Pei, William Wen at  **Hack The North 2023**

## Inspiration

an xbox 360 kinect

## What it does

Motion2Music converts dance into music using pose detection and generative AI. Includes an arduino based companion that dances along with you.

## How we built it

Motion2Music is built using the following technologies:

Python3, OpenCV, MediaPipe, CoHere API, Arduino

1. The user starts the program by clicking "start" on the GUI
2. StudyCam starts to keep track of the user's face using OpenCV face detection technologies
3. If the user leaves their study area for too long, StudyCam will start keeping track of information such as time gone, and amount of absences.
4. Once the user finishes their study session, they will be presented with a detailed summary of their session.

## Challenges we ran into

We had a great deal of difficulty working with OpenCV and optimizing their prebuilt models for our specific use case. Specifically, oftentimes in our project, the webcam wasn't directly viewing the front of a person's face, as people usually study with their heads facing down. We had to fine tune the model to be able to detect the noisy data, in addition to being able to track when the person left the frame.

## Accomplishments we're proud of

None of us had ever extensively used OpenCV before, or frankly any form of computer vision, so we're proud that we were able to implement such an advanced topic into our project.

## What we learned

- How computer vision works, and how to fine tune prebuilt models for personal usage
- How to communicate data in between a front end GUI, an external REST API, and a backend program

## What's next?

We have a lot of ideas for future additions that we didn't have time to implement this weekend at DeltaHacks:

1. Implement functionality into a chrome extension
2. More detailed reports, maybe include information such as total break time
3. More accurate face/studying detection
4. Analyze data from multiple study sessions to give user insightful data on their study habits