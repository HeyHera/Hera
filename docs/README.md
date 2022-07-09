# Hera - An Operating System Level Voice Recognition Package
Our project propose a new way of interacting with the operating system that prioritizes on improving the user experience via voice commands. It is able to recognize the spoken language and is able to draw meaningful conclusions from it and to provide responses accordingly.

## Introduction
Our project propose a new way of interacting with the operating system that prioritizes on improving the user experience via voice commands. 
It is able to recognize the spoken language and is able to draw meaningful conclusions from it and to provide responses accordingly. 
Unlike the traditional approach which rely heavily on the physical inputs, our proposed system can provide an alternative method through the means of voice interactions. 
Though we are developing a voice based system, the traditional physical input is still available, so the user can experience the best of both worlds.

## Features
- [X] Custom wake word detection
- [X] Natural Language Understanding
- [X] Ability to launch applicatons
- [X] Launch custom Scripts
- [X] Play music and movies from the folder specified
 
## Features to be added
- [ ] Usage analysis

## Methodology
For effective and efficient embedding of speech recognition into Linux Operating System, we employ a multimodule approach, namely Assistant, Coordinator and Skill modules.
These modules determine how the voice data is collected, processed and evaluated. The entire working of the system is divided into two phases,
Assistant-Coordinator (Primary) phase and Coordinator-Skill-Synthesis (Secondary) phase.
The primary phase consist of transcribing the voice data to the corresponding intents.
The secondary phase deals with mapping intents into corresponding skills and providing feedback in the form of speech or raw data.
[Read more](https://github.com/gokulmanohar/Hera/blob/master/docs/Hera%20-%20Project%20Preliminary%20Report%20With%20Schedule.pdf)

## Working
[![Design-Block-Diagram.jpg](https://i.postimg.cc/8PK7BRqX/Design-Block-Diagram.jpg)](https://postimg.cc/fJdWM9WY)

## Installation
### Hera is written in python,so you need to have it installed
Check it by: 
```
python --version
```
We recommend installing Hera on seperate virtual environment
### Setting up virtual environment
```
sudo apt install python3-venv
```
```
python3 -m venv Hera
```
### Clone the repositry :
```
git clone https://github.com/HeyHera/Hera.git
```
### 
### Installing dependencies
```
pip install -r requitements.txt
```

### Before running Hera,test your microphone  
```
arecord -f cd -d 10 --device="hw:0,0" /tmp/test-mic.wav
aplay /tmp/test-mic.wav
```

### Running Hera
```
python hera.py
```


### Members of the team  
- [Arjun Vishnu Varma](https://github.com/Arjun-Varma2)
- [Gokul Manohar](https://github.com/gokulmanohar)
- [Jithin James](https://github.com/jithinjames017)
- [Nandu Chandran](https://github.com/Nandu-Chandran)
