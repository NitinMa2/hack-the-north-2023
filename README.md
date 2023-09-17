# 💃 Motion2Music 🎶

Created by Nitin Mathew, Marwan Ali, Mona Pei, William Wen at  **Hack The North 2023**

## 🍃 Inspiration

The inspiration for the project was an old Xbox 360 Kinect. We saw how it could play music and sense people and track them as they danced. So, we thought what if we did that backwards?

## ❔ What it does

Motion2Music converts dance into music using pose detection and generative AI. Includes an arduino based companion that dances along with you.

## 🏗️ How we built it

Motion2Music is built using the following technologies:

Python3, OpenCV, MediaPipe, Cohere API, Arduino

We convert motion to music by doing the following: Record the person's movements and track major landmarks using OpenCV and ML models from MediaPipe. These landmarks are then converted to prompts to generate music lyrics using Cohere. The lyrics are then converted to sound using TTS and overlayed ontop of a melody and the original video. The result is completely new music generated for your dance everytime.

We also have an Arduino-based companion which can dance to the generated music.

## 🚧 Challenges we ran into

The biggest challenge we ran into created the project that we have. We originally all wanted to do a hardware hack and do something cool with sensors, breadboards and microcomputers but didn't manage to get our hands on enough to persue a full hardware project. But, we were able to instead pivot to a different class of project and still include hardware in the form of a little dancing motor. 

## 🏅 Accomplishments we're proud of

We're most proud of ourselves for meeting each other. Most of us had the opportunity of teaming up with people we were already familiar with but instead decided to get out of our comfort zone and meet new people. We all learned new things from each other and were exposed to new perspectives on existing things. [some concluding sentence maybe]

## 📖 What we learned

As individuals, we all walked away with some kind of new skill. For some of us it was learning a new API or library and for some it was an introduction to a whole class of projects. As a team, I think we learned (or at least had the idea reinforced) the importance of trying new things. Obviously, we all walked into a hackathon with the intention of finding a team full of brand new people so we had some of this in us already. But, this experience really exemplified why we bother to try new things and get out of our comfort zone. Each of us not only learned a skill, but a way of life.

## 🔮 What's next for Motion2Music?

The next step for Motion2Music is to generate music and lyrics live. This would be challenging because even a very low latency can be detected by people as a desync and be incredibly uncomfortable. We would have to figure out how to speed up out pipeline lots and find ways to reduce this desync effect.
