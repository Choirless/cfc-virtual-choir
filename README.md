# Virtual Choir
IBM Call for Code entry for Virtual Choir

Area of competition: Covid-19 Community / Communication


## Background:
My daughter is 9 years old, and a member of her school choir. The school has a fantastic school song that talks of being part of a community and talks of resilience -- something that resonates very well with current challenges with Covid-19 and the lockdown the UK. Pupils are now all schooling from home as the schools are now closed, and people are looking at new ways to stay connected remotely and feel a part of a community.


https://www.youtube.com/watch?v=7xltB716aO4


## Concept:
A tool that will allow the pupils to perform a "concert' of the school song together, despite all being at home in isolation. This would be a hosted tool, a SchoolRemoteChoir-aaS if you will, that would allow any school (or community choir) to sing together.

The production will be mostly automated, and use machine learning to stich and composite all the audio and video input into
a single production. This should be usable by a school music teacher without any specific skills in video/audio editing or production.

## Inspirations:
Technology - TikTok duets allow people to remotely "duet" with other existing videos. One person sings/mimes/dances one part, and someone else then asynchronously does the second part. They are then merged together on the backend.
Community - The film "Military Wives" (https://www.imdb.com/title/tt8951692/) is a recent film based on a true story about a group of wives and partners on a military base forming a choir as part of community building whilst their partners are off on deployment. 


## Process Workflow:
1) The choir "leader" creates a "concert" on the site, and uploads a video of themselves singing, conducting, along with the backing music (if any) and lyrics if needed.
2) Invites are sent out through other means to pupils to join in by a certain deadline (say, a week)
3) Participants (pupils) go to the invite URL on phone/tablet/computer and are taken through initial consent agreements and any T&Cs, safeguarding information, and tips for recording
4) The participants is then able to play the leader's video and sing along, recording their own audio and video (so you get to see their surroundings: in the garden, kitchen, living room, etc)
5) The participant can play it back and repeat as necessary until they are happy
6) Participant clicks "upload/save" to upload/save the recorded video
7) Server uses Watson Machine Learning to compare the recorded audio to that of the leader to ensure that it matches to a certain level (to prevent rubbish being uploaded), non-matching videos flagged
8) The backend then merges the audio tracks, normalising the volumes, syncing them up and creates a rendered "concert" that has a montage of the video feeds, perhaps rotating through several "canned" arrangements.
9) Leader can give final approval to rendered output
10) Concert is then published on the site for public to see along with links to syndicate to Youtube etc.


## Additional "stretch" goals:
1) Rudimentary editing controls for choir leader allowing them to highlight soloists etc.
2) "Personalised" versions of the concert in which certain participant is highlighted more frequently 


## Technical elements:
1) Backend service - Hosted on IBM Cloud, possibly deployed with Kubernetes if needed, or hosted on Cloud Functions. Utilises Watson Machine Learning features for processing the audio and video feeds
2) Web / Mobile front end. This could just be a web page, or could be an installable mobile app
3) Management consoles for managing the deployments /concerts / etc.

## Similar ideas

### Freedonia Symphonic Band Virtual Concert

This is a manual attempt doing the same with a school symphony band

![Freedonia Symphonic Band Virtual Concert](/doc_images/Freedonia-Symphonic-Band.png)

https://youtu.be/f-b4HJ04OdQ

### Eric Whitacre's Virtual Choir

This is a high-production art installation in which a mass virtual choir has been created. Again, this is 
manually stiched together and produced

![Eric Whitacre's Virtual Choir](/doc_images/Eric-Whittacre-Virtual-Choir.png)

https://ericwhitacre.com/the-virtual-choir

