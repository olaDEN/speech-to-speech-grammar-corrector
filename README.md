# Ai-speech-to-speech-grammer-corrector
A speech to speech  grammar corrector application using python and streamlit

![Screenshot (106)](https://user-images.githubusercontent.com/97802281/202772404-d06c5121-a3b4-4b27-b360-aa9e41fba6e8.png)


## **How to use:**

1- Open the CMD panel as an administrator and write the following command:
>> pip install -r requirements.txt.

2- Clone the repository to your local.

3- Open the CMD panel again, navigate to the folder where you cloned the repository and write the following command:
>> streamlit run gr-chatbot.py

4- If the browser's window did't open automatically, go to the Local URL: http://localhost:****.

P.S.: **** indicates the local host shown on the CMD, e.g. 8081

5- Make sure that your microphone on your local is allowing apps to access it: 
For Windows: *Settings -> Microphone Privacy Settings -> turn "Allow apps to access your microphone on"*.

6- Once the gr-chatbot.py is loaded to the browser, you can click the "Speak" button and speak clearly with short and one sentence at a time, simple sentences works better ( Ex: You is beuatiful -> You are beutiful) (Like do not read a statement and expect the chatbot to answer you :D).

P.S.: You do not need to continuously pressing the speak button while you speak, just click it once and start, once you finish speaking, the chatbot will wait for couple of seconds and then will answer you (with voice and text).

7- For better performance, try to refresh the site after 5 speak tries (Issue related to the pretrained model).

8- Have fun ;)

9- Do not forget to chack the references.  **kindly keep the source info.**

**Since this is a pretrained model, the answeres may be unexpected sometimes, either because of isseus related to microphone's quality or grammar evaluation.**
